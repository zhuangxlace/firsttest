import requests
import json
# json.dumps(r.json(), ensure_ascii=False, indent=4 ) #json格式输出缩进两个字符输出


class RunMethod:
    # @staticmethod
    def post_main(self, url, data, headers, cookies):
        # if header is None:
        if headers != "无":
            if cookies != "无":
                res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
            else:
                res= requests.post(url=url, data=data, headers=headers)
        else:
            if cookies != "无":
                res = requests.post(url=url, data=data, cookies=cookies)
            else:
                res = requests.post(url=url, data=data)
        return res

    # @staticmethod
    def get_main(self, url, data, headers, cookies):
        if headers != "无":
            if cookies != "无":
                res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
            else:
                res = requests.post(url=url, data=data, headers=headers)
        else:
            if cookies != "无":
                res = requests.post(url=url, data=data, cookies=cookies)
            else:
                res = requests.post(url=url, data=data)
        return res
    # 存在问题：get类型接口的data为空且存在header时候，应用此方法有问题？？？

    def run_main(self, method, url, data, headers, cookies):
        if method == "post":
            res = self.post_main(url, data, headers, cookies)
        else:
            res = self.get_main(url, data, headers, cookies)
        return res


if __name__ == '__main__':
    # str类型转json类型用loads
    # json类型转换成str类型用dumps
    a = RunMethod()
    data = {
        "name": "13260906289",
        "password": "abc123666",
        "remember": "false"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "Referfer": "https://accounts.douban.com/passport/login_popup?login_source=anony"
    }
    # res = a.run_main("get", "http://apis.juhe.cn/mobile/get?phone=13906129110&key=72435790ccc226a5e390cfc186782661","aa", "无", "无")
    res = a.run_main("post", "https://accounts.douban.com/j/mobile/login/basic", data, headers, "无")
    # print(res.text)
    print(res.status_code)
    print("返回值res的类型", type(res))
    print(res.text)
    print("res.text的类型", type(res.text))
    print(json.loads(res.text))
    print("json.loads(res.text)的类型", type(json.loads(res.text)))
    print(res.json())
    print("res.json()的类型", type(res.json()))
    print(json.dumps(res.json()))
    print("json.dumps(res.json())的类型", type(json.dumps(res.json())))
    print(res.json()["payload"]["account_info"]["name"])
    print(type(res.json()["payload"]["account_info"]["name"]))