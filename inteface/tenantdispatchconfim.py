from common.sendmsg import dict
from inteface.base import Base
from tables.g_server_models import BBuildDeviceTenantDispatchInfo, BDispatchTenantInfo, BDispatchTenantDevice


class TenantDispatchConfirm(Base):

    def __init__(self, method="POST", url="/api/server/v1/admin/dispatch/tenant-dispatch/confirm-dispatch"):
        super().__init__()
        self.method = method
        self.url = url

    def queryList(self, noticeId, assignId):
        ptDispatchObj = super().getConn().query(BBuildDeviceTenantDispatchInfo).filter_by(build_notice_id=noticeId, build_notice_device_assign_id=assignId).first()
        dispatchTenantId = ptDispatchObj.id
        print(dispatchTenantId)
        tenantDispatchObj = super().getConn().query(BDispatchTenantInfo).filter_by(build_device_tenant_dispatch_id=dispatchTenantId).first()
        tenantDispatchId = tenantDispatchObj.id
        dispatchDevicesObj = super().getConn().query(BDispatchTenantDevice).filter_by(dispatch_tenant_id=tenantDispatchId).first()
        dispatchDevicesId = dispatchDevicesObj.id
        return tenantDispatchId, dispatchDevicesId

    def tenantDispatchParam(self, dispatchTenantId, dispatchTenantDeviceId, deviceDetailId):
        json = {
            "dispatchTenantId": dispatchTenantId,
            "devices": [
                {
                    "dispatchTenantDeviceId": dispatchTenantDeviceId,
                    "details": [
                        {
                            "deviceDetailId": deviceDetailId,
                            "deviceNo": "dfd",
                            "madeTime": "2021-12-22",
                            "workHours": None,
                            "state": "NO_RENT",
                            "stateDesc": "待出租",
                            "pictures": None,
                            "enterTime": "2021-12-27 22:14:07",
                            "masterName": "",
                            "masterPhone": "",
                            "driverPhone": "17576075478",
                            "driverName": "测试",
                            "driverCarNo": "abcde"
                        }
                    ]
                }
            ]
        }
        return json

    def postTenantDispatchConfirm(self, token, num, dispatchTenantId, dispatchTenantDeviceId, deviceDetailId):
        response = self.req.request(self.url, self.method, json=self.tenantDispatchParam(dispatchTenantId, dispatchTenantDeviceId, deviceDetailId), headers=super(TenantDispatchConfirm, self).getHeader(token, num))
        if response.content is not None:
            dict.append("> 商户调度接口：<font color=\"info\">通过</font>\n")
        else:
            dict.append("> 商户接口：<font color=\"comment\">失败</font>\n")


