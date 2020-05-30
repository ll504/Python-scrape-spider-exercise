import requests
from bs4 import BeautifulSoup
import csv
import time

encoding='utf-8'

base_url= 'https://bj.zu.ke.com'

csv_file = with open('地铁十号线.csv', 'w')

t1=time.time()
csv_writer = csv.writer(csv_file, lineterminator="\n")  # lineterminator避免导出数据每行间有空行
csv_writer.writerow(['名称', '链接', '租金', '面积', '户型', '朝向', '层高', '行政区', '地铁站'])


print('\nScraping......')

for page in range(1,101):
    suffix = '/zufang/li651/pg{}rt200600000001/'.format(page)

    url= f'{base_url}{suffix}'

    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68'}

    html=requests.get(url, headers = header).text

    soup=BeautifulSoup(html,features='lxml')


    for house in soup.find_all('div', class_= "content__list--item"):
        house_info = house.find('p', class_= "content__list--item--title twoline")

        name = house_info.text.replace('\n','').replace(' ','')

        link = house_info.a['href']
        zf_link = f'{base_url}{link}'

        price = house.find('span', class_ = "content__list--item-price")
        rent = price.contents[0].text.replace('\n','').replace(' ','')
        # print(name)
        # print(rent)

        # try:
        #     property = house.find('p' , class_ = "content__list--item--des")
        # except Exception as e:
        #     pass

        try:
            area = house.find('p' , class_ = "content__list--item--des").text.split('/')[1].replace(' ','').replace('\n','')
            area = area[0:2]
        except Exception as e:
            area = None
        # print(area)

        try:
            structure = house.find('p' , class_ = "content__list--item--des").text.split('/')[3].replace(' ','').replace('\n','')
        except Exception as e:
            structure = None
        # print(structure)

        try:
            storey = house.find('p' , class_ = "content__list--item--des").text.split('/')[4].replace(' ','').replace('\n','')
        except Exception as e:
            storey = None
        # print(storey)

        try:
            face = house.find('p' , class_ = "content__list--item--des").text.split('/')[2].replace(' ','').replace('\n','')
        except Exception as e:
            face = None
        # print(face)

        location = house.find('p' , class_ = "content__list--item--des").text.split('/')[0].replace(' ','').replace('\n','')
        try:
            district = location.split('-')[0]
            subway = location.split('-')[1]
        except Exception as e:
            district = None
            subway = None

        # print(subway)
        # print(district)
        # print()

        csv_writer.writerow([name,zf_link,rent,area,structure,face,storey,district,subway])

csv_file.close()
print('\nFinished!')
print('Total time used: %.1f s' % (time.time()-t1, ))