#此模块没开发及封装完
import pymysql
# 连接database
conn=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    db="python_test",
    charset="utf8"
)
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor() #默认返回元组类型数据 即("a","b","c")
# 定义要执行的SQL语句
sql ="select * from interface"
# 执行SQL语句
cursor.execute(sql)
res=cursor.fetchall()
for row in res:
    print(row[0])
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()