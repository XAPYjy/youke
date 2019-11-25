from django.db import models


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
        db_table = 'downloadrecord'


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


class YkUser(models.Model):
    yk_name = models.CharField(max_length=50, blank=True, null=True)
    yk_auto_string = models.CharField(max_length=100, blank=True, null=True)
    yk_emil = models.CharField(max_length=50, blank=True, null=True)
    yk_phone = models.CharField(max_length=50,blank=True, null=True)
    sys_auth = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'yk_user'
