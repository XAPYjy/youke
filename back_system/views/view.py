from django.db import models
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from yk_models.models import *


class BaseView(View):
    def get(self, request,pagenumber=1):
        model_name = request.GET.get('name')
        model_cls: models.Model = eval(model_name)
        datas = model_cls.objects.all()
        fields = model_cls._meta.fields

        #  分页
        paginator = Paginator(datas, 3)  # 每页最多显示三条数据
        if pagenumber > paginator.num_pages:
            pagenumber -= 1
        if pagenumber < 1:
            pagenumber += 1
        page = paginator.page(pagenumber)

        fields = model_cls._meta.fields

        return render(request, 'base_list.html', locals())

