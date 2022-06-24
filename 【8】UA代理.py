#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @FileName    :【8】UA代理.py
# @Time        :2022/6/10 16:50
# @Author      :Judy Yu

from urllib import request

# 随机获取UA
# pip install fake-useragent


if __name__ == "__main__":
    # 定义变量：URL 与 headers
    url = 'http://httpbin.org/get'  # 向测试网站发送请求
    # 重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'}
    # 1、创建请求对象，包装ua信息
    req = request.Request(url=url, headers=headers)
    # 2、发送请求，获取响应对象
    res = request.urlopen(req)
    # 3、提取响应内容
    html = res.read().decode('utf-8')
    print(html)
