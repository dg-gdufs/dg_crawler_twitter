# encoding: utf-8
'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-03 20:35:40
LastEditors: Renhetian
LastEditTime: 2022-01-03 21:19:07
'''

from config.host_config import *

class ProxyDownloaderMiddleware:
    '''
    proxy下载中间件
    '''

    def process_request(self, request, spider): 
        try:
            request.meta['proxy'] = PROXY_HOST_LIST[spider.proxy]
        except Exception as e:
            spider.send_log(3, "ProxyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, request.url))