import copy

from django.http import JsonResponse
from lesson_page.models import *


def detail_view(request):
    if request.method == "GET":
        lessonData = {}
        recommendData = []
        rec_lesson = {}
        likeData = []
        likelesson = {}
        user_id = request.GET.get("uid")
        lesson_id = request.GET.get('lessonId')
        print(lesson_id)
        # 获取上一个页面返回的课程id的课程详情
        lesson = YkLesson.objects.filter(id=lesson_id).values_list('yk_video_jump_link','yk_lesson_name','yk_lesson_price','yk_class_size','yk_course_chapter','yk_teacher_describe','yk_lesson_click','yk_watch_amount','yk_buy_amount')
        #获取这个课程的目录下的课程数量
        lessonContentsNum = YkLesson.objects.filter(id=lesson_id).values('yk_lesson_contents_mark').count()
        #查询当前课程的二级分类
        two_list_id = YkLesson.objects.filter(id=lesson_id).values_list('yk_tow_list_id')[0][0]
        print('two_list_id=',two_list_id)
        # 'yk_video_jump_link'视频, 'yk_lesson_name', 'yk_lesson_price'价格,
        # 'yk_class_size'视屏大小, 'yk_course_chapter'章节,
        # 'yk_teacher_describe', 'yk_lesson_click'点击率,'yk_watch_amount'观看数目,'yk_buy_amount'已购买
        # 封装课程详情
        lessonData['lessonId'] = lesson_id
        lessonData['lessonVideo'] = lesson[0][0]
        lessonData['lessonName'] = lesson[0][1]
        lessonData['lessonPrice'] = lesson[0][2]
        lessonData['lessonVideoSize'] = lesson[0][3]
        lessonData['lessonChapter'] = lesson[0][4]
        lessonData['lessonContentsNum'] = lessonContentsNum
        lessonData['teacherDescribe'] = lesson[0][5]
        lessonData['lessonClick'] = lesson[0][6]
        lessonData['watchAmount'] = lesson[0][7]
        lessonData['buyAmount'] = lesson[0][8]
        # 封装推荐课程
        recommendLessons = YkLesson.objects.exclude(id=lesson_id).\
        filter(yk_tow_list_id=two_list_id).values_list('id', 'yk_lesson_name','yk_lesson_img',
                             'yk_lesson_price','yk_buy_amount',
                              'yk_lesson_price_type','yk_teacher_describe')[:5]
        for i in range(len(recommendLessons)):
            rec_lesson['lessonId'] = recommendLessons[i][0]
            rec_lesson['lessonName'] = recommendLessons[i][1]
            rec_lesson['lessonImg'] = recommendLessons[i][2]
            rec_lesson['lessonPrice'] = recommendLessons[i][3]
            rec_lesson['buyAmount'] = recommendLessons[i][4]
            rec_lesson['priceType'] = recommendLessons[i][5]
            rel = copy.deepcopy(rec_lesson)
            recommendData.append(rel)
        if user_id:

            likeLessons = YkLesson.objects.exclude(id=lesson_id).\
            filter(yk_lesson_price_type='免费').values_list('id', 'yk_lesson_name','yk_lesson_img',
                             'yk_lesson_price','yk_buy_amount',
                              'yk_lesson_price_type','yk_teacher_describe')[:5]
            for i in range(len(likeLessons)):
                likelesson['lessonId'] = likeLessons[i][0]
                likelesson['lessonName'] = likeLessons[i][1]
                likelesson['lessonImg'] = likeLessons[i][2]
                likelesson['lessonPrice'] = likeLessons[i][3]
                likelesson['buyAmount'] = likeLessons[i][4]
                likelesson['priceType'] = likeLessons[i][5]
                like = copy.deepcopy(likelesson)
                likeData.append(like)
        result = {
            'error':0,
            'lessonData':lessonData,
            'likeData':likeData,
            'recommendData':recommendData
        }
    return JsonResponse(result)


def discuss_view(request):
    if request.method == "GET":
        discussesData = []
        discuss_data = {}
        # 点击评论从后台
        lessonid = request.GET.get('lessonId')
        print('lessonId=',lessonid)
        # 获取所有评论
        discusses = YkDiscuss.objects.filter(yk_lesson_id=lessonid).values_list('id','yk_user_id','yk_discuss_date','yk_discuss_contents','yk_discuss_click_num')
        '''id,yk_user_id,yk_discuss_date,yk_discuss_contents,yk_discuss_click_num'''
        for i in range(len(discusses)):  #封装评论区
            discuss_data['disuserId'] = discusses[i][0]  #评论人id
            discuss_data['discussId'] = discusses[i][1]  #评论id
            discuss_data['lessonId'] = lessonid   #课程id
            discuss_data['discussData'] = discusses[i][2]  # 评论时间
            discuss_data['discussContents'] = discusses[i][3]  # 评论内容
            #discuss_data['discussClick'] = discusses[i][4]  #评论点赞数
            #封装到列表
            like = copy.deepcopy(discuss_data)
            discussesData.append(like)
        result = {
            'error':0,
            'discussesData':discussesData
        }
        return JsonResponse(result)

    elif request.method == 'POST':
        pass






