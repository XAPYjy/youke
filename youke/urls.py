import os

from django.http import HttpResponse
from django.urls import path, include

from cart.urls import *
from ykuser.urls import router_user

# 显示图片
def image_head_view(request, image):
    UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
    imagepath = os.path.join(UPLOAD_DIR, "statics/head", image)  # 拼接上传文件的最终路径
    image_data = open(imagepath, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg | image/png | image/bmp| image/tif |image/gif")


urlpatterns = [
    path('youke/', include('home_page.urls')),
    path('youke/lesson/', include('lesson_page.urls')),
    path('back/', include('back_system.urls', namespace='bk')),
    path('image/<image>/', image_head_view),  # 查询图片路由
    path('youke/', include(router_user.urls)),
    #path('cart/', include(cart_router.urls))
    path('cart/',include('cart.urls'))
]
