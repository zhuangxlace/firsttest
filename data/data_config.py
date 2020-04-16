# import sys
# sys.path.append("d:/pythonworkspace/interfaceframework")


class GlobalVar:
    # case_id
    # def __init__():
    id = "0"
    data = "1"
    url = "2"
    run = "3"
    request_way = "4"
    headers = "5"
    cookies = "6"
    depend = "7"
    expect = "8"
    dependcaseid = "9"
    dependfield = "10"
    owefield = "11"
    result = "12"
    finalres = "13"


def get_id():  # 获取caseid
    return int(GlobalVar.id)


def get_data():  # 获取请求数据
    return int(GlobalVar.data)


def get_url():  # 获取接口地址
    return int(GlobalVar.url)


def get_run():  # 获取是否执行
    return int(GlobalVar.run)


def get_request_way():  # 获取请求类型
    return int(GlobalVar.request_way)


def get_headers():  # 获取header
    return int(GlobalVar.headers)


def get_cookies():
    return int(GlobalVar.cookies)


'''
def get_header_value():  # 获取header的值
    header = {
        "zxl": "nb",
        "xc": "sb"
    }
'''


def get_depend():  # 获取是否具有数据依赖
    return int(GlobalVar.depend)


def get_expect():  # 获取预期结果
    return int(GlobalVar.expect)


def get_dependcaseid():  # 获取依赖的caseid
    return int(GlobalVar.dependcaseid)


def get_dependfield():  # 获取依赖的字段
    return int(GlobalVar.dependfield)


def get_owefield():  # 获取自身被依赖的字段
    return int(GlobalVar.owefield)


def get_result():  # 获取返回结果
    return int(GlobalVar.result)


def get_final_result():  #获取最终执行结果
    return int(GlobalVar.finalres)


if __name__ == "__main__":
    print(get_data())
    print(type(get_data()))

