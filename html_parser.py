#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
#ISO-8859-1
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data, squares_data = self._get_new_data(page_url, soup)###加的squares_data
        return new_urls, new_data, squares_data ###加的squares_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # find_all('a'  extracting all the URLs found within a page’s <a> tags
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url

        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_= "lemmaWgt-lemmaTitle-title").find("h1")
        print title_node
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        #catgrys = soup.find_all('div','para-title level-2')
#<div class="para-title level-2" label-module="para-title">
#<h2 class="title-text"><span class="title-prefix">Python</span>发展历程</h2>
#<a class="edit-icon j-edit-link" data-edit-dl="1" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
#</div>
        catgrys = soup.find_all('h2','title-text')
        #<h2 class="title-text"><span class="title-prefix">Python</span>发展历程</h2>

        #print catgrys
        squares = []###加的squares_data
        for catgry in catgrys:
            squares.append(catgry.get_text()[6:]) #[]为什么要在这里写死，PythonXXXX
        for i in squares:
            print i
        return res_data, squares###加的squares_data








#nothing
