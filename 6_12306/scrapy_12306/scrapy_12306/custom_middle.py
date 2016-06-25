# -*- coding: utf-8 -*-
import datetime

from scrapy.exceptions import IgnoreRequest

class CustomDownloaderMiddleware(object):

    def process_request(self, request, spider):
        spider.logger.info("in midderware, " + request.url)
        if "expire" in request.meta:
            s1 = request.meta["expire"]
            s2 = datetime.datetime.now()
            if s1 < s2:
                spider.logger.warning("in midderware, " + request.url + " expire.")
                raise IgnoreRequest()
            else:
                return None

        else:
            spider.logger.info("in midderware, don't deal")
            return None

















# vim: set ts=4 sw=4 sts=4 tw=100 et:
