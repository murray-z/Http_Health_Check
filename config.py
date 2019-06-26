# -*- coding: utf-8 -*-


import requests
import json


config = {
    "subject": "HEALTH CHECK REPORT",     # 邮件标题
    "from_email": "xxxxxxxxxx@qq.com",    # 发件邮箱
    "mail_host": "smtp.qq.com",           # 服务器，这里以qq为例
    "mail_port": 25,                      # 服务器端口
    "password": "xxxxxxxxxxx",            # 授权码，密码
    "to_email": ["xxxxxx@qq.com"],        # 收件邮箱
    "check_Intervals": 3600,              # 检查时间间隔，单位：秒
    "check_total": 100,                   # 每次检查调用接口次数
    "error_num": 5,                       # 预警阈值，即总检查次数超过error_num发送邮件
    "server_name": "my test server"       # 服务名称
}


def get_response_code():
    """获取接口状态码，需要用户根据自己接口实现，
       这里仅是一个示例
    """
    response = requests.post(url="http://localhost:9007", data=json.dumps({}))
    return response.status_code