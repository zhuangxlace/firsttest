import json
'''
fp=open("d:/pythonworkspace/interfaceframework/dataconfig/login.json")
data=json.load(fp)
print(data["aa"])
print(data["bb"])
print(data["cc"])
'''


class Operation_json():
    '''
    def __init__(self,id=None):
        if id:
            #self.path=path
            self.id=id
        else:
            #self.path="d:/pythonworkspace/interfaceframsework/dataconfig/login.json"
            self.id="aa"
        #self.aa=self.fun()
    def fun(self):
        fp=open("d:/pythonworkspace/interfaceframework/dataconfig/login.json")
        data=json.load(fp)
        print("11")
        return data[self.id]
        
if __name__=="__main__":
    a=Operationjson()
    x=a.fun()
    print(x)

    '''

    def __init__(self):
        self.data = self.read_json()
    # 读取json文件

    def read_json(self):
        # 写法一
        
        fp = open("e:/py/pythonworkspace/interfaceframework/dataconfig/login.json", encoding='UTF-8')
        data = json.load(fp)  # load():读取文件中json形式的字符串元素转化为Python类型
        fp.close()
        return data
        # 写法二
        # with open("d:/pythonworkspace/interfaceframework/dataconfig/login.json") as fp:
            #data=json.load(fp)
            #return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]


if __name__ == "__main__":
    a = Operation_json()
    x = a.get_data("ff")
    print(x)
    print(type(x))
    