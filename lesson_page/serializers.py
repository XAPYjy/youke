from rest_framework import serializers
from lesson_page.models import *


class YkViedoSerializer(serializers.ModelSerializer):  # 视频表序列化
    class Meta:
        model = YkViedo
        fields = "__all__"

class RecSerializer(serializers.ModelSerializer):  # 评论表序列化
    class Meta:
        model = YkDiscuss
        fields = "__all__"

class LessonListSerializer(serializers.ModelSerializer):  # 课程列表序列化
    class Meta:
        model = Lessonlist
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):  # 单门课程序列化
    class Meta:
        model = YkLesson
        fields = "__all__"