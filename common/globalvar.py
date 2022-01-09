import datetime

import jsonpath

BASE_URL = "https://qaadminweb.yaowutech.cn"

HEAD = ["application/x-www-form-urlencoded", "multipart/form-data", "application/json", "text/xml", "image/jpeg"]


def geturl(url):
    return BASE_URL + url


def headers(type, i=None, token=None):
    if type == 0:
        return {"content-type": HEAD[i]}
    elif type == 2:
        return {"Authorization": "bearer " + token}
    else:
        return {"content-type": HEAD[i], "Authorization": "bearer " + token}


def timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def get_KeyValue(data, keyword, i=0):
    """
    通过关键字从接口返回值中获取需要的字段值
    :param i:
    :param data:
    :param keyword:
    :return:
    """
    return jsonpath.jsonpath(data, f"$..{keyword}")[i]