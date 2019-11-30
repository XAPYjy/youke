def get_conn():
    conn = pymysql.connect(
        host="47.92.132.161",
        port=3306,
        user="root",
        password='root',
        database='youke'
    )
    return conn


def delete_user(user_id):
    conn =get_conn()
    cursor = conn.cursor()
    sql = "delete from  yk_user where id=%s"
    cursor.execute(sql,(user_id,))
    conn.commit()

if __name__ == '__main__':
    delete_user(4)