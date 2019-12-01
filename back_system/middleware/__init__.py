#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect


def valid_login(view_func):
    not_valid_paths = ['/back/','/back/role/','/back/syuser/','/back/uuser/','/back/uuser/<int:pagenumber>/',
                       '/back/uorder/','/back/uorder/<int:pagenumber>/','/back/lfirst/',
                       '/back/lfirst/<int:pagenumber>/','/back/lsecond/','/back/lsecond/<int:pagenumber>/',
                       '/back/lmessage/','/back/lmessage/<int:pagenumber>/','/back/tlesson/','/back/torder/',
                       '/back/tuser/','/back/upload_log/','/back/init_es/','/back/video/<video_url>/']

    def wrapper(request: HttpRequest, *args, **kwargs):
        if request.path  in not_valid_paths and'login_user' not in request.session.keys():
            return redirect('bk:lg')

        return view_func(request, *args, **kwargs)
    return wrapper