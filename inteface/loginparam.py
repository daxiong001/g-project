from common.basemethod import RequestMethod
from common.globalvar import getHeader, get_KeyValue, BASE_URL


class Login(object):

    def __init__(self, method="POST", url="/api/iam/v1/user/login"):
        self.method = method
        self.url = url
        self.header = getHeader(0, 2)
        self.request = RequestMethod(BASE_URL)

    def login_param(self):
        data = {
            "username": "admin",
            "password": "T7Y3CL+Xg8830KxbCoCu6H+oVLuOZfYtr8STTTvr+HXg2ulHl7uf1nyCtgZ7ddc9LeWNC6NkmTpxTSYu94SdQ0fkZEiokdZz/H+D7+UfmzIktJGUrF5666KEh5bIssLdctNBA0QZW4QXZstK4wpSvE8ld48wGI8tYO9cMbw+XBg=",
            "webType": "OPERATION_ADMIN"
        }
        return data

    def login_response(self):
        result = self.request.request(url=self.url, method=self.method, json=self.login_param(), headers=self.header)
        token = get_KeyValue(result.json(), "access_token")
        return token


if __name__ == '__main__':
    Login().login_response()
