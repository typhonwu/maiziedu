# -*- coding: utf-8 -*-
import scrapy
from topgoods.items import TopgoodsItem


class TmGoodsSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domains = ["http://www.tmall.com"]
    start_urls = (
        'http://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter',
    )
    # 记录处理的页数
    count = 0

    def parse(self, response):

        TmGoodsSpider.count += 1

        divs = response.xpath(
            "//div[@id='J_ItemList']/div[@class='product']/div")
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
                import pdb
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
