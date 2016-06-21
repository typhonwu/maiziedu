# -*- coding: utf-8 -*-
import scrapy
from topgoods.items import TopgoodsItem
import pdb

class TmGoodsSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domains = ["http://www.tmall.com"]
    start_urls = (
        'http://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter',
    )
    # 记录处理的页数
    count = 0


    def randomtime(self):
        str1=str(time.time()).replace(".",'')
        str2=time.strftime("%H%M", time.localtime())
        return "_".join([str1,str2])
    
    def generate_request(self,response):
        '''获得推荐商品的URL'''
        
        para_dict = OrderedDict()

        text = response.xpath('//textarea[@class="ks-datalazyload"]/script')
        j_command = response.xpath('//div[@id="J_Recommend"]')
        attr = j_command.xpath('@data-p4p-cfg').extract()[0]
        attr_dict = eval(attr)
        para_dict['pid'] = attr_dict['pid']
        
        son_dict = OrderedDict()
        son_dict['sbid'] = 2
        son_dict['frcatid'] = attr_dict['frontcatid']
        son_dict['keyword'] = attr_dict['keyword']
        son_dict['pid'] = attr_dict['pid']
        son_dict['offset'] = 45
        son_dict['propertyid'] = attr_dict['propertyid']
        son_dict['gprice'] = attr_dict['gprice']
        son_dict['loc'] = attr_dict['loc']
        son_dict['sort'] = attr_dict['sort']
        son_dict['feature_names'] = ("promoPrice,multiImgs,tags,dsrDeliver,dsrDeliverGap"
            ",dsrDescribe,dsrDescribeGap,dsrService,dsrServiceGap")
        son_query = urllib.quote(urllib.urlencode(son_dict))
        
        para_dict['qs1'] = son_query
        para_dict['_ksTS'] = self.randomtime()
        para_dict['cb'] = "json519"
        
        end_url = "?".join(["https://mbox.re.taobao.com/gt",urllib.urlencode(para_dict)])
        
        return end_url
        
    def parse_recommand(self,response):
 
        aim_str = re.findall(r'json519\((.*?)\)',response.body)
        
        if aim_str:
            json_obj = json.loads(aim_str[0])
            for obj in json_obj['data']['ds1']:
                item = TopgoodsItem()
                item["GOODS_URL"] = obj['eurl']
                item["GOODS_PRICE"] = obj['price']
                item["GOODS_NAME"] = obj['title']

                yield item

    def parse(self, response):

        TmGoodsSpider.count += 1
        divs = response.xpath(
            "//div[@id='J_ItemList']/div/div[@class='product-iWrap']")
        # 如果没有取到想要的元素就报错
        if not divs:
            self.log("List Page error--%s" % response.url)

        for div in divs:
            item = TopgoodsItem()
            # 商品价格
            item["GOODS_PRICE"] = div.xpath(
                "p[@class='productPrice']/em/@title")[0].extract()
            # 商品名称
            item["GOODS_NAME"] = div.xpath(
                "p[@class='productTitle']/a/@title")[0].extract()
            # 商品连接
            pre_goods_url = div.xpath(
                "p[@class='productTitle']/a/@href")[0].extract()
            # 如果不是绝对链接就拼接一下
            item["GOODS_URL"] = pre_goods_url if "http:" in pre_goods_url else ("http:" + pre_goods_url)

            # 图片链接
            try:
                # 注意图片元素有两种xpath表达式
                # 这里其实写成一行是这样的：
                # 'div[@class="productImg-wrap"]/a[1]/img/@src|div[@class="productImg-wrap"]/a[1]/img/@data-ks-lazyload'
                file_urls = div.xpath(
                    'div[@class="productImg-wrap"]/a[1]/img/@src|'
                    'div[@class="productImg-wrap"]/a[1]/img/@data-ks-lazyload').extract()[0]
                item['file_urls'] = ["http:" + file_urls]
            except Exception,e:
                print "Error: ",e
                pdb.set_trace()


            yield scrapy.Request(
                url=item["GOODS_URL"],
                meta={'item': item},
                callback=self.parse_detail, # 对每个抓取的链接返回一个请求，并调用这个回调函数进入下一个页面处理
                dont_filter=True)


    # 这是跳转到第二个页面之后调用的函数
    # 多个页面跳转之后，用item把所有数据组合好
    # 最后再返回
    def parse_detail(self, response):

        div = response.xpath('//div[@class="extend"]/ul')
        # 如果没有取到元素就用日志报错
        if not div:
            self.log("Detail Page error--%s" % response.url)

        item = response.meta['item']
        div = div[0]
        # 店铺名称
        item["SHOP_NAME"] = div.xpath("li[1]/div/a/text()")[0].extract()
        # 店铺连接
        item["SHOP_URL"] = div.xpath("li[1]/div/a/@href")[0].extract()
        # 公司名称
        item["COMPANY_NAME"] = div.xpath(
            "li[3]/div/text()")[0].extract().strip()
        # 公司所在地
        item["COMPANY_ADDRESS"] = div.xpath(
            "li[4]/div/text()")[0].extract().strip()

        yield item
