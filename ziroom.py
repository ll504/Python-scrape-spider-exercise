import requests
from bs4 import BeautifulSoup
import csv
import time
import re



base_url = 'http://www.ziroom.com'

header={'User-Agent':your user agent}

t1 = time.time()

csv_file = open('自如-整租两居-金台路-十里堡-青年路.csv', 'w')

csv_writer = csv.writer(csv_file, lineterminator="\n")  # lineterminator避免导出数据每行间有空行
csv_writer.writerow(['名称', '朝向', '链接', '面积', '楼层', '距离地铁站距离', '地铁站'])

print('\n爷开始爬了！...')

# http://www.ziroom.com/z/z2-s100008-t100046%7C100045%7C100047-u14-p1/?sort=2

for page in range(1,51):
    suffix = '/z/z2-s100008-t100046%7C100045%7C100047-u14-p{}/?sort=2'.format(page)
    url = f'{base_url}{suffix}'

    html = requests.get(url, headers=header).text
    soup = BeautifulSoup(html, features='lxml')

    print('正在爬取第%.f页数据'% page)

    for house in soup.find_all('div', class_ = 'item'):
        try:
            name = house.find('div', class_ = 'info-box').h5.text
        except Exception as e:
            name = None
        # print (name)

        try:
            face = house.find('div', class_ = 'info-box').h5.text.split('-')[-1]
        except Exception as e:
            face = None
        # print(face)

        try:
            link = house.find('div', class_ = 'info-box').a['href']
        except Exception as e:
            link = None
        # print (link)

        try:
            area = house.find('div', class_ = 'desc').text.split(' ')[0].replace('\n','')
            area = area[:-1]
        except Exception as e:
            area = None
        # print(area)

        try:
            storey = house.find('div', class_ = 'desc').text.split(' ')[2].replace('\n','').replace('\t','')
        except Exception as e:
            storey = None
        # print(storey)

        try:
            location = house.find('div', class_ = 'desc').text.split('\t')[-3].replace(' ','')
        except Exception as e:
            location = None

        try:
            distance = location.split('约')[-1]
        except Exception as e:
            distance = None
        # print(distance)

        try:
            subway = location.split('距')[1].split('站')[0]
        except Exception as e:
            subway = None
        # print(subway)
        # print()

        csv_writer.writerow([name,face,link,area,storey,distance,subway])

csv_file.close()

print('\n爬完了!')
print('总耗时: %.2f s' % (time.time() - t1,))
