import time

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from tools.bank_card_code import get_bank_info
from tools.cache_ import add_token, valid_token
from tools.crypo import encode4md5
from tools.file_dow import file_upload
from tools.integral_level_calculation import compute
from tools.sms_ import send_code
from tools.toke_ import new_token
from ykuser.models import YKUser, InFor, Pack, Recharge, BackCard
from ykuser.serializers import UserSerializer, UserCheckSerializer, UserLoginSerializer, \
    UserloginCheckSerializer, InforSerializer, User_CheckSerializer, PayPwdCheckSerializer, RechargeCheckSerializer, \
    BillSerializer, BankCardSerializer, CardSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = YKUser.objects.all()
    serializer_class = UserSerializer

    # 验证码注册
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=UserCheckSerializer)
    def register(self, request):
        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 901,
                "msg": e.detail
            }
            return Response(result)
        # name = ser.data["name"]  # 从序列化对象中获取用户名
        phone = ser.data["phone"]
        pwd = ser.data["pwd"]
        # emil = ser.data["emil"]
        make_pwd = encode4md5(pwd)  # 加密密码
        try:
            ykuser = YKUser()
            ykuser.save_user(phone=phone, pwd=make_pwd)  # 储存数据
        except Exception as e:
            result = {
                "status": 1,
                "msg": "注册异常"
            }
            print(e)
            return Response(result)

        result = {
            "status": 0,
            "msg": "注册成功",
            "data": {
                "phone": phone
            }
        }
        return Response(result)

    # 账号密码注册
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=User_CheckSerializer)
    def register_(self, request):
        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 901,
                "msg": e.detail
            }
            return Response(result)
        name = ser.data["name"]  # 从序列化对象中获取用户名
        pwd = ser.data["pwd"]
        make_pwd = encode4md5(pwd)  # 加密密码
        try:
            print(name, make_pwd)
            YKUser().save_user(name=name, pwd=make_pwd)  # 储存数据
        except Exception as e:
            result = {
                "status": 1,
                "msg": "注册异常"
            }
            print(e)
            return Response(result)

        result = {
            "status": 0,
            "msg": "注册成功",
            "data": {
                "phone": name,
                "pwd": make_pwd
            }
        }
        return Response(result)

    # 发送验证码
    @action(methods=["post"], detail=False)
    def code(self, request):
        phone = request.data.get("phone") if request.data.get("phone") else request.query_params.get("phone")
        print(phone)
        try:
            send_code(phone)
            result = {
                "status": 0,
                "msg": "发送成功"
            }
            return Response(result)
        except:
            result = {
                "status": 1,
                "msg": "发送失败，请重新发送！"
            }
            return Response(result)

    # 登录(验证码登录)
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=UserloginCheckSerializer)
    def login_sms(self, request):
        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 902,
                "msg": e.detail
            }
            return Response(result)
        phone = ser.data["phone"]
        flag = ser.data["flag"]  # 登录验证
        token = new_token()  # 定义token
        user = YKUser().select_all(phone=phone).first()
        if (not flag) or (not user):
            result = {
                "code": 901,
                "status": 1,
                "msg": "登录失败！"
            }
            return Response(result)
        print("user.id==", user.id)
        add_token(token=token, user_id=user.id)
        # cache.set(token, user.id, timeout=3600*24*14)  # 将token存储到缓存中
        result = {
            "status": 0,
            "msg": "登录成功！",
            "token": token
        }
        return Response(result)

    # 登录(账号密码登录)
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=UserLoginSerializer)
    def login(self, request):
        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 902,
                "msg": e.detail
            }
            return Response(result)
        name = ser.data["name"]
        flag = ser.data["flag"]  # 登录验证
        token = new_token()  # 定义token
        user = YKUser().select_all(name=name)
        print(flag, type(flag))
        if (not flag) or (not user):
            result = {
                "code": 901,
                "status": 1,
                "msg": "登录失败！"
            }
            return Response(result)
        print(user.id)
        add_token(token=token, user_id=user.id)  # 将token存储到缓存中
        result = {
            "status": 0,
            "msg": "登录成功！",
            "token": token
        }
        return Response(result)

    # 进行token验证,返回用户id
    def token_(self, request):
        # 获取token，False为GET获取
        token = request.data.get("token") if request.data.get("token") else request.query_params.get("token")
        print("token===", token)
        userid = valid_token(token)
        user = YKUser().select_all(id=userid)
        # 判断用户是否存在
        if user:
            # 判断用户id是否正确
            if int(userid) != user.id:
                return None
            return int(userid)
        return None

    # 个人资料查询
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["GET"], detail=False)
    def in_for_(self, request):
        print("==========================")
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        # 验证用户信息是否存在
        user_infor = InFor().select_infor_all(user_id)
        if not user_infor:
            result = {
                "status": 2,
                "msg": "请完善你的个人资料！"
            }
            return Response(result)
        print(user_infor)
        result = {
            "status": 0,
            "msg": "获取到已存在的数据！",
            "data": {
                "nikname": user_infor.yk_nickname,  # 昵称
                "name": user_infor.yk_name,  # 真实姓名
                "head": user_infor.yk_avatar,  # 头像
                "sex": user_infor.yk_sex,  # 性别
                "age": user_infor.yk_age,  # 年龄
                "career": user_infor.yk_career,  # 职业
                "hobby": user_infor.yk_hobby,  # 兴趣爱好
                "idnumber": user_infor.yk_idnumber,  # 身份证件号
                "signature": user_infor.yk_signature,  # 个性签名

            }
        }
        return Response(result)

    # 个人资料添加
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=InforSerializer)
    def in_for(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 901,
                "msg": e.detail
            }
            return Response(result)
        upload_file = request.FILES.get("head")[0]  # 接收上传文件对象,头像图片
        head_url = file_upload(upload_file)  # 图片地址
        if head_url:
            head_url = head_url
        else:
            head_url = "图片格式错误！"
        nikname = ser.data["nikname"]  # 从序列化对象中获取昵称
        name = ser.data["name"]  # 真实姓名
        sex = ser.data["sex"]  # 性别
        age = ser.data["age"]  # 年龄
        career = ser.data["career"]  # 职业
        hobby = ser.data["hobby"]  # 兴趣爱好
        idnumber = ser.data["idnumber"]  # 身份证件号
        signature = ser.data["signature"]  # 个性签名

        try:
            InFor().save_infor(user_id=int(user_id), nikname=nikname, name=name, head=head_url,
                               sex=sex, age=age, career=career, hobby=hobby,
                               idnumber=idnumber, signature=signature)
        except Exception as e:
            result = {
                "status": 1,
                "msg": "添加异常"
            }
            print(e)
            return Response(result)

        result = {
            "status": 0,
            "msg": "成功！",
            "data": {
                "nikname": nikname,  # 昵称
                "name": name,  # 真实姓名
                "head": head_url,  # 头像
                "sex": sex,  # 性别
                "age": age,  # 年龄
                "career": career,  # 职业
                "hobby": hobby,  # 兴趣爱好
                "idnumber": idnumber,  # 身份证件号
                "signature": signature,  # 个性签名
            }
        }
        return Response(result)

    # 个人钱包加载
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["GET"], detail=False)
    def wallet(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        pack = Pack().select_pack_all(user_id=user_id)
        if not pack:
            Pack().save_pack(user_id=user_id)
            result = {
                "status": 0,
                "msg": "查询成功！",
                "data": {
                    "money": 0,
                    "integral": 0,
                    "member": "柚籽",
                }
            }
            return Response(result)
        result = {
            "status": 0,
            "msg": "查询成功！",
            "data": {
                "money": pack.yk_balance,  # 余额
                "integral": pack.yk_integral,  # 积分
                "member": pack.yk_member,  # 等级
                "discount": pack.yk_discount  # 折扣
            }
        }
        return Response(result)

    # 添加修改支付密码
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=PayPwdCheckSerializer)
    def paypwd(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 901,
                "msg": e.detail
            }
            return Response(result)
        phone = ser.data["phone"]
        pay_pwd = ser.data["pay_pwd"]
        make_pwd = encode4md5(pay_pwd)  # 加密密码
        # 判断储存是否成功
        update_ped = Pack().update_pwd(user_id=user_id, pay_pwd=make_pwd)
        print(update_ped)
        if not update_ped:  # 储存数据
            result = {
                "code": 900,
                "status": 1,
                "msg": "重置异常！"
            }
            return Response(result)

        result = {
            "status": 0,
            "msg": "重置成功！",
            "data": {
                "phone": phone
            }
        }
        return Response(result)

    # 柚币充值
    # 由@action装饰器装饰的方法，方法名作为路径名
    @action(methods=["post"], detail=False, serializer_class=RechargeCheckSerializer)
    def recharge(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 901,
                "msg": e.detail
            }
            return Response(result)
        pwd = ser.data["pay_pwd"]  # 接收密码
        money = float(ser.data["money"])  # 接收充值或消费金额
        paymenType = ser.data["paymenType"]  # :param paymenType:支付方式（0：微信，1：支付宝，2：柚币）
        transType = ser.data["transType"]  # :param transType:消费方式（0:充值，1：消费）
        make_pwd = encode4md5(pwd)  # 加密密码
        pack = Pack().select_pack_all(user_id=user_id)  # 获取用户钱包信息
        integral = pack.yk_integral  # 查询用户积分
        balance = float(pack.yk_balance)  # 账号余额
        pay_pwd = pack.yk_pay_pwd  # 支付密码
        # 验证支付密码是否正确
        if make_pwd == pay_pwd:
            # 判断支付类型0表示充值1，表示消费
            if str(transType) == "0":
                item_dict = compute(money=money, integral=integral)  # 计算等级
                u_money = item_dict["money"]  # 充值金额
                u_integral = item_dict["integral"]  # 总积分
                u_member = item_dict["member"]  # 等级
                u_discount = item_dict["discount"]  # 折扣
                u_part = item_dict["part"]  # 积分
                sum_money = balance + u_money
                time_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间
                print(time_local)

                # 存储账单信息
                rech = Recharge().save_recharge(user_id=user_id, pack_id=pack.id, bill_time=time_local, integral=u_part,
                                                amount=sum_money, paymenType=str(paymenType), transType=str(transType))
                if rech:
                    print("账单生成成功······")
                else:
                    print("账单生成失败······")
                try:
                    Pack().save_pack(user_id=user_id, money=sum_money, integral=u_integral,
                                     member=u_member, discount=u_discount)  # 储存钱包数据
                    result = {
                        "status": 0,
                        "msg": "充值成功！",
                        "data": {
                            "money": sum_money,
                            "integral": u_integral,
                            "member": u_member,
                            "discount": u_discount
                        }
                    }
                    return Response(result)
                except Exception as e:
                    result = {
                        "code": 900,
                        "status": 3,
                        "msg": "充值异常！"
                    }
                    print(e)
                    return Response(result)
            elif str(transType) == "1":
                sum = balance - money
                # 判断余额是否充足
                if sum >= 0:
                    # 存储账单信息
                    time_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    rech = Recharge().save_recharge(user_id=user_id, pack_id=pack.id, bill_time=time_local,
                                                    amount=money, paymenType=str(paymenType),
                                                    transType=str(transType))
                    if rech:
                        print("账单生成成功······")
                    else:
                        print("账单生成失败······")
                    result = {
                        "status": 0,
                        "msg": "支付成功！",
                        "money": sum
                    }
                    Pack().update_money(user_id=user_id, money=sum)
                    return Response(result)
                else:
                    result = {
                        "code": 900,
                        "status": 4,
                        "msg": "支付失败，余额不足！"
                    }
                    return Response(result)

        else:
            result = {
                "code": 900,
                "status": 2,
                "msg": "支付失败！"
            }
            return Response(result)

    # 账单查询
    @action(methods=["get"], detail=False, serializer_class=BillSerializer)
    def bill(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        bills = Recharge().select_recharge_all(user_id=user_id)
        ser = self.get_serializer(bills, many=True)
        result = {
            "status": 0,
            "msg": "账单查询成功！",
            "data": ser.data
        }
        return Response(result)

    # 绑定银行卡
    @action(methods=["post"], detail=False, serializer_class=CardSerializer)
    def card(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)

        ser = self.get_serializer(data=request.data)  # 接收请求体中的参数，并将其封装到@action设置的序列化类对象中
        try:
            ser.is_valid(raise_exception=True)  # 会触发序列化对象的验证，包括格式验证和逻辑验证
        except APIException as e:
            result = {
                "code": 901,
                "msg": e.detail
            }
            return Response(result)

        name = ser.data["name"]
        cardID = ser.data["cardID"]
        bank_dict = get_bank_info(cardID)
        bank_name = bank_dict["bank_name"]
        card_type = bank_dict["card_type"]
        logo_href = bank_dict["logo_href"]
        try:
            BackCard().save_card(user_id=user_id, card_id=cardID, name=name, card_name=bank_name,
                                 card_type=card_type, card_logo=logo_href)

            result = {
                "status": 0,
                "msg": "添加成功！"
            }
            return Response(result)
        except:
            result = {
                "status": 2,
                "msg": "添加异常！"
            }
            return Response(result)

    # 银行卡查询查询
    @action(methods=["get"], detail=False, serializer_class=BankCardSerializer)
    def bank(self, request):
        user_id = self.token_(request)  # 验证token是否存在
        if not user_id:
            result = {
                "status": 1,
                "msg": "你还没有登陆，请登陆！"
            }
            return Response(result)
        try:
            cards = BackCard().select_card(user_id=user_id)
            ser = self.get_serializer(cards, many=True)
            result = {
                "status": 0,
                "msg": "银行卡信息查询成功！",
                "data": ser.data
            }
            return Response(result)
        except:
            result = {
                "code": 900,
                "status": 0,
                "msg": "你还没有添加银行卡，请添加！"
            }
            return Response(result)

    # 测试文件上传
    @action(methods=["post"], detail=False)
    def file(self, request):
        if request.FILES:
            image = request.FILES.getlist('up_file')[0]  # 拿到上传文件
            if not image:
                return Response({"msg":"接受文件为空"})
            print(image,"=====================")
            print(image.file)
            print(image.name)
            print(image.content_type)
            file_upload(image)
            return Response({"msg":"接受文件成功"})
