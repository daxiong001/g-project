import requests

from common.basemethod import RequestMethod
from locustdemo.result_base import ResultBase
from utils.logger import api_log_decorator


class Login(object):

    def __init__(self):
        self.url = "https://qaadminweb.yaowutech.cn/api/iam/v1/user/login"
        self.headers = {"content-type": "application"}
        self.data = {
            "username": "admin",
            "password": "T7Y3CL+Xg8830KxbCoCu6H+oVLuOZfYtr8STTTvr+HXg2ulHl7uf1nyCtgZ7ddc9LeWNC6NkmTpxTSYu94SdQ0fkZEiokdZz/H+D7+UfmzIktJGUrF5666KEh5bIssLdctNBA0QZW4QXZstK4wpSvE8ld48wGI8tYO9cMbw+XBg=",
            "webType": "OPERATION_ADMIN"
        }

    def postRequest(self):
        #result = ResultBase()
        res = requests.post(self.url, json=self.data)
        #result.response = res
        print(res.json())
        return res.json().get("data").get("access_token")


@api_log_decorator
def gt_login():
    req = RequestMethod("http://127.0.0.1:8000/api/server/v1/")
    response = req.request(url="admin/user/input", method="GET")
    return response
if __name__ == '__main__':
    gt_login()