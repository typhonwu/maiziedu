from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import pdb
class MyImagesPipeline(ImagesPipeline):
    # 这里的request就是图片链接请求
    def file_path(self, request, response=None, info= None):
        pdb.set_trace()
        image_guid = request.url.split('/')[-1]
        return 'full/%s/%s' % (image_guid.split('.')[0], image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['post_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item 