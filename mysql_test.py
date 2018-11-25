import pymysql

try:
    db = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="123456"  # 数据库密码
    )
    print("连接数据成功...")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM ming.sys_dept"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            dept_id = row[0]
            parent_id = row[1]
            name = row[2]
            order_num = row[3]
            del_flg = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                  (dept_id, parent_id, name, order_num, del_flg))
    except Exception as e:
        print("SQL语句异常...")
        print(e)

    # 关闭数据库连接
    db.close()
except Exception as e:
    print("连接数据失败....")
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
