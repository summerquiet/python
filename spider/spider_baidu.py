# _*_ coding: utf-8 _*_
'''
https://zhuanlan.zhihu.com/p/77560712

'''

# 导入urllib库的urlopen函数
from urllib.request import urlopen

# 发出请求，获取html
html = urlopen("http://www.baidu.com/")
# 获取的html内容是字节，将其转化为字符串
html_text = bytes.decode(html.read())
# 打印html内容
print(html_text)
