# 引入decimal模块
import pymysql

import config

configs = config.config()

class link:
    # 连接数据库
    db = pymysql.connect(host=configs.mysql_host,
                         user=configs.mysql_user,
                         password=configs.mysql_password,
                         charset='utf8',
                         port=configs.mysql_port)

    # 创建一个游标对象（相当于指针）
    cursor = None

    def __init__(self):
        self.cursor = self.db.cursor()
        self.cursor.execute('use meteorology;')


    def execute(self, sql):
        self.cursor.execute(sql)

    def get_execute(self):
        return self.cursor.fetchall()


# # 创建一个游标对象（相当于指针）
# cursor = db.cursor()
#
# # 执行创建数据库语句
# cursor.execute('use meteorology;')
# cursor.execute('select * from serial_set')
#
# # fetchone获取一条数据（元组类型）
# print(cursor.fetchone())
# # 现在指针到了[1]的位置
#
# # fetchall获取全部数据（字符串类型）
# all = cursor.fetchall()
# for i in all:
#     print(i[0])
#
# # 关闭游标和数据库连接
# cursor.close()
# db.close()
