import os
import json as complexjson
import requests

from common.globalvar import get_KeyValue
from inteface.base import Base
from inteface.loginparam import Login
from common.sendmsg import dict


class FileLoad(Base):
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    imagePath = os.path.join(rootPath, "resources/sc.png")

    def __init__(self, method="POST", url="/api/third-party/v1/api/file/file-upload"):
        super().__init__()
        self.method = method
        self.url = url

    def fileParam(self):
        files = {"file": open(r"/Users/daixiongkun/PycharmProjects/g-project/resources/sc.png", "rb")}
        data = {
            "fileName": "sc.png",
            "type": "PRIVATELY"
        }
        return files, data

    def postFile(self, token, num):
        response = requests.post(url="http://qaadminweb.yaowutech.cn/api/third-party/v1/api/file/file-upload",
                                 headers=super().getHeader(token, num), data=self.fileParam()[1], files=self.fileParam()[0])
        fileId = get_KeyValue(response.json(), "id")
        fileUrl = get_KeyValue(response.json(), "url")
        if response.content is not None:
            dict.append("> 图片上传接口：<font color=\"info\">通过</font>\n")
        else:
            dict.append("> 图片上传接口：<font color=\"comment\">失败</font>\n")
        return fileId, fileUrl

    def fileFunction(self, token, num):
        response = self.req.request(url=self.url, method=self.method, data=self.fileParam()[1], headers=super().getHeader(token, num),
                                    files=self.fileParam()[0])
        fileId = get_KeyValue(response.json(), "id")
        fileUrl = get_KeyValue(response.json(), "url")
        return fileId, fileUrl

if __name__ == '__main__':
    s = Login().login_response()
    FileLoad().fileFunction(token=s, num=2)
    print(FileLoad().fileFunction(token=s, num=2))


