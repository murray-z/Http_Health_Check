# -*- coding: utf-8 -*-


config = {
    "url": "http://localhost:9007",       # http url地址
    "data": {},                           # 接口输入数据
    "method": "post",                     # 输入方法 post/get
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