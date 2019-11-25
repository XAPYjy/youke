# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Firstclass(models.Model):
    yk_firstclassid = models.IntegerField(db_column='yk_FirstClassID')  # Field name made lowercase.
    yk_firstclassname = models.CharField(db_column='yk_FirstClassName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FirstClass'


class Secondclass(models.Model):
    yk_secondclassid = models.IntegerField(db_column='yk_SecondClassID')  # Field name made lowercase.
    yk_secondclassname = models.CharField(db_column='yk_SecondClassName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    yk_firstclassid = models.IntegerField(db_column='yk_FirstClassID', blank=True, null=True)  # Field name made lowercase.
    secondimage = models.CharField(max_length=256, blank=True, null=True)
    secondurl = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SecondClass'


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


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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


class Lessonlist(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_lessonname = models.CharField(db_column='yk_LessonName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    yk_lessonimage = models.CharField(db_column='yk_LessonImage', max_length=256, blank=True, null=True)  # Field name made lowercase.
    yk_lessonclassid = models.IntegerField(db_column='yk_LessonClassID', blank=True, null=True)  # Field name made lowercase.
    yk_priceclassid = models.IntegerField(db_column='yk_PriceClassID', blank=True, null=True)  # Field name made lowercase.
    yk_price = models.FloatField(db_column='yk_Price', blank=True, null=True)  # Field name made lowercase.
    yk_jumplink = models.CharField(db_column='yk_JumpLink', max_length=256, blank=True, null=True)  # Field name made lowercase.
    yk_clicks = models.IntegerField(db_column='yk_Clicks', blank=True, null=True)  # Field name made lowercase.
    yk_ageclass = models.CharField(db_column='yk_AgeClass', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lessonlist'


class Mycourse(models.Model):
    yk_user_id = models.IntegerField(blank=True, null=True)
    yk_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mycourse'


class Wallet(models.Model):
    yk_balance = models.CharField(max_length=50, blank=True, null=True)
    yk_pay_pwd = models.CharField(max_length=100, blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)
    yk_bank_card = models.IntegerField(blank=True, null=True)
    yk_integral = models.IntegerField(blank=True, null=True)
    yk_member = models.CharField(max_length=50, blank=True, null=True)
    yk_discount = models.CharField(max_length=10, blank=True, null=True)
    yk_paymentype = models.CharField(db_column='yk_paymenType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    yk_transtype = models.CharField(db_column='yk_transType', max_length=5, blank=True, null=True)  # Field name made lowercase.

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
    yk_class_size = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_lesson'


class YkOrder(models.Model):
    yk_goods_id = models.IntegerField(blank=True, null=True)
    yk_isorderstatus = models.IntegerField(db_column='yk_isorderStatus', blank=True, null=True)  # Field name made lowercase.
    yk_total_price = models.FloatField(blank=True, null=True)
    yk_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_order'


class YkRecommend(models.Model):
    yk_lesson_type = models.CharField(max_length=200)
    yk_lesson_jump_link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'yk_recommend'


class YkRotation(models.Model):
    yk_is_rotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yk_rotation'


class YkUser(models.Model):
    yk_name = models.CharField(max_length=50, blank=True, null=True)
    yk_auto_string = models.CharField(max_length=100, blank=True, null=True)
    yk_emil = models.CharField(max_length=50, blank=True, null=True)
    yk_phone = models.CharField(max_length=50, blank=True, null=True)
    sys_auth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_user'
