__author__ = 'Administrator'
import mysql.connector
#1数据库配置
config ={"host":"112.74.134.29",
         "user":"kstone",
         "password":"kstone!QAZ",
         "port":"3307",
         "database":"bear",
         "charset":"utf8"
}
#2.连接数据库
cnn=mysql.connector.connect(**config)

#3.创建游标
cursor=cnn.cursor()
#4.查询
cursor.execute("select * from ks_users where reg_mobile=15899860330")
a=cursor.fetchone()



