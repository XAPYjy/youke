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
        # usid = request.POST.get('token')
        # user_id = valid_token(usid)
        # pids = request.POST.get('lessonId')
        #
        # print('pids=',pids)
        # print('type(pids)=',type(pids))
        global pids
        json_data = req2json(request)
        if json_data == 1:
            result = {
                'error':2,
                'msg':'没有课程数据，不能点击购买！'
            }
            return JsonResponse(result)

        token = json_data.get('token')  # token验证用户的登陆状态
        print('token', token)
        user_id = valid_token(token)
        if not token:
            return JsonResponse({
                'code': 1,
                'msg': '未登录,请重新登陆'})
        pids = json_data.get('lessonId')
        if not pids:
            return JsonResponse({
                'code': 3,
                'msg': '未选择商品是不能点击购买的吆~~~'
            })
        carts = YkOrder.objects.filter(yk_user_id=user_id)  #查询该登录用户的订单信息
        print('carts=',carts)
        discount = YkWallet.objects.filter(yk_user_id=user_id).values('yk_discount')[0]['yk_discount']
        print('discount=', discount)
        if carts:  #用户产生过订单
            goodsid = carts.values_list('yk_goods_id')  # 查询该用户的订单信息内的所有商品id
            # 创建所有商品id的列表order_list
            order_list = []
            for i in goodsid:
                i = i[0].lstrip('[').rstrip(']').split(',')
                print('i=', i)
                for j in i:
                    j = j.strip(' \'')
                    print(j)
                    print('type(j)=',type(j))
                    order_list.append(int(j))
            total_price = 0
            nums = []
            print('type(pids)', type(pids))
            print('pids=', pids)
            if len(pids) <= 6:  # 单个订单单个商品的商品id
                pids = pids.lstrip('[').rstrip(']')
                pids = int(pids)
                print('单个订单单个商品的商品id',pids)
                if pids in order_list:
                    lesson = YkLesson.objects.filter(id=pids)[0]
                    order = carts.filter(yk_goods_id__contains=pids)
                    if order.filter(yk_isorderstatus=False).first():
                        ordernums = order.values('id')[0]['id']
                        print(ordernums)
                        total_price = round(order.values('yk_total_price')[0]['yk_total_price'] * float(discount),2)
                        print(total_price)
                        result = {
                            "code": 0,
                            'msg': '已添加至订单中，请跳转支付！！',
                            'orderId': ordernums,  # 此参数用作，支付成功后修改相关参数
                            'total_price': total_price
                        }
                    else:
                        result = {
                            "code": 0,
                            "msg": str(lesson.yk_lesson_name) + "已存在购物车中，请勿重新添加！！！"
                        }
                else:
                    lesson = YkLesson.objects.filter(id=pids).values_list('yk_lesson_price')[0][0]
                    print(lesson)
                    total_price = round(lesson * float(discount),2)
                    one = Bags.objects.filter(yk_lesson_id=pids)

                    if not one.filter(yk_goods_type=False).first():
                        Bags.objects.create(
                            yk_goods_type=False,
                            yk_list_id=None,
                            yk_lesson_id=int(pids),
                            yk_price=lesson,
                            yk_user_id=user_id,
                            yk_time=None,
                            yk_video_progress=0
                        )
                    YkOrder.objects.create(yk_goods_id=[pids],
                                           yk_total_price=total_price,
                                           yk_isorderstatus=None,
                                           yk_user_id=user_id)
                    order = carts.filter(yk_goods_id__contains=pids)
                    ordernums = order.values('id')[0]['id']
                    print('ordernums=',ordernums)
                    result = {
                        "code": 0,
                        'msg': '已添加至订单中，请跳转支付！！',
                        'orderId': ordernums,  # 此参数用作，支付成功后修改相关参数
                        'total_price': total_price
                    }
                return JsonResponse(result)
            else:  # 单个订单多个商品的模式
                pids = pids.lstrip('[').rstrip(']').split(',')
                print('175单个订单多个商品的模式',pids)
                for pid in pids:
                    print('177单个订单多个商品的模式',pid)
                    pid = int(pid)
                    nums.append(pid)
                    if pid in order_list:
                        lessonname = YkLesson.objects.filter(id=pid).values('yk_lesson_name')[0]
                        result = {
                            "code": 0,
                            "msg": str(lessonname['yk_lesson_name']) + "已存在购物车中，请勿重新添加！！！"
                        }
                        return JsonResponse(result)
                    else:
                        yk_price = round(YkLesson.objects.filter(id=pid).values_list('yk_lesson_price')[0][0] * float(
                            discount),2)
                        total_price += yk_price
                        lesson = YkLesson.objects.filter(id=pid).values_list('yk_lesson_price')[0][0]
                        one = Bags.objects.filter(yk_lesson_id=pid)

                        if not one.filter(yk_goods_type=False).first():
                            Bags.objects.create(
                                yk_goods_type=False,
                                yk_list_id=None,
                                yk_lesson_id=int(pid),
                                yk_price=lesson,
                                yk_user_id=user_id,
                                yk_time=None,
                                yk_video_progress=0
                            )
                YkOrder.objects.create(yk_goods_id=nums,
                                       yk_total_price=round(total_price, 2),
                                       yk_isorderstatus=None,
                                       yk_user_id=user_id)

                ordernums = YkOrder.objects.filter(yk_goods_id=nums, yk_user_id=user_id).values('id')[0]['id']

                result = {
                    "code": 0,
                    'msg': '已添加至订单中，请跳转支付！！',
                    'orderId': ordernums,  # 此参数用作，支付成功后修改相关参数
                    'total_price': round(total_price, 2)
                }
        else:
            # 订单信息为空！
            total_price = 0
            if len(pids) <= 8:  # 单个订单单个商品的商品id
                pids = pids.lstrip('[').rstrip(']')
                one = Bags.objects.filter(yk_lesson_id=pids)
                print('----')
                print('type(pids)',type(pids))
                discount = YkWallet.objects.filter(yk_user_id=user_id).values('yk_discount')[0]['yk_discount']
                print('discount=', discount)
                lesson = YkLesson.objects.filter(id=pids).values_list('yk_lesson_price')[0][0]
                print(lesson)
                yk_price = round(lesson * float(discount),2)
                total_price = yk_price
                if not one.filter(yk_goods_type=False).first():
                    Bags.objects.create(
                        yk_goods_type=False,
                        yk_list_id=None,
                        yk_lesson_id=int(pids),
                        yk_price=yk_price,
                        yk_user_id=user_id,
                        yk_time=None,
                        yk_video_progress=0
                    )
                    pids = [pids]
            else:  # 单个订单多个商品的模式
                pids = pids.lstrip('[').rstrip(']').split(',')
                print('去除[]分割多个pids中间的,pids=', pids)
                print('单个订单多个商品的模式pids=',pids)
                for pid in pids:
                    pid = int(pid)
                    print('客户没有买过订单且是单订单多商品下pid=',pid)
                    discount = YkWallet.objects.filter(yk_user_id=user_id).values('yk_discount')[0]['yk_discount']
                    print('discount=', discount)
                    yk_price = YkLesson.objects.filter(id=pid).values_list('yk_lesson_price')[0][0]
                    pay_price = round(yk_price * float(discount),2)
                    total_price += pay_price
                    one = Bags.objects.filter(yk_lesson_id=pid)
                    if not one.filter(yk_goods_type=False).first():
                        Bags.objects.create(
                            yk_goods_type=False,
                            yk_list_id=None,
                            yk_lesson_id=int(pid),
                            yk_price=yk_price,
                            yk_user_id=user_id,
                            yk_time=None,
                            yk_video_progress=0
                        )
            # 判断用户是否在购物车添加过正在购买的商品！，没有添加则创建购物车信息
            YkOrder.objects.create(yk_goods_id=pids,
                                   yk_total_price=round(total_price,2),
                                   yk_isorderstatus=None,
                                   yk_user_id=user_id)

            ordernums = YkOrder.objects.filter(yk_goods_id=pids, yk_user_id=user_id).values('id')[0]['id']

            result = {
                "code": 0,
                'msg': '已添加至订单中，请跳转支付！！',
                'orderId': ordernums,  # 此参数用作，支付成功后修改相关参数
                'total_price': round(total_price,2)
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
        global result
        # token = request.POST.get('token')
        # num = request.POST.get('orderId')
        json_data = req2json(request)
        token = json_data.get('token')  # token验证用户的登陆状态
        user_id = valid_token(token)
        print('token', token)
        num = json_data.get("orderId")  # 接收请求体中的orderid参数
        print('num=',num)
        if not token:
            print("没有接收到token")
            return JsonResponse({"1111": "没有接收到！"})
        try:
            user_id = valid_token(token)
        except:
            print('没有登录！')
            return JsonResponse({"1111": "没有接收到！"})
        goodsid = YkOrder.objects.filter(id=num, yk_user_id=user_id).values('yk_goods_id')[0]['yk_goods_id']
        print('type(goodsid=)', type(goodsid))
        print('251行的goodsid=',goodsid)
        now = time.localtime()
        t62 = time.strftime("%Y-%m-%d %H:%M:%S", now)
        if len(goodsid) >= 2:  #多个商品的订单处理
            goodsid = goodsid.lstrip('[').rstrip(']').split(',')
            print('type(goodsid=)', type(goodsid))
            print(2)
        else:   #单个商品的订单处理！
            print(1)
            goodsid = int(goodsid.lstrip('[\'').rstrip(']\''))
            bag = Bags.objects.filter(yk_lesson_id=goodsid, yk_user_id=user_id).first()
            print('单个的bag=', bag)
            bag.yk_time = t62
            bag.yk_goods_type = True
            bag.save()
            # 修改一条订单记录
            order_or = YkOrder.objects.filter(id=num).first()
            print('单个的order_or=', order_or)
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
            return JsonResponse(result)
        for g in range(len(goodsid)):
            goodid = goodsid[g].strip(' \'')
            print('goodid=',goodsid)
            goodid = int(goodid)
            try:
                # 修改一条购物车记录
                print("22222")
                bag = Bags.objects.filter(yk_lesson_id=goodid, yk_user_id=user_id).first()
                print('循环的bag=',bag)
                bag.yk_time = t62
                bag.yk_goods_type = True
                bag.save()
                # 修改一条订单记录

            except Exception as e:
                result = {
                    'code': 1,
                    'msg': '商品购买失败！'
                }
                print(e)
        order_or = YkOrder.objects.filter(id=num).first()
        print('order_or=', order_or)
        order_or.yk_isorderstatus = True
        order_or.yk_order_time = t62
        order_or.save()
        carts = Bags.objects.filter(yk_user_id=user_id, yk_goods_type=False).all()  # 查询登录用户的所有未购买商品
        list_cart_id = []
        # 循环出所有登录用户的未购买购物记录,并添加到列表

        for cart in carts:
            print('cart=', cart)
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

#删除未购买!
def delesson(request):
    if request.method == "POST":
        # token = request.POST.get('token')
        # pid = int(request.POST.get('lessonId').lstrip('[').rstrip(']'))
        json_data = req2json(request)
        token = json_data.get('token')  # token验证用户的登陆状态
        print('token', token)
        pid = int(json_data.get('lessonId'))
        if not token:
            return JsonResponse({
                'code': 1,
                'msg': '未登录,请重新登陆'})
        if not pid:
            return JsonResponse({
                'code': 1,
                'msg': '还未选择商品！'
            })
        user_id = valid_token(token)
        print('pid=',pid)
        print(type(pid))
        bag = Bags.objects.filter(yk_user_id=user_id, yk_lesson_id=pid, yk_goods_type=False)  # .first()
        if bag:
            print('bag=',bag)
            bag.delete()
            buys = Bags.objects.filter(yk_user_id=user_id, yk_goods_type=False)  # 查询登录用户的所有购物车记录
            list_buy_id = []  # 循环出所有登录用户的购物记录,并添加到列表
            for buy in buys:
                list_buy_id.append(buy.yk_lesson_id)
            list_id = []
            for i in list_buy_id:
                yk_video_progress = \
                Bags.objects.filter(yk_user_id=user_id, yk_lesson_id=i).values('yk_video_progress')[0][
                    'yk_video_progress']
                carts1 = \
                    YkLesson.objects.filter(id=i).values('id', 'yk_lesson_name', 'yk_course_chapter', 'yk_lesson_price',
                                                         'yk_lesson_img')[0]
                carts1['videoProgress'] = yk_video_progress
                list_id.append(carts1)
            # 将数据返回给前端
            result = {
                "code": 0,
                "msg": "课程删除成功！",
                'wgm': list_id,
            }
        else:
            result = {
                'error':0,
                'msg':'删除失败，不能没有课程id'
            }
        return JsonResponse(result)