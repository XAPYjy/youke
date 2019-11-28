from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from yk_models.models import YkUser


class UserUserView(View):
    def get(self, request):
        if request.GET.get('id',''):
            uuser = YkUser.objects.get(pk=request.GET.get('id'))
            print('uuser=',uuser)
            return  JsonResponse({
                'id':uuser.id,
                'yk_name':uuser.yk_name,
                'yk_auto_string':uuser.yk_auto_string,
                'yk_emil':uuser.yk_emil,
                'yk_phone':uuser.yk_phone,
            })
        uusers = YkUser.objects.all()
        return render(request, 'user_mgr/user.html', locals())

    def post(self, request:HttpResponse):
        id = request.POST.get("uuser_id",None)
        print('id=',id)
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        # 验证是否为空（建议：页面上验证）
        if id:
            # 更新
            uuser = YkUser.objects.get(pk=id)
            print('uuser=',uuser)
            uuser.yk_name = name
            uuser.yk_auto_string = pwd
            uuser.yk_emil = email
            uuser.yk_phone = phone
            uuser.save()
        else:
            uuser = YkUser.objects.create(yk_name=name,yk_auto_string=make_pwd(pwd),yk_emil=email,yk_phone=phone)
        return redirect('/back/uuser/')

    def delete(self, request):
        uuser_id = request.GET.get('id')
        print('uuser_id=',uuser_id)
        uuser = YkUser.objects.get(pk=uuser_id)
        uuser.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



