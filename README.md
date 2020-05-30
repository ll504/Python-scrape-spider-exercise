# Python-scrape-spider-exercise

Some scraping exercises by using BeautifulSoup &amp; Selenium 

几个基于BeautifulSoup和Selenium的爬虫

Based on Python 3.7

# Background

商科背景，纯属写着玩。一开始是觉得想租房一页页去翻很麻烦，直接导出成一个csv看会不会省事点。

然后选了我爱我家，贝壳找房和自如三家的网址去爬取他们在北京的房源。

以及处于个人兴趣写了个爬东方财富的‘上会企业’页面的爬虫，这里面的数据是在一个基于JAVAscript的动态表格里，希望能给各位提供一些思路

第一次用Github, 不是很会用，希望对以后想自学爬虫的人有一些帮助



# 我爱我家
我爱我家的网页源代码可以说是对我这个新手非常友好了，个人认为十分标准，通过request来实现翻页，再爬取每一页的数据并保存到excel里。
    
其中，值得注意的是需要用一个header来伪装爬虫以应对网站的反爬虫措施。

# 贝壳找房
思路同我爱我家差不多，比较简单

# 自如
同上

# 东方财富
通过selenium模拟浏览器来实现翻页

    
    
