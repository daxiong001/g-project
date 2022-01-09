from common.sendmsg import send_msg
from inteface.adddevicesdetail import AddDevicesDetail
from inteface.addnotices import Notices
from inteface.addtenantorder import AddTenantOrder
from inteface.enterconfirm import EnterConfirm
from inteface.fileload import FileLoad
from inteface.loginparam import Login
from inteface.tenantdispatchconfim import TenantDispatchConfirm

if __name__ == '__main__':

    notice_Obj = Notices()
    order_Obj = AddTenantOrder()
    fileObj = FileLoad()
    enter_Obj = EnterConfirm()
    login = Login().login_response()
    noticesId = notice_Obj.postAddNotice(login, 1)
    assignId = order_Obj.queryList(noticesId)[1]
    order_Obj.postTenantDispatch(login, 1, noticesId)
    dispatch_Obj = TenantDispatchConfirm()
    devices_Obj = AddDevicesDetail()
    dispatch_Obj.postTenantDispatchConfirm(login, 1, dispatch_Obj.queryList(noticesId, assignId)[0], dispatch_Obj.queryList(noticesId, assignId)[1],
                                devices_Obj.postAddDevicesDetail(login, 1))
    fileResponse = fileObj.postFile(login, 2)

    enter_Obj.postEnterConfirm(fileResponse[0], (fileResponse[1]), noticesId, login, 1)
    send_msg()