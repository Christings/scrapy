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

FEED_URI = u'file:///d://workspace/scrapy/caas/catlog_level2.csv'
FEED_FORMAT = 'CSV'

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
    "ASP.NET_SessionId": "rj5gviu21b3iku55zux2cvyd",
    "hadReadMeE": "Q6o2adA7vxvchXbHpuQ++w==",
    "comtrade3": "70EB54ED99875CD846DEA27EF683666CB73E8249F416943ADBAEC578D05E9F5A08C4BCB60331A5C178487980CA2069CD3F07DB90A0909C8408047C69C1AE6DE54AD8D53A489FB8D08B9BE1BA0AECF7A85491D0E2A3FE4F9A",
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
# DOWNLOADER_MIDDLEWARES = {
#    'caas.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'caas.pipelines.ComtradeCatalogPipeline': 300,
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
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
