def compute(money, integral):
    """
    折扣计算
    :param money:充值金额
    :param integral: 积分
    :return:
    """
    part = money * 0.1
    integral += part
    if integral <= 200:
        member = "柚籽"
        discount = "0.99"
    elif integral <= 500:
        member = "柚苗"
        discount = "0.96"
    elif integral <= 1000:
        member = "柚树"
        discount = "0.9"
    elif integral <= 1500:
        member = "青柚"
        discount = "0.88"
    elif integral <= 2000:
        member = "红柚"
        discount = "0.85"
    elif integral <= 5000:
        member = "金柚"
        discount = "0.8"
    item_dict = {
        "money": money,
        "member": member,
        "discount": discount,
        "integral": integral,
        "part": part,
    }
    return item_dict

