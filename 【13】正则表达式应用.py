#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @FileName    :【13】正则表达式应用.py
# @Time        :2022/6/24 14:40
# @Author      :Judy Yu
import re

regex = re.compile(pattern, flags=0) # pattern - 正则表达式的对象；flags - 代表功能标志位，扩展正则表达式的匹配
re.findall(pattern, string, flags=0) # pattern - 正则表达式对象；string - 目标字符串； flags - 代表功能标志位，扩展正则表达式的匹配
regex.findall(string, pos, endpos) # string - 目标字符串；pos - 截取目标字符串的开始匹配位置；endpos - 截取目标字符串的结束匹配位置
if __name__ == "__main__":
    run_code = 0
