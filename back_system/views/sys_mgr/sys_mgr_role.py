from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from back_system.models import *


class SRoleView(View):
    def get(self, request):
        if request.GET.get('id',''):
            role = SysRole.objects.get(pk=request.GET.get('id'))
            return  JsonResponse({
                'id':role.id,
                'name':role.name,
                'code':role.code
            })
        roles = SysRole.objects.all()
        return render(request, 'sys_mgr/role.html', locals())

    def post(self, request:HttpResponse):
        id = request.POST.get("role_id",None)
        name = request.POST.get("name")
        code = request.POST.get("code")
        # 验证是否为空（建议：页面上验证）
        if id:
            # 更新
            role = SysRole.objects.get(pk=id)
            role.name = name
            role.code = code
            role.save()
        else:
            role = SysRole.objects.create(name=name,code=code)

        return redirect('/role/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysRole.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



