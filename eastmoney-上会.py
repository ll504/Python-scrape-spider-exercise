import csv
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.simplefilter("ignore")



print('\nLoading...')

t1 = time.time()

url = 'http://data.eastmoney.com/xg/gh/default.html'

print('\nHeadless Firefox Initializing...')
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options, executable_path=r'C:\geckodriver.exe')

print('\nScraping...')

csv_file = open('东方财富上会数据111.csv', 'w')

csv_writer = csv.writer(csv_file, lineterminator="\n")  # lineterminator避免导出数据每行间有空行
csv_writer.writerow(['序号', '名称', '申报日期', '上会日期', '状态', '发行数量', '申购日期', '上市地点', '承销商'])

i = 0 # page number parameter

driver.get(url)

while i < 56:

    i += 1

    print('\n\tSraping Page %.f...'% i)


    index = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[1]")

    name = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[2]")

    sort = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[3]")

    announce = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[4]")

    meeting = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[5]")

    status = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[6]")

    try:
        purchase_date = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[7]")

    except Exception as e:

        purchase_date = None

    number = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[8]")

    stockexchange = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[9]")

    underwritter = driver.find_elements_by_xpath("//div[@class='content']/table/tbody/tr/td[10]")

    j = 0
    #
    while j < len(name):
        # print(index[j].text)
        # print(name[j].text)
        # print(announce[j].text)
        # print(meeting[j].text)
        # print(status[j].text)
        # print(purchase_date[j].text)
        # print(number[j].text)
        # print(stockexchange[j].text)
        # print(underwritter[j].text)

        csv_writer.writerow([index[j].text,
                             name[j].text,
                             announce[j].text,
                             meeting[j].text,
                             status[j].text,
                             number[j].text,
                             purchase_date[j].text,
                             stockexchange[j].text,
                             underwritter[j].text])
        j += 1



    WebDriverWait(driver, 3).until_not(EC.visibility_of_element_located((By.XPATH, "//div[@class='intellcont-qipao']")))

    element = driver.find_element_by_xpath("//div[@class='miniPageNav']/b[3]")
    # driver.execute_script("arguments[0].style.visibility='hidden'", element)
    element.click()

    time.sleep(2)  # 等待下一页数据刷出来




driver.quit()

print('\nFinished!')

csv_file.close()

t2 = time.time()-t1
print(t2)



