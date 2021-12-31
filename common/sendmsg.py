

import requests

from common.globalvar import timestamp


auto_robat = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3e52cdc9-3113-4336-a9f5-54a0357478cf"

dict = [" ----------接口自动化测试消息通知----------\n" + "项目名称：<font color=\"info\">即服务项目</font>\n" + "时间：<font color=\"comment\">{}</font>\n".format(timestamp())]

def content():
    s = ""
    for i in dict:
        s += i + ""
    return s



def send_msg():
    # json格式化发送的数据信息

    headers = {"Content-Type": "text/plain"}
    send_data = {
        "msgtype": "markdown",  # 消息类型，此时固定为markdown
        "markdown": {
            "content": content()
        }
    }

    res = requests.post(url=auto_robat, headers=headers, json=send_data)





if __name__ == '__main__':
    send_msg()