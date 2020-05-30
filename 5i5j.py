from bs4 import BeautifulSoup
import csv
import time
import random
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import warnings
warnings.simplefilter("ignore")

print('\nLoading...')
t1 = time.time()


base_url = 'https://bj.5i5j.com'

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

csv_file = open('5i5j-十号线-整租2.csv','w')
csv_writer = csv.writer(csv_file, lineterminator="\n")
csv_writer.writerow(['名称','价格','结构','面积','朝向','楼层','小区','地铁站','距离'])

print('\nStart scraping...')


page = 0  #页数
count1 = 0 #每页房源总数
count2 = 0 #每页房源序号

while page < 100:

    page += 1

    suffix = '/zufang/subway/sl10/n{}/'.format(page)
    website = f'{base_url}{suffix}'
    # website = 'https://bj.5i5j.com/zufang/subway/sl10'

    driver.get(website)

    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')

    print('\n正在爬取第 %.f 页数据......' % (page))

    for house in soup.find_all('div', class_='listCon'):

        name = house.find('h3', class_='listTit').text.replace('\n','')

        count1 += 1

        print("\t\t\n %s.%s"%(count1,name))
                    # time.sleep(0.2)

        price = house.find('p', class_ = 'redC').text.split('\n')[0]
                    # print(price)
                    # time.sleep(0.2)
                        #
        info = house.find('div', class_='listX').text.replace(' ', '').split('·')
                    # print(info)
                    # time.sleep(0.2)

        structure = info[0].replace('\n', '')
                    # # print(structure)
                    # time.sleep(0.2)

        area = info[1].split('平')[0]
                    # # print(area)
                    # time.sleep(0.2)

        face = info[2]
                    # # print(face)
                    # time.sleep(0.2)

        storey = info[3]
                    # # print(storey)
                    # time.sleep(0.2)

        community = info[4].split('\n')[1]
                    # # print(community)
                    # time.sleep(0.2)

        sub_info = info[5].split('\n')[0]
                    # print(sub_info)
        try:
            subway = re.split(r'(\d+)',sub_info)[0].split('铁')[1]

        except Exception as e:

            subway = None

                    # time.sleep(0.2)
        try:
            distance = re.split(r'(\d+)',sub_info)[1]
                    # time.sleep(0.2)
        except Exception as e:

            distance = None

        csv_writer.writerow([name,price,structure,area,face,storey,community,subway,distance])

        count2 += 1

    time.sleep(5)


driver.quit()

print('\nFinished!')

csv_file.close()


print('\n共耗时: %.2f s' % (time.time()-t1,))

time.sleep(0.5)
print('\n共爬取 %.f 组数据' % (count2))
