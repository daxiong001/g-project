from common.globalvar import get_KeyValue
from inteface.base import Base


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

    def postAddDevicesDetail(self):
        response = self.req.request(self.url, self.method, json=self.deviceDetailParam(), headers=super(AddDevicesDetail, self).getHeader())
        detailId = get_KeyValue(response.json(), "data")
        return detailId

if __name__ == '__main__':
    AddDevicesDetail().postAddDevicesDetail()