from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from yk_models.models import *


class LessonFirstView(View):
    def get(self, request):
        if request.GET.get('id',''):
            firstlist = YkFirstclass.objects.get(pk=request.GET.get('id'))
            print('firstlist=',firstlist)
            return JsonResponse({
                'id':firstlist.id,
                'firstid':firstlist.yk_firstclassid,
                'firstname':firstlist.yk_firstclassname
            })
            firstlists =YkFirstclass.objects.all()
            print('firstlists=',firstlists)
        return render(request, 'lesson_mgr/firstlist.html', locals())

    def post(self, request:HttpResponse):
        id = request.POST.get('first_id')
        firstid = request.POST.get("firstlist_id",None)
        firstname = request.POST.get("name")
        # 验证是否为空（建议：页面上验证）
        if id:
            # 更新

            firstlist = YkFirstclass.objects.get(pk=id)
            firstlist.yk_firstclassid = firstid
            firstlist.yk_firstclassname = firstname
            firstlist.save()
        else:
            firstlist = YkFirstclass.objects.create(yk_firstclassid=firstid,yk_firstclassname=firstname)
        return redirect('/back/lfirst/')

    def delete(self, request):
        firstlist_id = request.GET.get('id')
        firstlist = YkFirstclass.objects.get(pk=firstlist_id)
        firstlist.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



