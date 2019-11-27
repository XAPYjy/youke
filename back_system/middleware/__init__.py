#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect


def valid_login(view_func):
    not_valid_paths = ['/back/login/', '/back/regist/', '/back/upload_log/','/back/logout/']

    def wrapper(request: HttpRequest, *args, **kwargs):
        if 'login_user' not in request.session.keys() and request.path not in not_valid_paths:
            return redirect('bk:lg')

        return view_func(request, *args, **kwargs)
    return wrapper