<<<<<<< HEAD
=======
import pymysql


>>>>>>> 7c7e28ee0ce95810bdc62bb92398d2f6484fb269
def get_conn():
    conn = pymysql.connect(
        host="47.92.132.161",
        port=3306,
        user="root",
        password='root',
        database='youke'
    )
    return conn


<<<<<<< HEAD
def delete_user(user_id):
    conn =get_conn()
    cursor = conn.cursor()
    sql = "delete from  yk_user where id=%s"
    cursor.execute(sql,(user_id,))
    conn.commit()

if __name__ == '__main__':
    delete_user(4)
=======
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

>>>>>>> 7c7e28ee0ce95810bdc62bb92398d2f6484fb269
