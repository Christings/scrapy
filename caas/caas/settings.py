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

FEED_URI = u'file:///d://workspace/scrapy/caas/comtrade_catalog.csv'
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
    "ASP.NET_SessionId": "wejbbo45qejcv3vu3pydndy1",
    "hadReadMeE": "Q6o2adA7vxvchXbHpuQ++w==",
    "comtrade3": "E1EF2911DA1D00D7388867E1D716443AD525D2098E5AFC99455E00D0BD52883490B6527CE25F65D4DE3F00AE11A8F94015D0B6F5ED08E436BBD2291ECF136700B677AF6C26E9E7E32F171CC3719D19F29C4064841FC44F4AB6073254FBF542557410662A3C9B43A89B7C6AC63B7FAFB121803A3D658BD193F15C89BBA33AF9C5219496323427E5C30B5D6FDB21A65C98B2B29F976B3B6974BE88F7E6B0DBB6F39A95EAC90237BE4554C0EA0D68E789AEC1610FA01DCDE475",
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
