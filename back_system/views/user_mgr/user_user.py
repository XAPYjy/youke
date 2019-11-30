from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from tools.db import delete_user
from yk_models.models import YkUser


class UserUserView(View):
    def get(self, request,pagenumber=1):
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
        paginator = Paginator(uusers, 8)  # 每页最多显示8条数据
        if pagenumber > paginator.num_pages:
            pagenumber -= 1
        if pagenumber < 1:
            pagenumber += 1
        uusers = paginator.page(pagenumber)
        return render(request, 'user_mgr/user.html', locals())

    def post(self, request:HttpResponse,pagenumber=1):
        id = request.POST.get("user_id",None)
        print('id=',id)
        name = request.POST.get("name")
        pwd = request.POST.get("password")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        # 验证是否为空（建议：页面上验证）
        if id:
            # 更新
            user = YkUser.objects.get(pk=id)
            user.yk_name = name
            user.yk_auto_string = pwd
            user.yk_emil = email
            user.yk_phone = phone
            user.save()
        else:
            uuser = YkUser.objects.create(yk_name=name,yk_auto_string=make_pwd(pwd),yk_emil=email,yk_phone=phone)
        return redirect('/back/uuser/')

    def delete(self, request):
        uuser_id = request.GET.get('id')
        try:
            user = YkUser.objects.get(id=uuser_id)
            user.delete()
            # delete_user(uuser_id)
        except Exception as e:
            print(e, "=============")
            return JsonResponse({
                'status': 1,
                'msg': '删除失败!'
            })

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



