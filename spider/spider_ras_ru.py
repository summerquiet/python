# _*_ coding: utf-8 _*_
'''
http://www.ras.ru/members/personalstaff1724/fullmembers.aspx?ml=0
'''

# 导入urllib库的urlopen函数
from email import contentmanager
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
import re
import xlwt

class ExcelHelper():
    def __init__(self):
        self._book = book = xlwt.Workbook() #创建Excel
        self._sheet = self._book.add_sheet('sheet1') #创建sheet页
        self._row = 0
        self.creat()

    def creat(self):
        title = ['url', 'Name', 'content'] #把表头名称放入list里面

        #循环把表头写入
        col = 0
        for t in title:
            self._sheet.write(self._row, col ,t)
            col += 1

        # 移动到下一行
        self._row += 1

    def close(self):
        self._book.save('dump_ras_ru.xls')

    def write(self, item):
        #循环把内容写入
        '''
        col = 0
        for t in item:
            self._sheet.write(self._row, col ,t)
            col += 1

        # 移动到下一行
        self._row += 1
        '''
        print(item)
        

g_excel_helper = ExcelHelper()

class WriteItem():
    def __init__(self):
        '''
        '''

    def write(self, item):
        # 将目标写入到excel中
        '''
        '''
        g_excel_helper.write(item)


class ItemHtml():
    def __init__(self, url):
        self._url = url
        self._html = None
        self._write_item = WriteItem()

    def dump(self):
        self._html = urlopen(self._url)

        # 用BeautifulSoup解析html
        obj = bf(self._html.read(),'html.parser')

        # 获取title
        title = self.dumpTitle(obj)

        # 获取content
        content = self.dumpContent(obj)

        one_item = [self._url, title, content]
        self._write_item.write(one_item)

    def dumpTitle(self, bf_obj) -> str:
        # 从<div>标签中查找title1
        title = bf_obj.find_all('div', class_='title1')
        title1 = title[0].text
        return title1

    def dumpContent(self, bf_obj) -> str:
        # 从<br>标签中查找
        a_list = bf_obj.find_all('table')
        for a in a_list:
            if a:
                b_list = a.find_all('p')
                for b in b_list:
                    if b:
                        reg = r'<p><br/>.'
                        m = re.search(reg, str(b))
                        if m:
                            print(m.group(0))
                        

class SubLists():
    def __init__(self, list_html):
        '''
        '''
        self._list_html = list_html

    def dumpItem(self, id):
        # 根据id下载内容
        # 创建链接
        url = "http://www.ras.ru/win/db/show_per.asp?P=.%s.ln-ru" % id

        item_html = ItemHtml(url)
        item_html.dump()

    def dumpItems(self, id_list):
        # 下载list中所有内容
        #for id in id_list:
        #    self.dumpItem(id)
        self.dumpItem(id_list[0])

    def dump(self):
        # 用BeautifulSoup解析html
        obj = bf(self._list_html.read(),'html.parser')

        # 从标签<li>里提取地址
        li = obj.find_all('li')

        # 找到所有的id
        id_list = []
        for i in li:
            reg = r'id-\d+'
            m = re.search(reg, str(i))
            if m:
                id = str(m.group())
                id_list.append(id)

        self.dumpItems(id_list)

class MainHtml():
    def __init__(self):
        self._url = "http://www.ras.ru/members/personalstaff1724/fullmembers.aspx?ml="
        self._listCount = 1 #from 0 to 32
        self._html = None

    def dumpList(self, count):
        # 根据list编号下载list
        url = '%s%d' % (self._url, count)
        self._html = urlopen(url)

        # 打印html内容
        #html_text = bytes.decode(self._list_html.read())
        #print(html_text)

        sub_list = SubLists(self._html)
        sub_list.dump()

    def dumpLists(self):
        # 下载所有list
        for i in range(0, self._listCount):
            self.dumpList(i)

    def dumpAll(self):
        #下载所有内容
        self.dumpLists()


def main():
    main_html = MainHtml()
    main_html.dumpAll()
    g_excel_helper.close()

if __name__ == '__main__':
    main()
