import copy

from django.http import JsonResponse
from django.db.models import Q
from home_page.models import *


def home_view(request):
    roationData = []  # 所有的轮播图的数据
    recommendData = []  # 所有的推荐课程的数据
    roatlessons = {}  # 单个轮播图的属性集合
    recommendList = {}  # 单门推荐课程的属性集合
    more = []
    rotaions = YkRotation.objects.values_list("id")
    recommends = YkRecommend.objects.values_list("id",'yk_lesson_type')  # 获取推荐课程分类和id
    lesson = YkLesson.objects.all()
    for i in range(0,len(rotaions)-1):  # 生成轮播数据
        s = YkLesson.objects.filter(yk_rotaion_id=rotaions[i][0]).values('id','yk_lesson_img')
        roatlessons['roationId'] = i + 1
        roatlessons['lessonId'] = s[0]["id"]
        roatlessons['lessonImg'] = s[0]['yk_lesson_img']
        s = roatlessons.copy()
        roationData.append(s)
    for j  in range(len(recommends)):  # 生成推荐数据
        d = YkLesson.objects.filter(yk_recommend_id=recommends[j][0]).values_list('id','yk_lesson_name', 'yk_lesson_img','yk_lesson_price','yk_buy_amount','yk_lesson_price_type','yk_lesson_describe')[:14]

        recommendList["recommendId"] = recommends[j][0]
        recommendList['lessonType'] = recommends[j][1]

        lessonList = []  # 单个推荐课程下的课程列表
        relessons = {}  # 推荐课程的单门课程的属性集合yk_recommend_id
        if len(d) != 0:
            for i in range(len(d)):
                relessons['lessonId'] = d[i][0]
                relessons['lessonName'] = d[i][1]
                relessons['lessonImg'] = d[i][2]
                relessons['lessonPrice'] = d[i][3]
                relessons['buyAmount'] = d[i][4]
                relessons['priceType'] = d[i][5]
                relessons['lessonDescribe'] = d[i][6]
                rel = copy.deepcopy(relessons)
                lessonList.append(rel)
                les = tuple(lessonList)

            # 生成推荐课程属性集合
                les = list(les)
                recommendList['LessonList'] = les
            r = recommendList.copy()
            # 生成推荐数据包
            recommendData.append(r)
    s = []
    for i in recommends:
        s.append(i[0])

    more_lessons = lesson.exclude(yk_recommend_id__in=s).values_list(
        'id', 'yk_lesson_name', 'yk_lesson_img', 'yk_lesson_price', 'yk_buy_amount', 'yk_lesson_price_type','yk_lesson_describe')[:20]
    more_lesson = {}
    for i in range(len(more_lessons)):
        more_lesson['lessonId'] = more_lessons[i][0]
        more_lesson['lessonName'] = more_lessons[i][1]
        more_lesson['lessonImg'] = more_lessons[i][2]
        more_lesson['lessonPrice'] = more_lessons[i][3]
        more_lesson['buyAmount'] = more_lessons[i][4]
        more_lesson['priceType'] = more_lessons[i][5]
        more_lesson['lessonDescribe'] = more_lessons[i][6]
        rel = copy.deepcopy(more_lesson)
        more.append(rel)

    r = recommendList.copy()
    # 生成推荐数据包
    recommendData.append(r)

    result = {
        "error":0,
        "roationData":roationData,
        "recommendData":recommendData,
        'more':more
    }
    return JsonResponse(result)

def search_view(request):
    serachData=[]
    search_lesson={}

    if request.method == "GET":
        global result
        data = request.GET.get("data")
        q1 = Q(yk_lesson_name__contains=data)
        q2 = Q(yk_teacher_describe__contains=data)
        search_lessons = YkLesson.objects.filter(q1|q2).values_list('id','yk_lesson_name', 'yk_lesson_img','yk_lesson_price','yk_buy_amount','yk_lesson_price_type','yk_teacher_describe','yk_lesson_describe')
        if search_lessons:
            for i in search_lessons:  # 获取查询到的课程
                search_lesson['lessionId'] = i[0]
                search_lesson['lessionName'] = i[1]
                search_lesson['lessionImg'] = i[2]
                search_lesson['lessionPrice'] = i[3]
                search_lesson['buyAmount'] = i[4]
                search_lesson['priceType'] = i[5]
                search_lesson['teacherDescribe'] = i[6]
                search_lesson['lessonDescribe'] = i[7]
                se = copy.deepcopy(search_lesson)
                serachData.append(se)

            result = {
                'error': 0,
                'serachData': serachData
            }
        else:
            result = {
                'error':0,
                'serachData':'不好意思，没查到该数据！'
            }
    return JsonResponse(result)
