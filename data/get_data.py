# import sys
# sys.path.append("d:/pythonworkspace/interfaceframework")
from util.operation_excel import OperationExcel
# import data_config的方法导入是错误的   同一文件下模块导入必须按照以下这些
from data import data_config
from util.operation_json import Operation_json


class GetData:
    def __init__(self):
        self.opeexcel = OperationExcel()
        self.ope_json = Operation_json()

    # 获取excel行数，也就是case的个数
    def get_case_lines(self):
        return self.opeexcel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        isrun = self.opeexcel.get_cell_value(row, data_config.get_run())
        if isrun == "是":
            flag = True
        else:
            flag = False
        return flag

    # 获取excel的请求参数，并去json文件中找到匹配的参数内容
    def get_request_data(self, row):
        requestdata1 = self.opeexcel.get_cell_value(row, data_config.get_data())
        # print(requestdata1)
        requestdata2 = self.ope_json.get_data(requestdata1)
        # (requestdata2)
        return requestdata2

    # 获取接口地址
    def get_url(self, row):
        return self.opeexcel.get_cell_value(row, data_config.get_url())

    # 获取请求类型
    def get_requestway(self, row):
        requestway = self.opeexcel.get_cell_value(row, data_config.get_request_way())
        return requestway

    # 获取header
    def get_headers(self, row):
        headers = self.opeexcel.get_cell_value(row, data_config.get_headers())
        headerss = self.ope_json.get_data(headers)
        return headerss

    # 获取cookies
    def get_cookies(self, row):
        cookies = self.opeexcel.get_cell_value(row, data_config.get_cookies())
        cookiess = self.ope_json.get_data(cookies)
        return cookiess

    # 获取是否具有数据依赖
    def get_is_depend(self, row):
        is_depend = self.opeexcel.get_cell_value(row, data_config.get_depend())
        return is_depend

    # 获取预期结果
    def get_expect_value(self, row):
        expect = self.opeexcel.get_cell_value(row, data_config.get_expect())
        return expect

    # 取依赖case的id
    def get_depend_caseid(self, row):
        depend_caseid = self.opeexcel.get_cell_value(row, data_config.get_dependcaseid())
        if depend_caseid != None:
            return depend_caseid
        else:
            return None

    # 获取依赖case执行结果中的依赖字段
    def get_depend_field(self, row):
        depend_field = self.opeexcel.get_cell_value(row, data_config.get_dependfield())
        if depend_field != None:
            return depend_field
        else:
            return None

    # 获取case本身被依赖的字段
    def get_owe_field(self, row):
        owe_field = self.opeexcel.get_cell_value(row, data_config.get_owefield())
        if owe_field != None:
            return owe_field
        else:
            return None


if __name__ == "__main__":
    a = GetData()
    res = a.get_headers(1)
    # res=a.get_request_data(3)
    print(res)
