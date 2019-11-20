from django.db import models


# 后台管理
class SysRole(models.Model):
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysUser(models.Model):
    name = models.CharField(unique=True, max_length=50)
    auth_string = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.name, self.auth_string, self.email, self.phone)

    @property
    def role(self):
        role_id = SysUserRole.objects.get(user_id=self.id).role_id
        return SysRole.objects.get(pk=role_id)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user_role'


# 分类
# 一级分类
class Firstclass(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_firstclassname = models.CharField(db_column='yk_FirstClassName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FirstClass'


# 二级分类
class Secondclass(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_secondclassname = models.CharField(db_column='yk_SecondClassName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    yk_firstclassid = models.IntegerField(db_column='yk_FirstClassID', blank=True, null=True)  # Field name made lowercase.
    yk_jumplink = models.CharField(db_column='yk_JumpLink', max_length=256, blank=True, null=True)  # Field name made lowercase.
    yk_likenumber = models.IntegerField(db_column='yk_LikeNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecondClass'


# 课程列表
class Lessonlist(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_clicks = models.IntegerField(db_column='yk_Clicks', blank=True, null=True)  # Field name made lowercase.
    yk_ageclass = models.IntegerField(db_column='yk_AgeClass', blank=True, null=True)  # Field name made lowercase.
    yk_secondclassid = models.IntegerField(db_column='yk_SecondClassID', blank=True, null=True)  # Field name made lowercase.
    yk_lessonlistname = models.CharField(db_column='yk_LessonListName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LessonList'


# 课程
class Lesson(models.Model):
    yk_video_jump_link = models.CharField(max_length=200)
    yk_lesson_name = models.CharField(max_length=50, blank=True, null=True)
    yk_lesson_price = models.FloatField(blank=True, null=True)
    yk_lesson_describe = models.CharField(max_length=200, blank=True, null=True)
    yk_teacher_describe = models.CharField(max_length=100, blank=True, null=True)
    yk_lesson_contents = models.CharField(max_length=50)
    yk_lesson_contents_mark = models.IntegerField()
    yk_lesson_image = models.CharField(max_length=256, blank=True, null=True)
    yk_rotation_id = models.IntegerField(blank=True, null=True)
    yk_recommend_lesson_id = models.IntegerField(blank=True, null=True)
    yk_price_class = models.IntegerField(blank=True, null=True)
    yk_discount_price = models.FloatField(blank=True, null=True)
    yk_lesson_list_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lesson'


# 柚子树
class Bags(models.Model):
    yk_goods_type = models.IntegerField()
    yk_list_id = models.IntegerField(blank=True, null=True)
    yk_lesson_id = models.IntegerField()
    yk_price = models.FloatField()
    yk_authority = models.IntegerField()
    yk_user_id = models.IntegerField()
    yk_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'bags'


# 我的页面
class BillingDetails(models.Model):
    yk_wallet_id = models.IntegerField(blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)
    yk_recharge_time = models.TimeField(blank=True, null=True)
    yk_recharge_amount = models.FloatField(blank=True, null=True)
    yk_consumption_time = models.TimeField(blank=True, null=True)
    yk_consumption_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_details'


class Downloadrecord(models.Model):
    yk_dowtime = models.TimeField(db_column='yk_dowTime', blank=True, null=True)  # Field name made lowercase.
    yk_dowcontent = models.CharField(db_column='yk_dowContent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yk_u_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadRecord'


class Information(models.Model):
    yk_nickname = models.CharField(max_length=50, blank=True, null=True)
    yk_name = models.CharField(max_length=50, blank=True, null=True)
    yk_avatar = models.CharField(max_length=256, blank=True, null=True)
    yk_sex = models.CharField(max_length=10, blank=True, null=True)
    yk_age = models.IntegerField(blank=True, null=True)
    yk_career = models.CharField(db_column='yk_Career', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yk_hobby = models.CharField(max_length=50, blank=True, null=True)
    yk_idnumber = models.CharField(db_column='yk_IDnumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yk_signature = models.CharField(max_length=500, blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'information'


class Mycourse(models.Model):
    yk_user_id = models.IntegerField(blank=True, null=True)
    yk_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mycourse'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_nume = models.CharField(max_length=50)
    yk_auto_string = models.CharField(max_length=50)
    yk_phone = models.IntegerField()
    sys_auth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Wallet(models.Model):
    yk_balance = models.CharField(max_length=50, blank=True, null=True)
    yk_pay_pwd = models.CharField(max_length=50, blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)
    yk_bank_card = models.IntegerField(blank=True, null=True)
    yk_integral = models.IntegerField(blank=True, null=True)
    yk_member = models.CharField(max_length=50, blank=True, null=True)
    yk_discount = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet'


class YkLesson(models.Model):
    yk_video_jump_link = models.CharField(max_length=200, blank=True, null=True)
    yk_lesson_name = models.CharField(max_length=50, blank=True, null=True)
    yk_lesson_price = models.FloatField(blank=True, null=True)
    yk_lesson_describe = models.CharField(max_length=200, blank=True, null=True)
    yk_teacher_describe = models.CharField(max_length=100, blank=True, null=True)
    yk_lesson_contents = models.CharField(max_length=50, blank=True, null=True)
    yk_lesson_contents_mark = models.IntegerField(blank=True, null=True)
    yk_lesson_img = models.CharField(max_length=200, blank=True, null=True)
    yk_rotaion_id = models.IntegerField(blank=True, null=True)
    yk_recommend_id = models.IntegerField(blank=True, null=True)
    yk_lesson_price_type = models.CharField(max_length=50, blank=True, null=True)
    yk_lesson_dis_price = models.FloatField(blank=True, null=True)
    yk_lesson_list = models.IntegerField(blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)
    yk_buy_amount = models.IntegerField(blank=True, null=True)
    yk_watch_amount = models.IntegerField(blank=True, null=True)
    yk_course_chapter = models.CharField(max_length=20, blank=True, null=True)
    yk_one_list_id = models.IntegerField(blank=True, null=True)
    yk_tow_list_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_lesson'


class UserOrder(models.Model):
    yk_goods_id = models.IntegerField(blank=True, null=True)
    yk_isorderstatus = models.IntegerField(db_column='yk_isorderStatus', blank=True, null=True)  # Field name made lowercase.
    yk_total_price = models.FloatField(blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_order'


class YkRotation(models.Model):
    yk_is_rotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yk_rotation'


class YkRecommend(models.Model):
    yk_lesson_type = models.CharField(max_length=200)
    yk_lesson_jump_link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'yk_recommend'


class YkDiscuss(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_user_id = models.IntegerField()
    yk_discuss_contents = models.CharField(max_length=100)
    yk_discuss_date = models.DateTimeField()
    yk_discuss_outdate = models.DateTimeField()
    yk_discuss_click_num = models.IntegerField(blank=True, null=True)
    yk_lesson_id = models.IntegerField()
    yk_discuss_authority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yk_discuss'
