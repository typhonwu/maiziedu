# -*- coding:utf-8 -*- 

'''
Function:handle database's any operation
Author:Wan Shitao
Email:wst.521@163.com
Date:2014.8.20
Reference:funcs.py
'''
from twisted.enterprise import adbapi
import MySQLdb


# 连接mysql


def get_db(**kwargs):
    '''connect database,return link resource'''
    try:
        db = MySQLdb.connect(**kwargs)
    except Exception, e:
        print "Link DB error:", e
    else:
        return db

# 创建表格,proxy中并没有用到这个方法
def create_table (data, primary, table, **kwargs):
    ''' Create table for storing resume data. '''
    # 这是建表sql语句，用了占位符
    sql='create table if not exists `%s`(%s) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'
    # 这是python的列表解析式
    # 左边一个方括号是一个列表
    # 右边是可选参数，有传入主键就加上
    # data中是传入的建表需要的字段
    ps = ["`%s` text" % x for x in data] + ([primary, ] if primary else [])
    # 把列表中的字段名称拼接成字符串
    paras = ','.join(ps)
    # 再填充sql语句的占位符
    SQL = sql % (table, paras)
    # 调用另一个函数执行sql语句
    exec_sql(SQL, **kwargs)

# 执行sql语句的函数


def exec_sql(sql, data='', **kwargs):
    '''execute insert sql and other operation'''
    conn = get_db(**kwargs)
    cur = conn.cursor()
    if data == '':
        # 调用游标的sql语句执行函数
        cur.execute(sql)
    else:
        cur.execute(sql, data)
    # 执行之后调用函数获取全部结果，是一个列表
    result = cur.fetchall()
    # 提交这个结果
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
    return result

    
def insert_data (data_,table,**kwargs):
    '''insert data into database''' 
    insertSQL="insert into `"+table+"`(%s) values (%s)"
    keys = data_.keys()
    fields = ','.join([ '`%s`'%k for k in keys ])
    qm = ','.join(['%s'] * len(keys))
    sql = insertSQL % (fields,qm)
    data = [ data_[k] for k in keys ]
    exec_sql(sql,data,**kwargs)


def adb_connect_db(db_type,**kwargs):
    '''
    db_type-->"MySQLdb"
    '''
    dbpool = adbapi.ConnectionPool(db_type, **kwargs)
    return dbpool

def adb_insert_data(item,table,db_type,**kwargs):
    keys = item.keys()
    fields = u','.join(keys)
    qm = u','.join([u'%s'] * len(keys))
    insert_sql="insert into `"+table+"`(%s) values (%s)"
    sql = insert_sql % (fields, qm)
    data = [item[k] for k in keys]
    dbpool=adb_connect_db(db_type,**kwargs)
    d = dbpool.runOperation(sql, data)
    d.addCallback(insSuccess)
    d.addErrback(insFailed,item)
    dbpool.close()
    
def insSuccess(data):
    print "data inserted",data
    
def insFailed(exp,data):
    print "insert failed",data,"error:",exp.getErrorMessage()
