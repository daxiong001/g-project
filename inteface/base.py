import random
import time

from common.basemethod import RequestMethod
from common.globalvar import BASE_URL, headers
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
    def getHeader(token, num=None):
        if num == 0:
            header = headers(type=1, i=2, token=token)
        elif num == 2:
            header = headers(type=2, token=token)
        else:
            header = headers(type=1, i=2, token=token)
        return header


if __name__ == '__main__':
    s = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDEzOTMwMDIsInVzZXJfbmFtZSI6ImFkbWluIiwidXNlckRldGFpbCI6eyJ1c2VybmFtZSI6ImFkbWluIiwicmVhbE5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjpudWxsLCJ1c2VySWQiOjEsImxhbmd1YWdlIjpudWxsLCJhdXRob3JpdGllcyI6bnVsbCwiZGF0YU1hcCI6eyJ1c2VybmFtZSI6ImFkbWluIiwibW9iaWxlIjoiMTg4ODg4ODg4ODgiLCJyb2xlcyI6IlNVUEVSX0FETUlOIn0sImVuYWJsZWQiOnRydWUsImFjY291bnROb25FeHBpcmVkIjp0cnVlLCJhY2NvdW50Tm9uTG9ja2VkIjp0cnVlLCJjcmVkZW50aWFsc05vbkV4cGlyZWQiOnRydWV9LCJqdGkiOiJmM2Q4ODQzNS00NzRlLTQ1YzUtYmY0Ny0zYmZlYjIxYzA5ZTEiLCJjbGllbnRfaWQiOiJnLWZyb250Iiwic2NvcGUiOlsib3BlbmlkIl19.SxVR_oIXx9Bn06M2OaH71tVgfqBS71e09jWcD3zF5pmTw2TG5EBYvX4a2BUX5Me8_TvSGIcD9c5ggvD-4NaqY1O6dYcpARFr5aQrTXp3iNOaubRCRjUnBWbI2czjLA-ws_UGR143BGk_VRNuzZ53M5MnwUbeDT1JzTX_yFFI5ls"
    a = Login().login_response()
    print(Base.getHeader(token=s, num=2))