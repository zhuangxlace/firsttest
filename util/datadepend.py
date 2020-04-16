import sys
from data.get_data import GetData
from base.runmenthod import RunMethod
from jsonpath_rw import parse,jsonpath
sys.path.append("d:/pythonworkspace/interfaceframework")
# from util.operation_json import Operation_json


class Datadepend:
    def __init__(self):
        self.getdata = GetData()
        self.runmethod = RunMethod()
        # self.opejson=Operation_json()

    # 执行具有数据依赖的用例，并返回执行结果
    def rundependcase(self, i):
        # 必须转换为整形
        caseid = int(self.getdata.get_depend_caseid(i))
        res = self.runmethod.run_main(self.getdata.get_requestway(caseid), self.getdata.get_url(caseid),
                                      self.getdata.get_request_data(caseid), self.getdata.get_headers(caseid),
                                      self.getdata.get_cookies(caseid))
        return res.json()

    # 根据返回的执行结果，获取依赖case想对应的数据
    def getdata_by_dependcase(self, i):
        run_res = self.rundependcase(i)
        dependfield = self.getdata.get_depend_field(i)
        # 返回的是列表，取列表第一个元素
        res = [match.value for match in parse(dependfield).find(run_res)][0]
        return res

    # 将依赖case的数据写入自身需要修改的字段内,然后运行case
    def writedependdata_in_owefield(self, i):
        dependdata = self.getdata_by_dependcase(i)
        requeutdata = self.getdata.get_request_data(i)
        # print(requeutdata)
        owefield = self.getdata.get_owe_field(i)
        requeutdata[owefield] = dependdata
        # run_main(self,method,url,data=None,header=None)
        return requeutdata


if __name__ == "__main__":
    a = Datadepend()
    res = a.getdata_by_dependcase(10)
    print(res)
    '''
    a = Datadepend()
    res = a.writedependdata_in_owefield(10)
    print(res)
    print(type(res))
    # a = "city"
    '''
    '''
    s = jsonpath.jsonpath(res,'$..city')
    print(type(s[0]))
    print(type(s))
    
    import jsonpath
    s = jsonpath.jsonpath(dic,'$..name')   #不管有多少层，写两个.都能取到
    print(s)
    '''
    # print(match.value for match in res.find("city"))