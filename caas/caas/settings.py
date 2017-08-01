# -*- coding: utf-8 -*-

# Scrapy settings for caas project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'caas'

SPIDER_MODULES = ['caas.spiders']
NEWSPIDER_MODULE = 'caas.spiders'

# FEED_URI = u'file:///d://workspace/scrapy/caas/fao.csv'
# FEED_FORMAT = 'CSV'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'caas (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# COOKIES = {
#     "ASP.NET_SessionId": "pwjqca55ni5fn33luylgpemc",
#     "hadReadMeE": "Q6o2adA7vxvchXbHpuQ++w==",
#     "comtrade3": "EAEEBB0DEE5544FED1E6584E72C80DFAB1A080DB8E97EBDEE40A84C45FC8DD9C2B738E78EFC86FE3F61AA9C2C510ECDBC98F60479F58304073335A6B11F10E442EAAB1D9B71CDEEA651892580B5ED7EA93570009A93C25A5",
#     "_ga": "GA1.2.1958648564.1500279176", "_gid": "GA1.2.88170259.1500279176",
#     "_gat": "1"
#
# }

COOKIES = {
    "ASP.NET_SessionId": "imr5ebemxtezrparboig1uyq",
    "hadReadMeE": "Q6o2adA7vxvchXbHpuQ++w==",
    "comtrade3": "27BB138B988C4399D3E0348989B3CBD6369B7739F797FC316295649C85DD117105428F0D0EC2F99F806B949B7DDB2C572483C2B8C18AD5EDDF46EFEC6F36686204C14F25D95E629802FA487A6CFCF60FD029B8D6A7F0CB93",
    "_ga": "GA1.2.1958648564.1500279176",
    "_gid": "GA1.2.88170259.1500279176",
    "_gat": "1"
}

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'caas.middlewares.CaasSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# 下载中间件
DOWNLOADER_MIDDLEWARES = {
   # 'caas.middlewares.MyCustomDownloaderMiddleware': 543,
   'caas.downloadwebkit.WebkitDownloader': 543,   # 在FAO中使用selenium添加的下载浏览器网页源码中间件
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,#禁止内置的中间件

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'caas.pipelines.ComtradeCatalogPipeline': 300,
    'caas.mysqlpipelines.pipelines.WorldBankPipeline': 1,
    'caas.mysqlpipelines.pipelines.ComtradeCountryListPipeline': 1,
    # 'caas.pipelines.CaasPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# scrapy会缓存Requests，当再次请求时，如果存在缓存文档则返回缓存文档，而不是去网站请求，这样既加快了本地调试速度，也减轻了网站的压力。
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MySql数据库的配置信息
MYSQL_HOSTS = 'localhost'
MYSQL_DBNAME = 'caas'       # 数据库名字
MYSQL_USER = 'root'         # 数据库账号
MYSQL_PASSWORD = '421498'     # 数据库密码
MYSQL_PORT = '3306'         # 数据库端口，在dbHelper中使用