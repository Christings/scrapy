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

COOKIES = {
    "ASP.NET_SessionId": "pwjqca55ni5fn33luylgpemc",
    "hadReadMeE": "Q6o2adA7vxvchXbHpuQ++w==",
    "comtrade3": "EAEEBB0DEE5544FED1E6584E72C80DFAB1A080DB8E97EBDEE40A84C45FC8DD9C2B738E78EFC86FE3F61AA9C2C510ECDBC98F60479F58304073335A6B11F10E442EAAB1D9B71CDEEA651892580B5ED7EA93570009A93C25A5",
    "_ga": "GA1.2.1958648564.1500279176", "_gid": "GA1.2.88170259.1500279176",
    "_gat": "1"

}

# COOKIES = {
#     "ASP.NET_SessionId": "xbbxtr45yhjjhxmtppegn3f1",
#     "hadReadMeE": "Q6o2adA7vxvchXbHpuQ++w==",
#     "comtrade3": "1F004B5383FCE395C8A22E0A7DF7116F2D578A53CCC0D6C371F812405351AFB799E3A708C6029D8DF1E711EC2EC51E351C35F3FE2669537F277D231CDE313A2F8E0C59C08C5D9B444CE559BAB733EE2DFD9DC5BE8933049DE6B8CD2D7F6A2C212FF69D0979E40A3F74028B5F6B6D2788C9A478CEF1E5C3EC07FC23E1E2571B5B2D2E4FECFBA7B2FD8EEC79778B938480B3C72FEF9EDA5A9B9621C594E45EED9595BAA6B024EAF1AD7FC50C0C32ACCB4FB4E894902C262B88",
#     "_ga": "GA1.2.1958648564.1500279176",
#     "_gid": "GA1.2.88170259.1500279176",
#     "_gat": "1"
# }


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
# ITEM_PIPELINES = {
#    'caas.pipelines.CaasPipeline': 300,
# }

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
