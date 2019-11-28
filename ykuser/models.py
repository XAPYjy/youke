from django.db.models import Q

from yk_models.models import YkUser, YkInformation, YkWallet, YkBillingDetails, YkBankCard, YkLesson


# 用户类
class YKUser(YkUser):
    def save_user(self, name=None, pwd=None, phone=None, emil=None, auth=True):
        YkUser.objects.create(yk_name=name, yk_auto_string=pwd, yk_phone=phone, yk_emil=emil, sys_auth=auth)

    def select_all(self, id=0, name=0, phone=0, pwd=0, emil=0):
        try:
            q = Q(id=id) | Q(yk_name=name) | Q(yk_phone=int(phone)) | Q(yk_auto_string=pwd) | Q(yk_emil=emil)
            item = YkUser.objects.filter(q).first()
            return item
        except:
            return None

    def up_pwd(self, user_id, up_pwd):
        users = YKUser.objects.filter(id=user_id)
        users.yk_auto_string = up_pwd
        users.save()


# 个人资料类
class InFor(YkInformation):
    def select_infor_all(self, userid):
        try:
            item = YkInformation.objects.filter(yk_user_id=userid).first()
            return item
        except:
            return None

    def save_infor(self, user_id, nikname=None, name=None, head=None, sex=None,
                   age=0, career=None, hobby=None, signature=None):
        """
        :param nikname: 昵称
        :param name: 真实姓名
        :param head: 头像
        :param sex: 性别
        :param age: 年龄
        :param career: 职业
        :param hobby: 兴趣爱好
        :param idnumber: 身份证件号
        :param signature: 个性签名
        :return:
        """
        # 判断用户资料是否存在，存在更新，不存在新增
        if self.select_infor_all(user_id):
            infor_update = YkInformation.objects.filter(yk_user_id=user_id)
            infor_update.update(yk_nickname=nikname, yk_name=name, yk_avatar=head,
                                yk_sex=sex, yk_age=age, yk_career=career, yk_hobby=hobby,
                                yk_signature=signature, yk_user_id=user_id)
        else:
            YkInformation.objects.create(yk_nickname=nikname, yk_name=name, yk_avatar=head,
                                         yk_sex=sex, yk_age=age, yk_career=career, yk_hobby=hobby,
                                         yk_signature=signature, yk_user_id=user_id)

    # 头像上传
    def up_head(self, user_id, head_img):
        infor = YkInformation.objects.filter(yk_user_id=user_id).first()
        if infor:
            infor.yk_avatar = head_img
            infor.save()
        else:
            YkInformation.objects.create(yk_user_id=user_id, yk_avatar=head_img)


# 钱包类
class Pack(YkWallet):
    # 查询个人钱包数据
    def select_pack_all(self, user_id):
        try:
            item = YkWallet.objects.filter(yk_user_id=user_id).first()
            return item
        except:
            return None

    # 添加钱包数据
    def save_pack(self, user_id, money="0", integral=0, member="柚籽", discount=None):
        """
        :param user_id: 用户id
        :param money: 余额
        :param integral:积分
        :param member:积分等级
        :param discount:会员折扣
        :return:
        """
        # 判断用户是否存在钱包资料，存在更新，不存在新增
        if self.select_pack_all(user_id):
            pack_update = YkWallet.objects.filter(yk_user_id=user_id)
            pack_update.update(yk_user_id=user_id, yk_balance=money,
                               yk_integral=integral, yk_member=member,
                               yk_discount=discount)
        else:
            YkWallet.objects.create(yk_user_id=user_id, yk_balance=money,
                                    yk_integral=integral, yk_member=member,
                                    yk_discount=discount)

    # 修改支付密码
    def update_pwd(self, user_id, pay_pwd):
        # pay_pwd: 支付密码
        try:
            wallet = YkWallet.objects.filter(yk_user_id=user_id).first()
            # 判断查询为空，重新添加
            if not wallet:
                YkWallet.objects.create(yk_user_id=user_id, yk_pay_pwd=pay_pwd)
                return True
            wallet.yk_pay_pwd = pay_pwd
            wallet.save()
            return True
        except Exception as e:
            print(e)
            return False

    # 修改消费金额
    def update_money(self, user_id, money):
        # pay_pwd: 支付密码
        try:
            wallet = YkWallet.objects.filter(yk_user_id=user_id).first()
            wallet.yk_balance = money
            wallet.save()
            return True
        except:
            return False


# 账单类
class Recharge(YkBillingDetails):
    def select_recharge_all(self, user_id):
        try:
            items = YkBillingDetails.objects.filter(yk_user_id=user_id).order_by('-yk_bill_time')
            return items
        except:
            return None

    def save_recharge(self, user_id, pack_id, bill_time=None, amount=None,
                      integral=None, paymenType=None, transType=None):
        """
        :param user_id: 用户id
        :param pack_id: 钱包id
        :param bill_time: 时间
        :param amount: 金额
        :param integral 积分
        :param paymenType:支付方式（0：微信，1：支付宝）
        :param transType:消费方式（0:充值，1：消费）
        :return:
        """
        try:
            YkBillingDetails.objects.create(yk_user_id=user_id, yk_wallet_id=pack_id, yk_bill_time=bill_time,
                                            yk_amount=amount, yk_integral=integral,
                                            yk_transtype=transType, yk_paymentype=paymenType
                                            )
            return True
        except Exception as e:
            print(e)
            return False


# 银行卡类
class BackCard(YkBankCard):
    # 查询用户银行卡
    def select_card(self, user_id):
        items = YkBankCard.objects.filter(yk_user_id=user_id)
        return items

    # 判断银行卡号是否存在
    def isIDcard(self, card_id):
        try:
            items = YkBankCard.objects.filter(yk_id_card=card_id)
            return items
        except:
            return None

    # 添加银行卡
    def save_card(self, user_id, card_id, name, card_name, card_type, card_logo):
        """
        :param user_id: 用户id
        :param card_id: 银行卡号
        :param name: 姓名
        :param card_name:银行卡名称
        :param card_type: 银行卡类型
        :param card_logo: 银行卡logo
        :return:
        """
        YkBankCard.objects.create(yk_user_id=user_id, yk_id_card=card_id, name=name,
                                  yk_card_name=card_name, yk_card_type=card_type, yk_card_logo=card_logo)


# 课程类
class Lesson(YkLesson):
    # 查询用户课程
    def select_class(self, user_id):
        try:
            items = YkLesson.objects.filter(yk_user_id=user_id)
            return items
        except:
            return None

    # 添加课程
    def update_class(self, user_id=None, classname=None, classfile=None, classimg=None, price=None, lessonDescribe=None,
                     oneSort=None, towSort=None,
                     classChapter=None, teacherDescribe=None, class_size=None, up_time=None):
        """"
        classname课程名称
        classfile视频文件
        classimg课程图片
        price课程价格
        lessonDescribe课程描述
        oneSort课程一级分类
        towSort课程二级分类
        classChapter课程章节
        teacherDescribe讲师描述
        class_size 视频大小
        up_time  上传时间
        """
        YkLesson.objects.create(yk_user_id=user_id, yk_lesson_name=classname, yk_video_jump_link=classfile,
                                yk_lesson_img=classimg, yk_class_size=class_size,
                                yk_lesson_price=price, yk_up_time=up_time,
                                yk_lesson_describe=lessonDescribe, yk_teacher_describe=teacherDescribe,
                                yk_one_list_id=oneSort, yk_tow_list_id=towSort, yk_course_chapter=classChapter)
