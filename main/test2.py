import requests


url = "http://10.78.234.11:8080/aiga3/login"
data = {
    "username": "zhuangxl",
    "password": "Rw0k0Z1queD/fLL2F/FYnw=="
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    "referer": "http://10.78.234.11:8080/aiga3/html/login.html;jsessionid=C6672E56E3B37FA3F5F4980EB6F5F46C"
}
res = requests.post(url, data)
print(res.status_code)
print(res.text)
print(res.json())
print(res.cookies)
a = requests.utils.dict_from_cookiejar(res.cookies)
print(a)
print(type(a))
url2 = "http://10.78.234.11:8080/aiga3/index.html"
r = requests.get(url2, cookies=res.cookies)
print(r.text)
print(r.status_code)