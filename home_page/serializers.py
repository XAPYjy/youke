from rest_framework import serializers
from home_page.models import *


class WheelSerializer(serializers.ModelSerializer):  # 轮播序列化
    class Meta:
        model = YkRotation
        fields = "__all__"

class RecSerializer(serializers.ModelSerializer):  # 推荐课程序列化
    class Meta:
        model = YkRecommend
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):  # 单门课程序列化
    class Meta:
        model = YkLesson
        fields = "__all__"
