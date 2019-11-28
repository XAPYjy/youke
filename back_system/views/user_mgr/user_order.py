from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from yk_models.models import *


class UserOrderView(View):
    def get(self, request):
        if request.GET.get('id',''):
            order = YkOrder.objects.get(pk=request.GET.get('id'))
            return  JsonResponse({
                'id':order.id,
                'goods_id':order.yk_goods_id,
                'status':order.yk_isorderstatus,
                'total_price':order.yk_total_price,
                'user_id':order.yk_user_id,
            })

        orders = YkOrder.objects.all()
        return render(request, 'user_mgr/order.html', locals())

    def delete(self, request):
        suser_id = request.GET.get('id')
        suser = SysUser.objects.get(pk=suser_id)
        suser.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })



