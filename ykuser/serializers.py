from rest_framework import serializers, request

from tools.crypo import encode4md5
from tools.error import YKException
from tools.sms_ import validate_code
from yk_models.models import YkBillingDetails, YkBankCard, YkLesson
from ykuser.models import YKUser, BackCard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = YKUser
        fields = "__all__"


class UserCheckSerializer(serializers.Serializer):  # 注册
    phone = serializers.CharField(max_length=12, required=False)
    code = serializers.CharField(max_length=7, required=False)
    pwd = serializers.CharField(max_length=20, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        phone = attrs.get("phone")
        code = attrs.get("code")
        pwd = attrs.get("pwd")

        if not phone:
            raise YKException("手机号不能为空！")
        if not code:
            raise YKException("验证码不能为空！")
        if not pwd:
            raise YKException("密码不能为空！")
        if YKUser().select_all(phone=phone):
            raise YKException("手机号已存在！")
        if not validate_code(phone, code):
            raise YKException("验证码错误！")
        return attrs


# 账号密码注册
class User_CheckSerializer(serializers.Serializer):  # 注册
    name = serializers.CharField(max_length=20, required=False)
    pwd = serializers.CharField(max_length=20, required=False)
    pwd_code = serializers.CharField(max_length=20, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        name = attrs.get("name")
        pwd = attrs.get("pwd")
        pwd_code = attrs.get("pwd_code")

        if not name:
            raise YKException("用户名不能为空！")
        if not pwd:
            raise YKException("密码不能为空！")
        if not pwd_code:
            raise YKException("确认密码不能为空！")
        if YKUser().select_all(name=name):
            raise YKException("用户名已存在！")
        if pwd != pwd_code:
            raise YKException("两次密码不相同，请重新输入！")
        return attrs


# 验证码登录
class UserloginCheckSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, required=False)
    code = serializers.CharField(max_length=7, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        phone = attrs.get("phone")
        code = attrs.get("code")
        if not phone:
            raise YKException("手机号不能为空！")
        if not code:
            raise YKException("验证码不能为空！")
        if not validate_code(phone, code):
            raise YKException("验证码错误！")
        return attrs


# 账号密码登录
class UserLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=12, required=False)
    pwd = serializers.CharField(max_length=20, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        name = attrs.get("name")
        pwd = attrs.get("pwd")
        if not name:
            raise YKException("用户名不能为空！")
        if not pwd:
            raise YKException("密码不能为空！")
        if not YKUser().select_all(name=name):
            raise YKException("用户名错误！")
        if not YKUser().select_all(pwd=encode4md5(pwd)):
            raise YKException("密码错误！")
        return attrs


# 修改密码
class UpPwdCheckSerializer(serializers.Serializer):
    pwd = serializers.CharField(max_length=18, required=False)
    up_pwd = serializers.CharField(max_length=18, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        pwd = attrs.get("pwd")
        up_pwd = attrs.get("up_pwd")

        if not pwd:
            raise YKException("旧密码不能为空！")
        if not up_pwd:
            raise YKException("新密码不能为空！")
        return attrs


# 个人资料
# class InforSerializer(serializers.Serializer):
#     nikname = serializers.CharField(max_length=20, required=False, default=None)  # 昵称
#     name = serializers.CharField(max_length=6, required=False, default=None)  # 真实姓名
#     sex = serializers.CharField(max_length=6, required=False, default=None)  # 性别
#     age = serializers.CharField(max_length=6, required=False, default=None)  # 年龄
#     career = serializers.CharField(max_length=30, required=False, default=None)  # 职业
#     hobby = serializers.CharField(max_length=50, required=False, default=None)  # 兴趣爱好
#     idnumber = serializers.CharField(max_length=18, required=False, default=None)  # 身份证件号
#     signature = serializers.CharField(max_length=50, required=False, default=None)  # 个性签名
#

# 修改支付密码
class PayPwdCheckSerializer(serializers.Serializer):
    # phone = serializers.CharField(max_length=11, required=False)
    # code = serializers.CharField(max_length=6, required=False)
    pay_pwd = serializers.CharField(max_length=6, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        # phone = attrs.get("phone")
        # code = attrs.get("code")
        pay_pwd = attrs.get("pay_pwd")

        # if not phone:
        #     raise YKException("手机号不能为空！")
        # if not code:
        #     raise YKException("验证码不能为空！")
        if not pay_pwd:
            raise YKException("密码不能为空！")
        # if not validate_code(phone, code):
        #     raise YKException("验证码错误！")
        # phone_ = YKUser().select_all(phone=phone).yk_phone
        # if not phone_:
        #     raise YKException("手机号不匹配！")
        return attrs


# 充值和消费
class RechargeCheckSerializer(serializers.Serializer):
    pay_pwd = serializers.CharField(max_length=10, required=False)
    money = serializers.CharField(max_length=11, required=False)
    paymenType = serializers.CharField(max_length=11, required=False, default=None)
    transType = serializers.CharField(max_length=11, required=False, default=None)
    """
        :param paymenType:支付方式（0：微信，1：支付宝）
        :param transType:消费方式（0:充值，1：消费）
    """

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        money = attrs.get("money")
        pay_pwd = attrs.get("pay_pwd")
        if not money:
            raise YKException("金额不能为空！")
        if not pay_pwd:
            raise YKException("密码不能为空！")
        return attrs


# 账单查询
class BillSerializer(serializers.ModelSerializer):
    bill_time = serializers.CharField(max_length=20, source='yk_bill_time')
    amount = serializers.FloatField(source='yk_amount')
    integral = serializers.FloatField(source='yk_integral')
    transtype = serializers.CharField(max_length=20, source='yk_transtype')
    paymentype = serializers.CharField(max_length=20, source='yk_paymentype')

    class Meta:
        model = YkBillingDetails
        fields = ["bill_time", "amount", "integral", "transtype", "paymentype"]


# 绑定银行卡
class CardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=6, required=False)
    phone = serializers.CharField(max_length=11, required=False)
    cardID = serializers.CharField(max_length=20, required=False)
    code = serializers.CharField(max_length=6, required=False)

    # 重写validate方法，进行逻辑认证
    def validate(self, attrs):
        name = attrs.get("name")
        phone = attrs.get("phone")
        cardID = attrs.get("cardID")
        code = attrs.get("code")
        if not name:
            raise YKException("姓名不能为空！")
        if not phone:
            raise YKException("手机号不能为空！")
        phone_ = YKUser().select_all(phone=phone).yk_phone
        if not phone_:
            raise YKException("手机号不匹配！")
        if not cardID:
            raise YKException("银行卡号不能为空！")
        card_id = BackCard().isIDcard(card_id=str(cardID))
        if card_id:
            raise YKException("银行卡已存在！")
        if not code:
            raise YKException("验证码不能为空！")
        if not validate_code(phone, code):
            raise YKException("验证码错误！")

        return attrs


# 账单查询
class BankCardSerializer(serializers.ModelSerializer):
    card_id = serializers.CharField(max_length=20, source='yk_id_card')
    card_name = serializers.CharField(max_length=20, source='yk_card_name')
    card_type = serializers.CharField(max_length=10, source='yk_card_type')
    card_logo = serializers.CharField(max_length=256, source='yk_card_logo')

    class Meta:
        model = YkBankCard
        fields = ["card_id", "card_name", "card_type", "card_logo"]


# 视频上传
class LessonCardSerializer(serializers.Serializer):
    classname = serializers.CharField(max_length=20, required=False, default=None)  # 课程名称
    price = serializers.FloatField(required=False, default=None)  # 课程价格
    lessonDescribe = serializers.CharField(max_length=200, required=False, default=None)  # 课程描述
    oneSort = serializers.CharField(max_length=20, required=False, default=None)  # 课程一级分类
    towSort = serializers.CharField(max_length=20, required=False, default=None)  # 课程二级分类
    classChapter = serializers.CharField(max_length=10, required=False, default=None)  # 课程章节
    teacherDescribe = serializers.CharField(max_length=200, required=False, default=None)  # 讲师描述


# 我的课程获取
class ClassCardSerializes(serializers.ModelSerializer):
    lesson_name = serializers.CharField(max_length=20, source='yk_lesson_name')  # 课程名称
    video_link = serializers.CharField(max_length=20, source='yk_video_jump_link')  # 课程地址
    lesson_describe = serializers.CharField(max_length=20, source='yk_lesson_describe')  # 课程描述
    watch_amount = serializers.CharField(max_length=20, source='yk_watch_amount')  # 课程观看数
    lesson_img = serializers.CharField(max_length=20, source='yk_lesson_img')  # 课程图片
    lesson_price = serializers.CharField(max_length=20, source='yk_lesson_price')  # 课程价格

    class Meta:
        model = YkLesson
        fields = ["lesson_name", "video_link", "lesson_describe", "watch_amount", "lesson_img", "lesson_price"]


# 我的订单
class OrderCardSerializes(serializers.ModelSerializer):
    lesson_name = serializers.CharField(max_length=20, source='yk_lesson_name')  # 课程名称
    video_link = serializers.CharField(max_length=20, source='yk_video_jump_link')  # 课程地址
    lesson_describe = serializers.CharField(max_length=20, source='yk_lesson_describe')  # 课程描述
    watch_amount = serializers.CharField(max_length=20, source='yk_watch_amount')  # 课程观看数
    lesson_img = serializers.CharField(max_length=20, source='yk_lesson_img')  # 课程图片
    lesson_price = serializers.CharField(max_length=20, source='yk_lesson_price')  # 课程价格

    class Meta:
        model = YkLesson
        fields = ["lesson_name", "video_link", "lesson_describe", "watch_amount", "lesson_img", "lesson_price"]
