from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from yk_models.models import *


class LessonSecondView(View):
    def get(self, request):
        if request.GET.get('id',''):
            secondlist = YkSecondclass.objects.get(pk=request.GET.get('id'))
            return  JsonResponse({
                'id':secondlist.id,
                'secondid':secondlist.yk_secondclassid,
                'secondname':secondlist.yk_secondclassname,
                'firstid':secondlist.yk_firstclassid,
                'image':secondlist.secondimage,
                'url':secondlist.secondurl
            })
            secondlists = YkSecondclass.objects.all()
        return render(request, 'lesson_mgr/secondlist.html', locals())

    def post(self, request:HttpResponse):
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



