import time
from django.http import JsonResponse
from tools.request2json import req2json
from yk_models.models import YkWallet, Bags, YkLesson, YkOrder,YkUser
from tools.cache_ import valid_token



# def total_prices(self,request, uid):
#     uid = request.GET.get('uid')
#     carts = Bags.objects.filter(yk_user_id=uid, yk_goods_type=False)
#     discount = YkWallet.objects.filter(yk_user_id=uid).values_list("yk_discount")[0]
#     total = 0
#     for c in carts:
#         if discount:
#             total += c.yk_price * 0.8
#         elsyk_discusse:
#             total += c.yk_price
#     return "{:.2f}".format(total)


# 当点击购物车按钮，遍历出未购买商品并返回给前端
def get_cart(request):
    if request.method == 'POST':
        json_data = req2json(request)
        token = json_data.get('token')  # token验证用户登陆状态
        print(token)
        try:
            user_id = valid_token(token)
        except:
            return JsonResponse({
                'code': 1,
                'msg': '未登录,请重新登陆'})
        uname = YkUser.objects.filter(id=user_id).values('yk_name')[0]['yk_name']
        discount = YkWallet.objects.filter(yk_user_id=user_id).values('yk_discount')[0]['yk_discount']
        discount = int(float(discount) * 100)
        # if not user_id:
        #     return JsonResponse({
        #         'code': 1,
        #         'msg':'未登录,请重新登陆'})

        carts = Bags.objects.filter(yk_user_id=user_id, yk_goods_type=False)  # 查询登录用户的所有未购买商品
        list_cart_id = []
        # 循环出所有登录用户的未购买购物记录,并添加到列表
        for cart in carts:
            list_cart_id.append(cart.yk_lesson_id)
        list_id = []
        for i in list_cart_id:
            carts1 = \
            YkLesson.objects.filter(id=i).values('id', 'yk_lesson_name', 'yk_course_chapter', 'yk_lesson_price',
                                                 'yk_lesson_img')[0]
            list_id.append(carts1)

        # 将数据返回给前端
        result = {
            'code': 0,
            'uname': uname,
            'discount': discount,
            'wgm': list_id
        }
    else:
        result = {
            'error': 2,
            'msg': '请求方式不对，请正确访问！！！'
        }
    return JsonResponse(result)

# 前端页面点击 点击购买按钮，可能携带商品id列表
def buy_lesson(request):
    if request.method == 'POST':
        json_data = req2json(request)
        if json_data == 1:
            result = {
                'error':2,
                'msg':'没有课程数据，不能点击购买！'
            }
            return JsonResponse(result)

        token = json_data.get('token')  # token验证用户的登陆状态
        print('token', token)

        if not token:
            return JsonResponse({
                'code': 1,
                'msg': '未登录,请重新登陆'})
        pids = list(json_data.get('pid'))
        if not pids:
            return JsonResponse({
                'code': 3,
                'msg': '未选择商品是不能点击购买的吆~~~'
            })
        user_id = valid_token(token)
        carts = YkOrder.objects.filter(yk_user_id=user_id).values_list('yk_goods_id')
        order_list = []
        nums = []
        for i in carts:
            order_list.append(i[0])
        total_price = 0
        for pid in pids:
            pid = int(pid)
            if pid in order_list:
                lessonname = YkLesson.objects.filter(id=pid).values('yk_lesson_name')[0]
                result = {
                    "code": 0,
                    "msg": str(lessonname['yk_lesson_name']) + "已存在订单中，请勿重新添加！！！"
                }
                return JsonResponse(result)
            else:
                yk_price = YkLesson.objects.filter(id=pid).values_list('yk_lesson_price')[0][0] * float(
                    YkWallet.objects.filter(yk_user_id=user_id).values('yk_discount')[0]['yk_discount'])
                total_price += yk_price
                YkOrder.objects.create(yk_goods_id=pid,
                                       yk_total_price=total_price,
                                       yk_isorderstatus=None,
                                       yk_user_id=user_id)
                num = YkOrder.objects.filter(yk_goods_id=pid, yk_user_id=user_id).values('id')[0]['id']
                nums.append(num)

        result = {
            "code": 0,
            'msg': '已添加至订单中，请跳转支付！！',
            'orderid': nums,  # 此参数用作，支付成功后修改相关参数
            'total_price': total_price
        }
    else:
        result = {
            'error': 2,
            'msg': '请求方式不对，请正确访问！！！'
        }

    return JsonResponse(result)


# 支付成功后，修改相关参数

def after_buy(request):
    if request.method == "POST":
        json_data = req2json(request)
        token = json_data.get('token')  # token验证用户的登陆状态
        print('token', token)
        num = json_data.get("orderid")  # 接收请求体中的orderid参数
        print(num)
        if not token:
            print("没有接收到token")
            return JsonResponse({"1111": "没有接收到！"})
        try:
            user_id = valid_token(token)
        except:
            print('没有登录！')
            return JsonResponse({"1111": "没有接收到！"})
        goodsid = list(YkOrder.objects.filter(id=num, yk_user_id=user_id).values('yk_goods_id')[0]['yk_goods_id'])
        print(goodsid)
        for goodid in goodsid:
            global result
            bag = Bags.objects.filter(yk_lesson_id__in=goodid, yk_user_id=user_id)
            now = time.localtime()
            t62 = time.strftime("%Y-%m-%d %H:%M:%S", now)
            try:
                bag.update(yk_time=t62, yk_goods_type=True)  # 修改一条购物车记录
                order_or = YkOrder.objects.filter(id=num).first()
                order_or.yk_isorderstatus = True
                order_or.yk_order_time = t62
                order_or.save()
                carts = Bags.objects.filter(yk_user_id=user_id, yk_goods_type=False)  # 查询登录用户的所有未购买商品
                list_cart_id = []
                # 循环出所有登录用户的未购买购物记录,并添加到列表
                for cart in carts:
                    list_cart_id.append(cart.yk_lesson_id)
                list_id = []
                for i in list_cart_id:
                    carts1 = \
                        YkLesson.objects.filter(id=i).values('id', 'yk_lesson_name', 'yk_course_chapter',
                                                             'yk_lesson_price',
                                                             'yk_lesson_img')[0]
                    list_id.append(carts1)

                result = {
                    'code': 0,
                    'msg': '商品已成功购买',
                    'wgm': list_id
                }
            except:
                result = {
                    'code': 1,
                    'msg': '商品购买失败！'
                }
    else:
        result = {
            'error': 2,
            'msg': '请求方式不对，请正确访问！！！'
        }
    return JsonResponse(result)

# 已购买接参
def My_Bought( request):
    if request.method == 'POST':
        json_data = req2json(request)
        uid = json_data.get('token')  # token验证用户的登陆状态
        print('token', uid)

        if not uid:
            return JsonResponse({
                'code': 1,
                'msg': '未登录,请重新登陆'})
        user_id = valid_token(uid)
        buys = Bags.objects.filter(yk_user_id=user_id, yk_goods_type=True)  # 查询登录用户的所有购物车记录
        list_buy_id = []  # 循环出所有登录用户的购物记录,并添加到列表
        for buy in buys:
            list_buy_id.append(buy.yk_lesson_id)
        list_id = []
        for i in list_buy_id:
            yk_video_progress = Bags.objects.filter(yk_user_id=user_id, yk_lesson_id=i).values('yk_video_progress')[0][
                'yk_video_progress']
            carts1 = \
            YkLesson.objects.filter(id=i).values('id', 'yk_lesson_name', 'yk_course_chapter', 'yk_lesson_price',
                                                 'yk_lesson_img')[0]
            carts1['videoProgress'] = yk_video_progress
            list_id.append(carts1)
        # 将数据返回给前端
        result = {
            "code": 0,
            "msg": "课程成功查询",
            'ygm': list_id,
        }
    else:
        result = {
            'error': 2,
            'msg': '请求方式不对，请正确访问！！！'
        }
    return JsonResponse(result)