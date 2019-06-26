# Http Health Check
> 监测http服务是否运行正常，当监测到异常，向用户发邮件！

# 目录说明
- config.py  参数配置文件
- http_health_check.py  主函数
- test_http.py   一个简单的http服务 

# 使用

- 配置服务
    - 在config.py中的config中配置邮件及检查参数
    - 在config.py中的get_response_code中实现自己调用接口函数

- 启动http服务
```python
python test_http.py
```

- 启动监测服务
```python
python http_health_check.py
```

# 注意事项
- 采用第三方邮箱发送邮件需要开启SMTP
