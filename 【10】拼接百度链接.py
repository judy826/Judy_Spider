#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @FileName    :【10】拼接百度链接.py
# @Time        :2022/6/24 9:14
# @Author      :Judy Yu
from urllib import request, parse


def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    # 此处使用urlencode()进行编码
    params = parse.urlencode({'wd': word})
    full_url = url.format(params)
    return full_url


def request_url(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33'}
    # 1、创建请求对象，包装ua信息
    req = request.Request(url=url, headers=headers)
    # 2、发送请求，获取响应对象
    res = request.urlopen(req)
    # 3、提取响应内容
    html = res.read().decode('utf-8')
    # 保存文件到本地
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == "__main__":
    word = input('请输入想要搜索的内容：')
    url = get_url(word)
    filename = word + '.html'
    request_url(url, filename)
