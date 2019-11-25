from rest_framework import serializers, request

from util.crypo import encode4md5
from util.error import YKException
from util.sms_ import validate_code
from ykuser.models import YKUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = YKUser
        fields = "__all__"


class UserCheckSerializer(serializers.Serializer):  # 注册
    phone = serializers.CharField(max_length=11, required=False)
    code = serializers.CharField(max_length=6, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        phone = attrs.get("phone")
        code = attrs.get("code")

        user = YKUser().select_all(phone=phone)
        if not phone:
            raise YKException("手机号不能为空")
        if user:
            raise YKException("手机号已存在")
        if not code:
            raise YKException("验证码不能为空")
        if not validate_code(phone,code):
            raise YKException("验证码错误")
        return attrs


# 验证码登录
class UserloginCheckSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, required=False)
    code = serializers.CharField(max_length=6, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        phone = attrs.get("phone")
        code = attrs.get("code")
        if not phone:
            raise YKException("手机号不能为空")
        if not code:
            raise YKException("验证码不能为空")
        if not validate_code(phone, code):
            raise YKException("验证码错误")
        return attrs


#账号密码登录
class UserLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=12, required=False)
    pwd = serializers.CharField(max_length=6, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        name = attrs.get("name")
        pwd = attrs.get("pwd")
        pwd_ = encode4md5(pwd)
        print(pwd_,type(pwd_))
        if not name:
            raise YKException("用户名不能为空！")
        if not pwd:
            raise YKException("密码不能为空！")
        if not YKUser().select_all(name=name):
            raise YKException("用户名错误！")
        if not YKUser().select_all(pwd=pwd_):
            raise YKException("密码错误！")
        return attrs
