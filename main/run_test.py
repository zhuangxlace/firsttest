import sys
sys.path.append("e:/py/pythonworkspace/interfaceframework")
from base.runmenthod import RunMethod
from data.get_data import GetData
from util.operation_excel import OperationExcel
import json
from data.data_config import get_result, get_final_result
from util.datadepend import Datadepend
from util.send_email import SendEmail


class RunTest:
    def __init__(self):
        self.runmain = RunMethod()
        self.data = GetData()
        self.excel = OperationExcel()
        self.data_depend = Datadepend()
        self.send_mail = SendEmail()
        # self.dataconfig=data_config()

    def fun(self):
        rowcount = self.data.get_case_lines()
        countsuccess = 0  # 统计成功的用例数
        countnotrun = 0  # 统计失败的用例数
        for i in range(1, rowcount):
            if self.data.get_is_run(i):
                if self.data.get_is_depend(i) == "无":
                    res = self.runmain.run_main(self.data.get_requestway(i), self.data.get_url(i),
                                                self.data.get_request_data(i), self.data.get_headers(i),
                                                self.data.get_cookies(i))
                    expect_result = self.data.get_expect_value(i)
                    # print(expect_result)
                    # real_result=json.dumps(res.json(),ensure_ascii=False,indent=2)
                    real_result = res.text
                    # 为str类型 无需用上一行的json.dumps方法 上面的方法会导致逗号后面有空格
                    if i == 11:
                        print(real_result)
                    self.excel.writetestresultintoecxel(i, get_result(), real_result)
                    if expect_result in real_result:
                        self.excel.writetestresultintoecxel(i, get_final_result(), "通过")
                        countsuccess = countsuccess+1
                    else:
                        self.excel.writetestresultintoecxel(i, get_final_result(), "失败")
                    # print(json.dumps(res,ensure_ascii=False, indent=4))
                else:
                    request_data = self.data_depend.writedependdata_in_owefield(i)
                    res = self.runmain.run_main(self.data.get_requestway(i), self.data.get_url(i),
                                                request_data,
                                                self.data.get_headers(i), self.data.get_cookies(i))
                    # print(res.text)
                    expect_result = self.data.get_expect_value(i)
                    # real_result=(json.loads(res.text))["resultcode"]
                    real_result = res.text
                    # print(real_result)
                    self.excel.writetestresultintoecxel(i, get_result(), real_result)
                    if expect_result in real_result:
                        self.excel.writetestresultintoecxel(i, get_final_result(), "通过")
                        countsuccess = countsuccess+1
                    else:
                        self.excel.writetestresultintoecxel(i, get_final_result(), "失败")
            else:
                countnotrun = countnotrun+1
        q = rowcount-1
        w = countsuccess
        e = countnotrun
        r = rowcount-countsuccess-1-countnotrun
        t = "%.2f%%" % ((countsuccess/(rowcount-1-e))*100)
        context = "总用例个数为%d,成功个数为%d,未执行个数为%d,失败个数为%d,成功率为%s。" % (q, w, e, r, t)+"具体情况如附件所示!"
        res = self.send_mail.mail(context)
        print(res)


if __name__ == "__main__":
    a = RunTest()
    a.fun()
    # print(res)
