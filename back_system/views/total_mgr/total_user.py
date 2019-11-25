from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from back_system.models import *


class TotalUserView(View):
    def get(self, request):
        if request.GET.get('id',''):
            suser = SysUser.objects.get(pk=request.GET.get('id'))
            return  JsonResponse({
                'id':suser.id,
                'name':suser.name,
                'auth_string':suser.auth_string,
                'email':suser.email,
                'phone':suser.phone
            })
        susers = SysUser.objects.all()
        return render(request, 'total_mgr/user_total.html', locals())

    def post(self, request:HttpResponse):
        id = request.POST.get("suser_id",None)
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        # 验证是否为空（建议：页面上验证）
        if id:
            # 更新
            suser = SysUser.objects.get(pk=id)
            suser.name = name
            suser.auth_string = pwd
            suser.email = email
            suser.phone = phone
            suser.save()
        else:
            suser = SysUser.objects.create(name=name,auth_string=make_pwd(pwd),email=email,phone=phone)
        return redirect('/tuser/')

    def delete(self, request):
        suser_id = request.GET.get('id')
        suser = SysUser.objects.get(pk=suser_id)
        suser.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



