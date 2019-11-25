import operator
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yk_models.models import *

#对模型类进行序列化
class FirstclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firstclass
        fields = ('yk_firstclassname',)

class SecondclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secondclass
        fields = ('yk_secondclassname','secondimage')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = YkLesson
        fields = ('yk_lesson_name','yk_lesson_price','yk_lesson_img')

#将id字节的数据转成字节类型
# def to_id_str(datas):
#     for item in datas:
#         item['id'] = str(item['id'])
        # item['yk_firstclassid'] = str(item['yk_firstclassid'])
        # item['yk_secondclassid'] = str(item['yk_secondclassid'])

# #根据价格对查询到的课程进行升序排序
# def price_sort(datas):
#     sorted(datas,key=operator.itemgetter('课程价格'))
# #根据价格对查询到的课程进行降序排序
# def price_unsort(datas):
#     sorted(datas,key=operator.itemgetter('课程价格'),reverse=True)

#大分类的视图函数
@api_view(["GET"])
def first_class(request):
    data = int(request.GET.get('Sortid'))
    #对查询出来的所有大类对象进行序列化
    if data == 1:
        bb = FirstclassSerializer(Firstclass.objects.all(), many=True).data
    #对查询出来的所有小类对象进行序列化
        cc = SecondclassSerializer(Secondclass.objects.all(), many=True).data
    # to_id_str(bb)
    # to_id_str(cc)
    #封装参数
        result = {
            'code': 200,
            'left': bb,
            'all': cc
        }
        return Response(result)

# @api_view(["GET"])
# def second_class(request):
#     data = int(request.GET.get('typeid'))
#     ff = SecondclassSerializer(Secondclass.objects.filter(yk_firstclassid=data), many=True).data
#     to_id_str(ff)
#     result = {
#         'code': 200,
#         'data': ff
#     }
#     return Response(result)

#课程的视图函数
@api_view(["GET"])
def lesson_list(request):
    #接收前端传来的小分类id
    data2 = int(request.GET.get('secondid'))
    # data3 = int(request.GET.get('sortid'))
    #根据接收来的小分类id查找相符的课程，并进行序列化
    jj = LessonSerializer(YkLesson.objects.filter(yk_tow_list_id=data2), many=True).data
    # to_id_str(jj)
    result = {
        'code': 200,
        'data':jj
    }
    return Response(result)

#分类的视图函数
@api_view(["GET"])
def sort_lesson(request):
    #接收前端传来的小类id和分类id
    data2 = int(request.GET.get('secondid'))
    data3 = int(request.GET.get('sortid'))
    #根据小类id查找相符的课程，并将其序列化
    kk = LessonSerializer(YkLesson.objects.filter(yk_tow_list_id=data2), many=True).data
    #判断分类id的类型
    if data3 == 0:
        # # ll = to_id_str(mm)
        # print(mm)
        # r = []
        # for i in kk:
        #     r1 = {}
        #     r1['课程id']=i['id']
        #     r1['课程名称']=i['yk_lesson_name']
        #     r1['课程价格'] = i['yk_lesson_price']
        #     r.append(r1)
        # print(r)
        # mm = price_sort(r)
        #进行升序排序
        mm = sorted(kk, key=operator.itemgetter('yk_lesson_price'))
        result = {
            'code': 200,
            'data': mm
        }
        return Response(result)
    elif data3 == 1:
        mm = sorted(kk, key=operator.itemgetter('yk_lesson_price'),reverse=True)
        result = {
            'code': 200,
            'data': mm
        }
        return Response(result)
    #     r = []
    #     for i in kk:
    #         r1 = {}
    #         r1['课程id'] = i['id']
    #         r1['课程名称'] = i['yk_lesson_name']
    #         r1['课程价格'] = i['yk_lesson_price']
    #         r.append(r1)
    #     #进行降序排序
    #     mm = sorted(r, key=operator.itemgetter('课程价格'),reverse=True)
    #     # ll = to_id_str(mm)
    #     result = {
    #
    #    'code': 200,
    #         'data': mm
    #     }
    #     return Response(result)