import os

import requests

from inteface.base import Base
from inteface.loginparam import Login
from utils.logger import log_filter


class fileLoad(Base):
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    imagePath = os.path.join(rootPath, "resources/sc.png")

    def __init__(self, method="POST", url="/api/third-party/v1/api/file/file-upload"):
        super().__init__()
        self.method = method
        self.url = url

    def fileParam(self):
        data = {
            "fileName": "sc.png",
            "file": [{
                "url": self.imagePath,
                "type": "null",
                "name": "sc.png"
            }],
            "type": "PRIVATELY"
        }
        return data

    def postFile(self, token, num):
        response = self.req.request(self.url, self.method, data=self.fileParam(),
                                    headers=super(fileLoad, self).getHeader(token, num))
        return response.json()

    def fileFunction(self):
        files = {"file": ("sc.png", open(r"/Users/daixiongkun/PycharmProjects/g-project/resources/sc.png", "rb"), "image/png")}
        header = {
            # "Content-Type":"multipart/form-data",
            "Authorization": "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDEzOTMwMDIsInVzZXJfbmFtZSI6ImFkbWluIiwidXNlckRldGFpbCI6eyJ1c2VybmFtZSI6ImFkbWluIiwicmVhbE5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjpudWxsLCJ1c2VySWQiOjEsImxhbmd1YWdlIjpudWxsLCJhdXRob3JpdGllcyI6bnVsbCwiZGF0YU1hcCI6eyJ1c2VybmFtZSI6ImFkbWluIiwibW9iaWxlIjoiMTg4ODg4ODg4ODgiLCJyb2xlcyI6IlNVUEVSX0FETUlOIn0sImVuYWJsZWQiOnRydWUsImFjY291bnROb25FeHBpcmVkIjp0cnVlLCJhY2NvdW50Tm9uTG9ja2VkIjp0cnVlLCJjcmVkZW50aWFsc05vbkV4cGlyZWQiOnRydWV9LCJqdGkiOiJmM2Q4ODQzNS00NzRlLTQ1YzUtYmY0Ny0zYmZlYjIxYzA5ZTEiLCJjbGllbnRfaWQiOiJnLWZyb250Iiwic2NvcGUiOlsib3BlbmlkIl19.SxVR_oIXx9Bn06M2OaH71tVgfqBS71e09jWcD3zF5pmTw2TG5EBYvX4a2BUX5Me8_TvSGIcD9c5ggvD-4NaqY1O6dYcpARFr5aQrTXp3iNOaubRCRjUnBWbI2czjLA-ws_UGR143BGk_VRNuzZ53M5MnwUbeDT1JzTX_yFFI5ls"
        }
        response = requests.post(url="http://qaadminweb.yaowutech.cn/api/third-party/v1/api/file/file-upload",
                                 headers=header, files=files)
        print(response, response.content)


if __name__ == '__main__':
    fileLoad().fileFunction()
    print(fileLoad().imagePath)
