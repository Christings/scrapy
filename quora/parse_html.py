# _*_ coding:utf8 _*_
import pymysql
import gzip
import json
from datetime import datetime
import re
import os
from lxml import etree

filepath="/home/lab/quora_now"
allDir = os.listdir(filepath)
logfp = open('/home/lab/quora_temp/output.log','w+')
conn = pymysql.connect(host='192.168.0.211',port = 3306,user = 'root',passwd='ctcisgreat',db='quora',charset='UTF8')
cur = conn.cursor()
for filename in allDir:
    filename = os.path.join(filepath,filename)
    print filename
    logfp.write(filename)
    logfp.write('\n')
    f = gzip.open(filename,'r')
    content = f.readlines()
    for line in content:
        line = json.loads(line)
        html= line['html']
        pattern = re.compile('</p>')
        html = pattern.sub('\n</p>',html)
        pattern = re.compile('<br>|<br />')
        html = pattern.sub('\n',html)
        pattern = re.compile('</li>')
        html = pattern.sub('\n</li>',html)
        html = etree.HTML(html)
        answers = html.xpath('//div[@class = "pagedlist_item"]')
        for answer in answers:
            id = answer.xpath('./div/div/div/a/@name') #获取answer的id
            if len(id)>0:
                id = id[0]
            else:
                continue
            id_list = id.split('_')
            if len(id_list) > 1:
                id = int(id_list[1])
            else:
                id = 0
            answerList = answer.xpath('.//*[@class="rendered_qtext"]/text() | .//*[@class="rendered_qtext"]/b//text() | .//*[@class="rendered_qtext"]/blockquote//text() | .//*[@class="rendered_qtext"]/p//text() | .//*[@class="rendered_qtext"]/div//text() | .//*[@class="rendered_qtext"]/span//text() | .//*[@class="rendered_qtext"]/ol//text() | .//*[@class="rendered_qtext"]/li//text() | .//*[@class="rendered_qtext"]/ul//text() ') # 提取answer里正文的规则
            content = ''
            for temp in answerList:
                content = content + temp +u" "
            content = content.encode('utf8')
            now = datetime.now()
            content = pymysql.escape_string(content)
            try:
                cur.execute("update answer set content=%s,update_on=%s where id=%s",(content,now.strftime('%Y-%m-%d %H:%M:%S'),id))
                conn.commit()
            except:
                pass

logfp.write("all have done")
conn.close()
