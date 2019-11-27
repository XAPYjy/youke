from rest_framework import serializers
from yk_models.models import Bags, YkLesson


class YKCartSerializer(serializers.ModelSerializer):  # 购物车序列化类
    class Meta:
        model = Bags
        fields = "__all__"


# class YKOrder(serializers.ModelSerializer):
#     pid = serializers.CharField(max_length=50, source='id')
#     cost = serializers.FloatField(source='yk_total_price')
#
#     class Meta:
#         model = Bags
#         fields = ['pid','cost']


class YKLessonSerializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=50, source='id')
    info = serializers.CharField(max_length=200, source='yk_course_chapter')
    price = serializers.FloatField(source='yk_lesson_price')
    pic = serializers.CharField(max_length=200, source='yk_lesson_img')

    class Meta:
        model = YkLesson
        fields = ['pid','info','price','pic']


class YKLesson2Serializer(serializers.ModelSerializer):
    pid = serializers.CharField(max_length=50, source='id')
    title = serializers.CharField(max_length=200, source='yk_lesson_name')
    detail = serializers.CharField(max_length=200, source='yk_teacher_describe')   # 讲师简介
    # process = serializers.FloatField(source='yk_video_progress')   # 学习进度百分比
    pic = serializers.CharField(max_length=200, source='yk_lesson_img')

    class Meta:
        model = YkLesson
        fields = ['pid','title','detail','pic']

        def get_bags_name(self):
            bags_name = Bags.objects.filter().process
            return bags_name