import pymysql

def login(usr_name, usr_password):
    conn = pymysql.connect(host='localhost', port=3306, db='kindshell', user='root', password='123')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from tableofteacher where ID=%s'
    row = cursor.execute(sql, usr_name)
    sql = 'select * from tableofteacher where ID=%s and password=%s'
    pawrow = cursor.execute(sql, (usr_name, usr_password))
    print(int(pawrow))
    conn.commit()
    cursor.close()
    conn.close()

    if int(row) == 1:
        print('有该用户')
        if int(pawrow) == 1:
            print('密码也对')
        else:
            return 1
        return 2
    else:
        return 0


