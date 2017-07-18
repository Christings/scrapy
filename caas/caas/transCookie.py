# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = "ASP.NET_SessionId=pwjqca55ni5fn33luylgpemc; hadReadMeE=Q6o2adA7vxvchXbHpuQ++w==; comtrade3=1F004B5383FCE395C8A22E0A7DF7116F2D578A53CCC0D6C371F812405351AFB799E3A708C6029D8DF1E711EC2EC51E351C35F3FE2669537F277D231CDE313A2F8E0C59C08C5D9B444CE559BAB733EE2DFD9DC5BE8933049DE6B8CD2D7F6A2C212FF69D0979E40A3F74028B5F6B6D2788C9A478CEF1E5C3EC07FC23E1E2571B5B2D2E4FECFBA7B2FD8EEC79778B938480B3C72FEF9EDA5A9B9621C594E45EED9595BAA6B024EAF1AD7FC50C0C32ACCB4FB4E894902C262B88; _ga=GA1.2.1958648564.1500279176; _gid=GA1.2.88170259.1500279176; _gat=1"
    trans = transCookie(cookie)
    print(trans.stringToDict())
