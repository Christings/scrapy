import requests
import json
import redis
import logging
from .settings import REDIS_URL

logger = logging.getLogger(__name__)
# 使用REDIS_URL链接Redis数据库，deconde_response=True这个参数必须要，数据会变成byte形式，完全没法用
reds = redis.Redis.from_url(REDIS_URL, db=2, decode_response=True)
login_url = ""


# 获取Cookie
def get_cookie(account, password):
    s = requests.Session()
    payload = {
        'log': account,
        'pwd': password,
        'rememberme': 'forever',
        'wp-submit': "登录",
        'redirect_to': 'ss',
        'testcookie': '1'
    }
    response = s.post(login_url, data=payload)
    cookies = response.cookies.get_dict()
    logger.warning("获取Cookie成功！（账号为：%s）" % account)
    return json.dumps(cookies)


def init_cookie(red, spidername):
    redkeys = reds.keys()
    for user in redkeys:
        password = reds.get(user)
        if red.get("%s:Cookies:%s--%s" % (spidername, user, password)) is None:
            cookie = get_cookie(user, password)
            red.set("%s:Cooies:%s--%s" % (spidername, user, password), cookie)


