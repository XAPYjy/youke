from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from yk_models.models import *


class LessonSecondView(View):
    def get(self, request,pagenumber=1):
        if request.GET.get('id',''):
            secondlist = YkSecondclass.objects.get(pk=request.GET.get('id'))
            return  JsonResponse({
                'id':secondlist.id,
                'yk_secondclassid':secondlist.yk_secondclassid,
                'yk_secondclassname':secondlist.yk_secondclassname,
                'yk_firstclassid':secondlist.yk_firstclassid,
                'secondimage':secondlist.secondimage,
                'secondurl':secondlist.secondurl
            })
        secondlists = YkSecondclass.objects.all()
        paginator = Paginator(secondlists, 8)  # 每页最多显示8条数据
        if pagenumber > paginator.num_pages:
            pagenumber -= 1
        if pagenumber < 1:
            pagenumber += 1
            firstlists = paginator.page(pagenumber)
        return render(request, 'lesson_mgr/secondlist.html', locals())

    def post(self, request:HttpResponse):
        id = request.POST.get("second_id",None)
        secondid = request.POST.get("secondlist_id",None)
        name = request.POST.get("name")
        first_id = request.POST.get("first_id")
        image = request.POST.get("image")
        url = request.POST.get("url")
        # 验证是否为空（建议：页面上验证）
        if id:
            # 更新
            secondlist = YkSecondclass.objects.get(pk=id)
            secondlist.yk_secondclassid = secondid
            secondlist.yk_secondclassname = name
            secondlist.yk_firstclassid = first_id
            secondlist.secondimage = image
            secondlist.secondurl = url
            secondlist.save()
        else:
            secondlist = YkSecondclass.objects.create(yk_secondclassid=secondid,
                                                      yk_secondclassname=name,
                                                      yk_firstclassid=first_id,
                                                      secondimage=image, secondurl=url)
        return redirect('/back/lmessage/')

    def delete(self, request):
        secondelist_id = request.GET.get('id')
        secondelist = YkFirstclass.objects.get(pk=secondelist_id)
        secondelist.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



