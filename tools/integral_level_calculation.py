def compute(money, integral):
    """
    折扣计算
    :param money:充值金额
    :param integral: 积分
    :return:
    """
    part = money * 0.1
    integral += part
    member = "柚籽"
    discount = "九九折"
    if integral <= 200:
        member = "柚籽"
        discount = "九九折"
    elif integral <= 500:
        member = "柚苗"
        discount = "九六折"
    elif integral <= 1000:
        member = "柚树"
        discount = "九折"
    elif integral <= 1500:
        member = "青柚"
        discount = "八八折"
    elif integral <= 2000:
        member = "红柚"
        discount = "八五折"
    elif integral <= 5000:
        member = "金苗"
        discount = "八折"
    item_dict = {
        "money": money,
        "member": member,
        "discount": discount,
        "integral": integral,
        "part": part,
    }
    return item_dict

