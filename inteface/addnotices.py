from common.globalvar import getHeader, get_KeyValue
from inteface.base import Base
from inteface.loginparam import Login


class Notices(Base):

    def __init__(self, method="POST", url="/api/server/v1/admin/dispatch/build/added"):
        super().__init__()
        self.method = method
        self.url = url

    def addNoticeParam(self):
        json = {
            "customerName": "大雄客户",
            "contractCode": "TJ022X-202112-4671KH",
            "contractName": "机械设备租赁合同",
            "customerOrderCode": "TJ022X-202112-4671KH-001",
            "projectId": "1465874223856308226",
            "customerId": "1465884407236349954",
            "contractId": "1472840793983766530",
            "customerOrderId": "1472840793996349441",
            "projectName": "大雄测试工程",
            "siteLeader": "调度",
            "siteLeaderPhone": "17878900987",
            "address": "新疆维吾尔自治区可克达拉市安康西路与昆仑山南路交叉口西北方向120米 128地址",
            "provinceCode": "110000",
            "cityCode": "110100",
            "districtCode": "110101",
            "provinceName": "北京市",
            "cityName": "北京市",
            "districtName": "东城区",
            "devices": [
                {
                    "buildNoticeId": None,
                    "bulidNoticeDeviceId": None,
                    "buildNoticeDeviceAssignId": None,
                    "customerOrderDeviceId": "1472840794021515265",
                    "deviceCategoryId": "1465867653999185922",
                    "deviceCategoryName": "履带式挖掘机",
                    "brandId": "1465867068998635521",
                    "brandName": "大雄",
                    "deviceType": "kl343",
                    "leasingModel": "DRY_LEASE",
                    "leasingModelDesc": "干租",
                    "valuationWay": "MONTH",
                    "rentUnit": None,
                    "valuationWayDesc": "月租",
                    "orderNum": 5,
                    "enterTime": "2021-12-27 16:35:13",
                    "waitNum": 5,
                    "num": None,
                    "dispatchedNum": None,
                    "waitDispatchNum": None,
                    "params": [
                        {
                            "buildDeviceId": None,
                            "deviceCategoryId": "1465867653999185922",
                            "deviceCategoryName": "履带式挖掘机",
                            "deviceParamId": "1465867654036934658",
                            "deviceParamName": "臂展",
                            "deviceParamValue": 10,
                            "unitId": "1465867360641175554",
                            "unitName": "米"
                        }
                    ],
                    "currDispatchDeviceNum": 1,
                    "assignsLength": 1,
                    "id": "1472840794021515265",
                    "assigns": [
                        {
                            "num": 1,
                            "enterTime": "2021-12-27 16:35:13"
                        }
                    ],
                    "waitWorkDeviceNum": 1
                }
            ]
        }
        return json

    def postAddNotice(self, token, num):
        response = self.req.request(self.url, self.method, json=self.addNoticeParam(), headers=super(Notices, self).getHeader(token, num))
        noticeId = get_KeyValue(response.json(), "data")
        return noticeId


if __name__ == '__main__':
    Notices().postAddNotice()
