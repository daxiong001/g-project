from common.globalvar import get_KeyValue
from inteface.base import Base
from common.sendmsg import dict

class AddDevicesDetail(Base):

    def __init__(self, method="POST", url="/api/server/v1/admin/device/device-detail/add"):
        super().__init__()
        self.method = method
        self.url = url

    def deviceDetailParam(self):
        json = {
            "deviceNo": super().rand(),
            "brandId": "1465867068998635521",
            "deviceType": "kl343",
            "madeTime": "2021-12-27",
            "state": "NO_RENT",
            "deviceId": "1470309229115703297",
            "brand": "大雄"
        }
        return json

    def postAddDevicesDetail(self, token, num):
        response = self.req.request(self.url, self.method, json=self.deviceDetailParam(), headers=super(AddDevicesDetail, self).getHeader(token, num))
        detailId = get_KeyValue(response.json(), "data")
        if detailId is not None:
            dict.append("> 添加设备明细接口：<font color=\"info\">通过</font>\n")
        else:
            dict.append("> 添加设备明细接口：<font color=\"comment\">失败</font>\n")
        return detailId

if __name__ == '__main__':
    AddDevicesDetail().postAddDevicesDetail()