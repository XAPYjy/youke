import copy
import time

from django.http import JsonResponse

from lesson_page.models import *
from tools.cache_ import valid_token
from yk_models.models import YkOrder, Bags

# from util.cache_ import valid_token

from tools.cache_ import valid_token
from yk_models.models import YkOrder, Bags


def detail_view(request):
    if request.method == "GET":
        global result
        lessonData = {}
        recommendData = []
        rec_lesson = {}
        likeData = []
        likelesson = {}
        user_id = request.GET.get("uid")
        lesson_id = request.GET.get('lessonId')
        # 获取上一个页面返回的课程id的课程详情
        lesson = YkLesson.objects.filter(id=lesson_id).values_list('yk_video_jump_link','yk_lesson_name','yk_lesson_price','yk_class_size','yk_course_chapter','yk_teacher_describe','yk_lesson_click','yk_watch_amount','yk_buy_amount','yk_lesson_describe')
        #获取这个课程的目录下的课程数量
        lessonContentsNum = YkLesson.objects.filter(id=lesson_id).values('yk_lesson_contents_mark').count()
        #查询当前课程的二级分类
        two_list_id = YkLesson.objects.filter(id=lesson_id).values_list('yk_tow_list_id')[0][0]
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
        lessonData['lessonDescribe'] = lesson[0][9]
        # 封装推荐课程
        recommendLessons = YkLesson.objects.exclude(id=lesson_id).\
        filter(yk_tow_list_id=two_list_id).values_list('id', 'yk_lesson_name','yk_lesson_img',
                             'yk_lesson_price','yk_buy_amount',
                              'yk_lesson_price_type','yk_teacher_describe','yk_lesson_describe')[:5]
        for i in range(len(recommendLessons)):
            rec_lesson['lessonId'] = recommendLessons[i][0]
            rec_lesson['lessonName'] = recommendLessons[i][1]
            rec_lesson['lessonImg'] = recommendLessons[i][2]
            rec_lesson['lessonPrice'] = recommendLessons[i][3]
            rec_lesson['buyAmount'] = recommendLessons[i][4]
            rec_lesson['priceType'] = recommendLessons[i][5]
            rec_lesson['teacherDescribe'] = recommendLessons[i][6]
            rec_lesson['lessonDescribe'] = recommendLessons[i][7]
            rel = copy.deepcopy(rec_lesson)
            recommendData.append(rel)
        if user_id:

            likeLessons = YkLesson.objects.exclude(id=lesson_id).\
            filter(yk_lesson_price_type='免费').values_list('id', 'yk_lesson_name','yk_lesson_img',
                             'yk_lesson_price','yk_buy_amount',
                              'yk_lesson_price_type','yk_teacher_describe','yk_lesson_describe')[:5]
            for i in range(len(likeLessons)):
                likelesson['lessonId'] = likeLessons[i][0]
                likelesson['lessonName'] = likeLessons[i][1]
                likelesson['lessonImg'] = likeLessons[i][2]
                likelesson['lessonPrice'] = likeLessons[i][3]
                likelesson['buyAmount'] = likeLessons[i][4]
                likelesson['priceType'] = likeLessons[i][5]
                likelesson['teacherDescribe'] = likeLessons[i][6]
                likelesson['lessonDescribe'] = likeLessons[i][7]
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

def add2cart(request):
    token = request.POST.get('token')
    pid = request.POST.get('lessonId')
    user_id = valid_token(token)
    lesson_price = YkLesson.objects.filter(id=pid).values_list('yk_lesson_price')[0][0]
    print('lesson_price=',lesson_price)
    islesson = Bags.objects.filter(yk_user_id=user_id,yk_lesson_id=pid).first()
    print('islesson=',islesson)
    i = float("1")
    if not islesson:
        global result
        Bags.objects.create(
            yk_goods_type=False,
            yk_list_id=None,
            yk_lesson_id=pid,
            yk_price=lesson_price,
            yk_user_id=user_id,
            yk_time=None,
            yk_video_progress=0
        )
        result = {
            'code': 0,
            'msg': '添加成功！'
        }
    else:
        result = {
            'code':0,
            'msg':'添加失败，已存在购物车，请勿重新添加！'
        }

    return JsonResponse(result)


# 前端页面点击购买按钮，后台做的操作
def buy_lesson(request):
    token = request.POST.get('token')  # token验证用户的登陆状态
    pid = int(request.POST.get('lessonId'))
    if not token:
        return JsonResponse({
            'code': 1,
            'msg': '未登录,请重新登陆'})
    user_id = valid_token(token)
    carts = YkOrder.objects.filter(yk_user_id=user_id).values_list('yk_goods_id')
    print(carts)
    order_list = []
    for i in carts:
        order_list.append(i[0])
    total_price = 0
    if pid in order_list:
        lessonname = YkLesson.objects.filter(id=pid).values('yk_lesson_name')[0]
        result = {
            "code": 0,
            "msg": str(lessonname['yk_lesson_name']) + "已存在订单中，请勿重新添加！！！"
        }
        return JsonResponse(result)
    else:
        yk_price = YkLesson.objects.filter(id=pid).values_list('yk_lesson_price')[0][0]
        total_price += yk_price
        YkOrder.objects.create(yk_goods_id=pid,
                               yk_total_price=total_price,
                               yk_isorderstatus=None,
                               yk_user_id=user_id)

        num = YkOrder.objects.filter(yk_goods_id=pid,yk_user_id=user_id).values('id')[0]['id']
        Bags.objects.create(
            yk_goods_type=False,
            yk_list_id=None,
            yk_lesson_id=pid,
            yk_price=yk_price,
            yk_user_id=user_id,
            yk_time=None,
            yk_video_progress=0
        )

        result = {
            "code": 0,
            'msg': '已添加至订单中，请跳转支付！！',
            'orderid': num,  # 此参数用作，支付成功后修改相关参数
            'total_price': total_price
        }
    return JsonResponse(result)


# 支付成功后，修改相关参数

def after_buy(request):
    token = request.POST.get('token')  # token验证用户的登陆状态
    num = request.POST.get("lessonId")  # 接收请求体中的nums参数
    user_id = valid_token(token)
    # 修改购物车状态
    bag = Bags.objects.filter(yk_lesson_id=int(num), yk_user_id=user_id,yk_goods_type=False)
    now = time.localtime()
    t62 = time.strftime("%H:%M[:%S[%Y-%m-%d]]", now)
    try:
        bag.update(yk_time=t62,yk_goods_type=True)  #修改一条购物车记录
        result = {
            'code': 0,
            'msg': '商品已成功购买'
        }
    except:
        result = {
            'code': 0,
            'msg': '商品购买失败！'
        }

    return JsonResponse(result)




