#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: crawl http://www.mzitu.com/ 网页数据内容
'''
import os
import requests
import bs4
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
SOURCE_URL = 'https://www.mzitu.com/tag/youhuo/'
SAVE_PATH = '/Users/yaoqijun/workspace/cache/meizitu'
MAX_PAGE_INDEX = 202


def download(page_url, save_path):
    res_sub = requests.get(page_url, headers=headers)
    soup_sub = BeautifulSoup(res_sub.text, 'html.parser')
    all_a = soup_sub.find('div', class_='postlist').find_all('a', target='_blank')
    count = 0
    for a in all_a:
        count = count + 1
        if count % 2 == 0:
            print("current inner count is：" + str(count / 2))
            save_path_2 = '%s/%s' % (save_path, count / 2)
            create_file(save_path_2)
            href = a.attrs['href']
            res_sub_1 = requests.get(href, headers=headers)
            soup_sub_1 = BeautifulSoup(res_sub_1.text, 'html.parser')
            try:
                pic_max = soup_sub_1.find('div', class_='pagenavi').find_all('span')[6].text
                for j in range(1, int(pic_max) + 1):
                    href_sub = href + "/" + str(j)
                    res_sub_2 = requests.get(href_sub, headers=headers)
                    soup_sub_2 = BeautifulSoup(res_sub_2.text, "html.parser")
                    img = soup_sub_2.find('div', class_='main-image').find('img')
                    if isinstance(img, bs4.element.Tag):
                        url = img.attrs['src']
                        array = url.split('/')
                        file_name = array[len(array)-1]
                        print file_name
                        headers['Referer'] = href
                        img = requests.get(url, headers=headers)
                        f = open('%s/%s' % (save_path_2, file_name), 'ab')
                        f.write(img.content)
                        f.close()
            except Exception as e:
                print e


def create_file(path):
    if os.path.exists(path) is False:
        os.mkdir(path)
    os.chdir(path)


def main():
    res = requests.get(SOURCE_URL, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_max = soup.find('div', class_='nav-links').find_all('a')[3].text
    for page_index in range(1, int(img_max)+1):
        if page_index > MAX_PAGE_INDEX:
            break
        if page_index == 1:
            page = SOURCE_URL
        else:
            page = SOURCE_URL + 'page/' + str(page_index)
        save_path = '%s/%s' % (SAVE_PATH, str(page_index))
        create_file(save_path)
        download(page, save_path)


if __name__ == '__main__':
    main()
