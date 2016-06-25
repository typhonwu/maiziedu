# -*- coding: utf-8 -*-

#import hashlib

from scrapy.dupefilters import RFPDupeFilter

class CustomURLFilter(RFPDupeFilter):
    def request_fingerprint(self, request):
        if "timestamp" in request.meta:
            return request.url + "--" + request.meta["timestamp"]
        else:
            return request.url














# vim: set ts=4 sw=4 sts=4 tw=100 et:
