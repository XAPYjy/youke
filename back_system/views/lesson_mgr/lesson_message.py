from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from yk_models.models import *


class LessonMessageView(View):
    def get(self, request,pagenumber=1):
        if request.GET.get('id',''):
            lesson = YkLesson.objects.get(pk=request.GET.get('id'))
            print('******'*10)
            return  JsonResponse({
                'id': lesson.id,
                'yk_video_jump_link':lesson.yk_video_jump_link,
                'yk_lesson_name':lesson.yk_lesson_name,
                'yk_lesson_price':lesson.yk_lesson_price,
                'yk_lesson_price_type':lesson.yk_lesson_price_type,
                'yk_lesson_dis_price':lesson.yk_lesson_dis_price,
                'yk_teacher_describe':lesson.yk_teacher_describe,
                'yk_lesson_describe':lesson.yk_lesson_describe,
                'yk_lesson_contents':lesson.yk_lesson_contents,
                'yk_lesson_contents_mark':lesson.yk_lesson_contents_mark,
                'yk_lesson_img':lesson.yk_lesson_img,
                'yk_rotaion_id':lesson.yk_rotaion_id,
                'yk_recommend_id':lesson.yk_recommend_id,
                'yk_user_id':lesson.yk_user_id,
                'yk_buy_amount':lesson.yk_buy_amount,
                'yk_watch_amount':lesson.yk_watch_amount,
                'yk_course_chapter':lesson.yk_course_chapter,
                'yk_one_list_id':lesson.yk_one_list_id,
                'yk_tow_list_id':lesson.yk_tow_list_id,
                'yk_class_size':lesson.yk_class_size,
                'yk_lesson_click':lesson.yk_lesson_click,

            })
        lessons = YkLesson.objects.all()
        paginator = Paginator(lessons, 8)  # 每页最多显示8条数据
        if pagenumber > paginator.num_pages:
            pagenumber -= 1
        if pagenumber < 1:
            pagenumber += 1
        lessons = paginator.page(pagenumber)
        return render(request, 'lesson_mgr/message.html', locals())

    def post(self, request:HttpResponse):
        id = request.POST.get("lesson_id",None)
        link = request.POST.get("link")
        name = request.POST.get("name")
        price = request.POST.get("price")
        price_type = request.POST.get("price_type")
        dis_price = request.POST.get("dis_price")
        tdescribe = request.POST.get("tdescribe")
        ldescribe = request.POST.get("ldescribe")
        lcontens = request.POST.get("lcontens")
        lcontens_mark = request.POST.get("lcontens_mark")
        img = request.POST.get("img")
        rotaion_id = request.POST.get("rotaion_id")
        recommend_id = request.POST.get("recommend_id")
        user_id = request.POST.get("user_id")
        buy_amount = request.POST.get("buy_amount")
        watch_amount = request.POST.get("watch_amount")
        course_chapter = request.POST.get("course_chapter")
        one_list_id = request.POST.get("one_list_id")
        tow_list_id = request.POST.get("tow_list_id")
        size = request.POST.get("size")
        click = request.POST.get("click")

        # 验证是否为空（建议：页面上验证）
        if id:
            print('id=',id)
            # 更新
            lesson = YkLesson.objects.get(pk=id)
            lesson.yk_video_jump_link = link
            lesson.yk_lesson_name = name
            lesson.yk_lesson_price = price
            lesson.yk_lesson_price_type = price_type
            lesson.yk_lesson_dis_price = dis_price
            lesson.yk_teacher_describe = tdescribe
            lesson.yk_lesson_describe = ldescribe
            lesson.yk_lesson_contents = lcontens
            lesson.yk_lesson_contents_mark = lcontens_mark
            lesson.yk_lesson_img = img
            lesson.yk_rotaion_id = rotaion_id
            lesson.yk_recommend_id = recommend_id
            lesson.yk_user_id = user_id
            lesson.yk_buy_amount = buy_amount
            lesson.yk_watch_amount = watch_amount
            lesson.yk_course_chapter = course_chapter
            lesson.yk_one_list_id = one_list_id
            lesson.yk_tow_list_id = tow_list_id
            lesson.yk_class_size = size
            lesson.yk_lesson_click = click
            lesson.save()
        else:
            lesson = YkLesson.objects.create(yk_video_jump_link=link,yk_lesson_name=name,
                                             yk_lesson_price=price,yk_lesson_price_type=price_type,
                                             yk_lesson_dis_price=dis_price,yk_teacher_describe = tdescribe,
                                             yk_lesson_describe=ldescribe,yk_lesson_contents = lcontens,
                                             yk_lesson_contents_mark=lcontens_mark,yk_lesson_img = img,
                                             yk_rotaion_id=rotaion_id,yk_recommend_id = recommend_id,
                                             yk_user_id=user_id,yk_buy_amount = buy_amount,yk_watch_amount = watch_amount,
                                             yk_course_chapter=course_chapter,yk_one_list_id = one_list_id,
                                             yk_tow_list_id=tow_list_id,yk_class_size = size,
                                             yk_lesson_click=click )
        return redirect('/back/lmessage/')

    def delete(self, request):
        lesson_id = request.GET.get('id')
        lessonid = YkFirstclass.objects.get(pk=lesson_id)
        lessonid.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })






