import pymysql


def get_conn():
    conn = pymysql.connect(
        host="47.92.132.161",
        port=3306,
        user="root",
        password='root',
        database='youke'
    )
    return conn


# def delete_user(user_id):
# #     conn =get_conn()
# #     cursor = conn.cursor()
# #     sql = "delete from  yk_user where id=%s"
# #     cursor.execute(sql,(user_id,))
# #     conn.commit()

# 重置登陆密码
def update_pwd(user_id,up_pwd):
    try:
        conn =get_conn()
        cursor = conn.cursor()
        sql = "update  yk_user set yk_auto_string=%s where id = %s"
        cursor.execute(sql,(up_pwd,user_id))
        conn.commit()
        return True
    except:
        return None
    finally:
        cursor.close()
        conn.close()


# 重置登陆密码
def update_phone(user_id,phone):
    try:
        conn =get_conn()
        cursor = conn.cursor()
        sql = "update  yk_user set yk_phone=%s where id = %s"
        cursor.execute(sql,(phone,user_id))
        conn.commit()
        return True
    except:
        return None
    finally:
        cursor.close()
        conn.close()
