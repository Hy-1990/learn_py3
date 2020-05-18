# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> mysqlutils
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/28 1:45 下午
# @Desc   ：
# ==================================================
import pymysql
import GlobalParameters
import traceback


def get_connect():
    db = pymysql.connect(GlobalParameters.mysql_host, GlobalParameters.mysql_username, GlobalParameters.mysql_password,
                         GlobalParameters.mysql_database)
    return db


def test():
    db = get_connect()
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)

    sql = "select * from node"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(str(row))
    except Exception as e:
        print(e)
        # traceback.print_exc()


if __name__ == '__main__':
    test()
