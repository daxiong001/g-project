from common.sendmsg import dict
from inteface.adddevicesdetail import AddDevicesDetail
from inteface.addnotices import Notices
from inteface.addtenantorder import AddTenantOrder
from inteface.base import Base
from inteface.fileload import FileLoad
from inteface.loginparam import Login
from inteface.tenantdispatchconfim import TenantDispatchConfirm
from tables.g_server_models import BEnterInfo


class EnterConfirm(Base):

    def __init__(self, method="PUT", url="/api/server/v1/admin/enter/confirm"):
        super().__init__()
        self.method = method
        self.url = url

    def confirmParam(self, fileId, fileUrl, enterId, captcha):
        data = {
            "acceptanceInstructions": None,
            "address": "新疆维吾尔自治区可克达拉市安康西路与昆仑山南路交叉口西北方向120米 128地址",
            "attachmentList": [
                {
                    "fileId": fileId,
                    "fileName": "sc.png",
                    "url": fileUrl,
                    "status": "done",
                    "uid": "rc-upload-1640935949089-10",
                    "name": "sc.png",
                    "extension": "png"
                }
            ],
            "cityCode": "110100",
            "cityName": "北京市",
            "confirmTime": "2021-12-22 17:38:32",
            "districtCode": "110101",
            "districtName": "东城区",
            "provinceCode": "110000",
            "provinceName": "北京市",
            "captcha": captcha,
            "id": enterId
        }
        return data

    def postEnterConfirm(self, fileId, fileUrl, noticeId, token, num):
        enterObj = super().getConn().query(BEnterInfo).filter_by(notice_id=noticeId).first()
        enterId = enterObj.id
        captcha = enterObj.captcha
        response = self.req.request(url=self.url, method=self.method,
                                    headers=super(EnterConfirm, self).getHeader(token, num),
                                    json=self.confirmParam(fileId, fileUrl, enterId, captcha))
        if response.content is not None:
            dict.append("> 确认进场接口：<font color=\"info\">通过</font>\n")
        else:
            dict.append("> 确认进场接口：<font color=\"comment\">失败</font>\n")

if __name__ == '__main__':
    a = Notices()
    b = AddTenantOrder()
    c = Login().login_response()
    p = FileLoad()
    noticesId = a.postAddNotice(c, 1)
    print(noticesId)
    assignId = b.queryList(noticesId)[1]
    b.postTenantDispatch(c, 1, noticesId)
    print(assignId)
    s = TenantDispatchConfirm()
    g = AddDevicesDetail()
    s.postTenantDispatchConfirm(c, 1, s.queryList(noticesId, assignId)[0], s.queryList(noticesId, assignId)[1],
                                g.postAddDevicesDetail(c, 1))
    file = p.fileFunction(c, 2)
    obj = EnterConfirm()
    obj.postEnterConfirm(file[0], file[1], noticesId, c, 1)
