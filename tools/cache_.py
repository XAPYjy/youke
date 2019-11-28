from tools import rd1 as rd


def add_token(token, user_id):
    # 登录成功后绑定token和user_id
    rd.set(token, user_id, ex=3600 * 24 * 14)


def remove_token(token):
    # 退出时删除token
    op = rd.delete(token)
    if op == 1:
        return True
    else:
        return False


def valid_token(token):
    # 验证token是否存在
    userid = rd.get(token.lstrip(" "))
    print("userid==========", userid)
    if userid:
        return userid
    return False


def get_user_id_for_token(token):
    # 获取token绑定的id
    pass
