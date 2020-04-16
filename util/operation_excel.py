#-*-encoding:utf-8-*-
import xlrd
from xlutils.copy import copy
#from xlutils.copy import copy
'''
data=xlrd.open_workbook("d:\pythonworkspace\interfaceframework\dataconfig\interface.xlsx")
#data=xlrd.open_workbook("../dataconfig/interface.xlsx")
tables=data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(0,0))

def readtestdatafromexcel(sheetname,row,column): #此方法根据sheetname以及行数和列数三个数据返回excel单元格数据
    x1 = xlrd.open_workbook(path4)
    sheet1 = x1.sheet_by_name(sheetname)
    return sheet1.cell_value(row, column)
    pass
def writetestresultintoecxel(sheetindex,row,column,msg):#此方法根据sheet索引，行数和列数以及输入信息四个参数对excel单元格写入数据
    x2=xlrd.open_workbook(path4)
    newx2=copy(x2)
    a=newx2.get_sheet(sheetindex)
    a.write(row,column,msg)
    newx2.save(path4)
    pass
'''


class OperationExcel:
    def __init__(self, url=None):
        if url:    
            self.url = url
        else:
            self.url = "e:\py\pythonworkspace\interfaceframework\dataconfig\interface.xlsx"
        self.data = self.get_data()

    # 获取sheet的内容

    def get_data(self):
        data = xlrd.open_workbook(self.url)
        tables = data.sheets()[0]
        return tables

    # 获取单元格的行数

    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容

    def get_cell_value(self, row, col):
        return self.get_data().cell_value(row, col)

    # 将值写进某个单元格

    def writetestresultintoecxel(self, row, col, msg):
        x1 = xlrd.open_workbook(self.url)
        newx2 = copy(x1)
        a = newx2.get_sheet(0)
        a.write(row, col, msg)
        newx2.save(self.url)


if __name__ == "__main__":
    a = OperationExcel()
    # res=a.get_cell_value(0,2)
    # res=a.get_data()
    # print(res)
    a.writetestresultintoecxel(15, 15, "你好")