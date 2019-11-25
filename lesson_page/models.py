from django.db import models


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
    yk_lesson_click = models.IntegerField(blank=True, null=True)
    yk_class_size = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'yk_lesson'


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



class YkDiscuss(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_user_id = models.IntegerField()
    yk_discuss_contents = models.CharField(max_length=100)
    yk_discuss_date = models.DateTimeField()
    yk_discuss_outdate = models.DateTimeField()
    yk_discuss_click_num = models.IntegerField(blank=True, null=True)
    yk_lesson_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'yk_discuss'


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
    yk_phone = models.CharField(max_length=50, blank=True, null=True)
    sys_auth = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_user'


class YkViedo(models.Model):
    id = models.IntegerField(primary_key=True)
    yk_video_name = models.CharField(max_length=50, blank=True, null=True)
    yk_lesson_id = models.IntegerField()
    yk_video_progress = models.FloatField(blank=True, null=True)
    yk_user_id = models.IntegerField()
    yk_crats_id = models.IntegerField(blank=True, null=True)
    yk_lesson_jump_link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'yk_viedo'
