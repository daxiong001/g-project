from inteface.addnotices import Notices
from inteface.base import Base
from inteface.loginparam import Login
from tables.connect_server import Server
from tables.g_server_models import BBuildNoticeDevice, BBuildNoticeDeviceAssign


class AddTenantOrder(Base):

    def __init__(self, method="POST", url="/api/server/v1/admin/dispatch/build/dispatch-confirm"):
        super().__init__()
        self.method = method
        self.url = url
        self.tenantObj = Server()

    def queryList(self, noticesId):
        listDevices = self.tenantObj.query(BBuildNoticeDevice).filter_by(build_notice_id=noticesId, delete_flag=0).all()
        noticeDeviceAssign = self.tenantObj.query(BBuildNoticeDeviceAssign).filter_by(build_notice_id=noticesId,
                                                                                      delete_flag=0).first()
        array = []
        for i in listDevices:
            array.append(i)
        buildDeviceId = array[0].id
        assignId = noticeDeviceAssign.id
        return buildDeviceId, assignId

    def addParam(self, noticesId, buildDeviceId, buildNoticeDeviceAssignId):
        json = {
            "buildNoticeId": noticesId,
            "devices": [
                {
                    "buildDeviceId": buildDeviceId,
                    "buildNoticeDeviceAssignId": buildNoticeDeviceAssignId,
                    "tenantDispatchInfos": [
                        {
                            "deviceCategoryId": "1465867653999185922",
                            "deviceCategoryName": "履带式挖掘机",
                            "brandId": "1465867068998635521",
                            "brandName": "大雄",
                            "deviceType": "kl343",
                            "buildNoticeDeviceAssignId": buildNoticeDeviceAssignId,
                            "buildNoticeId": noticesId,
                            "customerOrderDeviceId": "1472840794021515265",
                            "tenantContractId": "1472841051530809345",
                            "tenantContractCode": "BJ010X-202112-4672SH",
                            "tenantOrderId": "1472841051568558082",
                            "tenantOrderCode": "BJ010X-202112-4672SH-001",
                            "tenantOrderDeviceId": "1472841051581140993",
                            "tenantOrderValuationId": "1472841051732135937",
                            "tenantName": "大雄自营商机测试",
                            "tenantId": "1443298461983805442",
                            "tenantOrderNum": 3,
                            "dispatchedNum": 2,
                            "num": 1,
                            "remainDispatchNum": 3,
                            "dispatchedTime": None,
                            "valuationWay": "MONTH"
                        }
                    ]
                }
            ]
        }
        return json

    def postTenantDispatch(self, token, num,  noticesId):
        response = self.req.request(self.url, self.method,
                                    json=self.addParam(noticesId, self.queryList(noticesId)[0],
                                                       self.queryList(noticesId)[1]),
                                    headers=super(AddTenantOrder, self).getHeader(token, num))


if __name__ == '__main__':
    s = Notices()
    a = Login().login_response()
    AddTenantOrder().postTenantDispatch(a, s.postAddNotice(a))
