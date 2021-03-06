from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd, es_

from django.db import connection

from yk_models.models import SysUser


def index_view(request: HttpRequest):
    return render(request, 'index.html')


def login_view(request: HttpRequest):
    if request.method == "POST":
        # 获取用户名和口令
        logname = request.POST.get('logname', '')
        logpwd = request.POST.get('logpwd', '')
        print(logname, logpwd)
        if any((not logname, not logpwd, len(logname) == 0, len(logpwd) == 0)):
            error = '用户名或密码不能为空！'
        else:
            ret = SysUser.objects.filter(name=logname, auth_string=make_pwd(logpwd))
            print(ret)
            if ret:
                login_user = ret.first()

                # 将登录的用户信息存到session中
                request.session['login_user'] = {
                    'id': login_user.id,
                    'name': login_user.name,
                    'role_name': login_user.role.name,
                    'role_code': login_user.role.code
                }
                return redirect('/back/')
            error = '用户名或密码错误！'
    return render(request, 'login.html', locals())


# def register_view(request: HttpRequest):
#     return render(request, 'register.html')


def logout_view(request: HttpRequest):
    request.session.pop('login_user')
    return redirect('/back/login/')


class ESView(View):
    def get(self, request):
        # 同步ES（初始化）
        es_.create_index()

        cursor = connection.cursor()
        cursor.execute('select * from mysql.sys_role')
        for row in cursor.fetchall():
            print(row)

        return JsonResponse({
            'status': 0,
            'msg': '同步ElasticSearch搜索引擎成功'
        })


class ESLogView(View):
    def post(self, request):
        data = request.POST
        print(data)

        return JsonResponse({
            'status': 0,
            'msg': '上传日志成功'
        })
