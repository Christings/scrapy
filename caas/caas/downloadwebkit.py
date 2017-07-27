from selenium import webdriver
import time


class WebkitDownloader(object):
    # 通过selenium打开chrome内核，从而获得网页加载后的源代码。
    def process_request(self, request, spider):
        browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        browser.get("http://www.fao.org/countryprofiles/geographic-and-economic-groups/en/")
        time.sleep(10)
        pagesource = browser.page_source
        browser.close()
        return pagesource
