import uuid

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from util.cache_ import add_token
from util.crypo import encode4md5
from util.sms_ import send_code
from util.toke_ import new_token
from ykuser.models import YKUser
from ykuser.serializers import UserSerializer, UserCheckSerializer, UserLoginSerializer,UserloginCheckSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = YKUser.objects.all()
    serializer_class = UserSerializer

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
        # pwd = ser.data["pwd"]
        # emil = ser.data["emil"]
        code = ser.data["code"]
        print(phone[-6:])
        make_pwd = encode4md5(phone[-6:])  # 加密密码
        try:
            ykuser = YKUser()
            ykuser.save_user(phone=phone,pwd=make_pwd) # 储存数据
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
        # 发送验证码

    @action(methods=["post"], detail=False)
    def code(self, request):
        phone = request.POST.get("phone")
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

    #登录(验证码登录)
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
        token = new_token()  # 定义token
        user = YKUser().select_all(phone=phone).first()
        if not user:
            result = {
                "status": 1,
                "msg": "登录失败！"
            }
            return Response(result)
        print(user.id)
        add_token(token=token,user_id=user.id)
        # cache.set(token, user.id, timeout=60 * 60)  # 将token存储到缓存中
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
        token = new_token()  # 定义token
        user = YKUser().select_all(name=name).first()
        if not user:
            result = {
                "status": 1,
                "msg": "登录失败！"
            }
            return Response(result)
        print(user.id)
        # cache.set(token, user.id, timeout=60 * 60)  # 将token存储到缓存中
        result = {
            "status": 0,
            "msg": "登录成功！",
            "token": token
        }
        return Response(result)


