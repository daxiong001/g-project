import requests
import json as complexjson
# from utils.logger import log_filter


class RequestMethod(object):

    def __init__(self, base_url):
        self.root_url = base_url


    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.root_url + url
        if method == "GET":
            return requests.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                data = complexjson.dumps(json)
            return requests.put(url, data, **kwargs)
        if method == "DELETE":
            return requests.delete(url, **kwargs)
        if method == "PATCH":
            return requests.patch(url, data, **kwargs)
