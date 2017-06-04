#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []
        self.datalist = [] ###加的 list


    def collect_data(self, data, datalist):
        if data is None:
            return
        if datalist is None:###加的 list
            return
        self.datas.append(data)
        self.datalist.append(datalist)###加的 list

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        if self.datalist is None:###加的 list
            return
        for data in self.datalist:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data)
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
