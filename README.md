# scrapy-orm

Scrapy sample code using with Orator (ORM).  
https://scrapy.org/  
https://orator-orm.com/  

## Requirements
- Python 3.4+

## Setup

#### setup python environment

```shell
$ git clone https://github.com/Chanmoro/scrapy-orm
$ cd scrapy-orm

# create new virtual env (optional)
$ python -m venv venv
$ . venv/bin/activate

# install dependencies
$ pip install -r requirements.txt
```

#### start up database (mysql)

```shell
$ docker-compose up -d
# mysql container will listen localhost:3306 
```

## Run spider

```shell
$ cd scrapy-orm/crawlers
$ scrapy crawl scraping_hub
```

After crawling, scraped data will be saved into mysql.

```shell
$ mysql -h 127.0.0.1 -P 3306 -D scrapy -u root -pdocker

mysql> select * from pages limit 5;
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------------------------+----------------------------+
| id | url                                                                                           | title                                                            | created_at                 | updated_at                 |
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------------------------+----------------------------+
|  1 | https://blog.scrapinghub.com/gdpr-web-scraping-iiap-europe-data-protection-congress           | Do What is Right Not What is Easy!                               | 2018-12-19 09:17:07.141725 | 2018-12-19 09:17:07.141725 |
|  2 | https://blog.scrapinghub.com/shubber-gettogether-2018                                         | Shubber GetTogether 2018                                         | 2018-12-19 09:17:07.239666 | 2018-12-19 09:17:07.239666 |
|  3 | https://blog.scrapinghub.com/data-quality-assurance-for-enterprise-web-scraping               | Data Quality Assurance for Enterprise Web Scraping               | 2018-12-19 09:17:07.248357 | 2018-12-19 09:17:07.248357 |
|  4 | https://blog.scrapinghub.com/what-i-learned-as-a-google-summer-of-code-student-at-scrapinghub | What I Learned as a Google Summer of Code student at Scrapinghub | 2018-12-19 09:17:07.256107 | 2018-12-19 09:17:07.256107 |
|  5 | https://blog.scrapinghub.com/web-scraping-gdpr-compliance-guide                               | GDPR Compliance For Web Scrapers: The Step-By-Step Guide         | 2018-12-19 09:17:07.263378 | 2018-12-19 09:17:07.263378 |
+----+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------+----------------------------+----------------------------+
5 rows in set (0.00 sec)
```
