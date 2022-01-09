import requests


data = {
    "acceptanceInstructions":None,
    "address":"新疆维吾尔自治区可克达拉市安康西路与昆仑山南路交叉口西北方向120米 128地址",
    "attachmentList":[
        {
            "fileId":"1476850323753816066",
            "fileName":"图片1.png",
            "url":"http://g-server-private-1304519326.cos.ap-shanghai.myqcloud.com/file/test/%E5%9B%BE%E7%89%871%2824%29.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDVqvkJbdOs40f3A0atue7JErEJ7fvvf8J%26q-sign-time%3D1640943530%3B1640945330%26q-key-time%3D1640943530%3B1640945330%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Da103122fb143173d7a894350e583181af58759da",
            "status":"done",
            "uid":"rc-upload-1640935949089-10",
            "name":"图片1.png",
            "extension":"png"
        }
    ],
    "cityCode":"110100",
    "cityName":"北京市",
    "confirmTime":"2021-12-22 17:38:32",
    "districtCode":"110101",
    "districtName":"东城区",
    "provinceCode":"110000",
    "provinceName":"北京市",
    "captcha":"902328",
    "id":"1476849639648878594"
}
header = {
    "content-type": "application/json",
    "Authorization":"bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDEzOTMwMDIsInVzZXJfbmFtZSI6ImFkbWluIiwidXNlckRldGFpbCI6eyJ1c2VybmFtZSI6ImFkbWluIiwicmVhbE5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjpudWxsLCJ1c2VySWQiOjEsImxhbmd1YWdlIjpudWxsLCJhdXRob3JpdGllcyI6bnVsbCwiZGF0YU1hcCI6eyJ1c2VybmFtZSI6ImFkbWluIiwibW9iaWxlIjoiMTg4ODg4ODg4ODgiLCJyb2xlcyI6IlNVUEVSX0FETUlOIn0sImVuYWJsZWQiOnRydWUsImFjY291bnROb25FeHBpcmVkIjp0cnVlLCJhY2NvdW50Tm9uTG9ja2VkIjp0cnVlLCJjcmVkZW50aWFsc05vbkV4cGlyZWQiOnRydWV9LCJqdGkiOiJmM2Q4ODQzNS00NzRlLTQ1YzUtYmY0Ny0zYmZlYjIxYzA5ZTEiLCJjbGllbnRfaWQiOiJnLWZyb250Iiwic2NvcGUiOlsib3BlbmlkIl19.SxVR_oIXx9Bn06M2OaH71tVgfqBS71e09jWcD3zF5pmTw2TG5EBYvX4a2BUX5Me8_TvSGIcD9c5ggvD-4NaqY1O6dYcpARFr5aQrTXp3iNOaubRCRjUnBWbI2czjLA-ws_UGR143BGk_VRNuzZ53M5MnwUbeDT1JzTX_yFFI5ls"
}

response = requests.put(url="http://qaadminweb.yaowutech.cn/api/server/v1/admin/enter/confirm", json=data, headers=header)
print(response.request.headers)
print(response.request.body)
print(response.json())