from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from back_system.common import make_pwd
from yk_models.models import *


class TotalOrderView(View):
    def get(self,request):
        return render(request,'total_mgr/order_total.html')