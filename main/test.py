import requests
import re
import json

'''
payload = {"type": "top", "key": "a4c88b8e58bc6f92321190ff2e9b6d9a"}
r2 = requests.post('http://v.juhe.cn/toutiao/index', data=payload)
print(r2.text)
'''

'''
url = "https://accounts.douban.com/j/mobile/login/basic"
data = {
        "name": "13260906289",
        "password": "abc123666",
        "remember": "false"
    }
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "Referfer": "https://accounts.douban.com/passport/login_popup?login_source=anony"
    }
res = requests.post(url, data=data, headers=header)
cookie = requests.utils.dict_from_cookiejar(res.cookies)
print(res.text)
print(cookie)
print(type(cookie))
print(res.cookies)


def crawl_data():
    comment_url = 'https://movie.douban.com/subject/1292052/comments?start=240&limit=20&sort=new_score&status=P'
    # 请求头
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    try:
        r = requests.get(comment_url, headers=headers, cookies={'bid': 'iLKwDq2ThIc', 'dbcl2': '"211552801:QNL/JUE96gc"'})
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        #print(r.text)
    except Exception as e:
        print(e)
        # print('第%d页爬取请求失败' % page)
        return 0
    comments = re.findall(r'<span class="short">(.*)</span>', r.text)
    for a in comments:
        print(a)

crawl_data()
'''
'''
path = "e:/py/pythonworkspace/interfaceframework/dataconfig/cookie.txt"
with open(path, 'r') as f:
    cookies = f.read()
print(cookies)
print(type(cookies))
c = json.loads(cookies)
print(c)
print(type(c))
print("下面")
aa = {'bid': 'hpquXkxmxOA', 'dbcl2': '"211552801:QNL/JUE96gc"'}
print(aa)
print(type(aa))
'''

