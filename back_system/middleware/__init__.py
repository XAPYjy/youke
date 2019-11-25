#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect


def valid_login(view_func):
    not_valid_paths = ['/logout/',"/role/",'/syuser/','/uuser/','/uorder/','/lfirst/','/lsecond/','/lmessage/','/llist/','/tlesson/','/torder/','/tuser/','/init_es/','/upload_log/']

    def wrapper(request: HttpRequest, *args, **kwargs):
        if 'login_user'  in request.session.keys() and request.path  in not_valid_paths:
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper