import random
import time

from common.basemethod import RequestMethod
from common.globalvar import BASE_URL, getHeader
from inteface.loginparam import Login
from tables.connect_server import Server


class Base(object):

    def __init__(self):
        self.req = RequestMethod(BASE_URL)

    def getConn(self):
        return Server()

    def rand(self):
        random_str = str(random.randrange(1, 9999999999, 10))
        return random_str

    def getTime(self):
        timestamp = lambda: int(time.time() * 1000)
        return str(timestamp())

    @staticmethod
    def getHeader(token, num):
        if num == 0:
            header = getHeader(1, 2, token)
        else:
            header = getHeader(1, 1, token)
        return header


if __name__ == '__main__':
    a = Login().login_response()
    print(Base.getHeader(a, 1))