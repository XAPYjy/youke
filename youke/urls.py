import os

from django.http import HttpResponse
from django.urls import path, include

from cart.urls import *
from ykuser.urls import router_user

# 显示头像图片


def image_head_view(request, image):
    UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
    imagepath = os.path.join(UPLOAD_DIR, "statics/head", image)  # 拼接上传文件的最终路径
    image_data = open(imagepath, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg | image/png | image/bmp| image/tif |image/gif")



# 显示视频图片
def image_video_view(request, image_url):
    UPLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 返回到上级目录
    imagepath = os.path.join(UPLOAD_DIR, "statics/video_img/", image_url)  # 拼接上传文件的最终路径
    image_data = open(imagepath, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg | image/png | image/bmp| image/tif |image/gif")


from django.urls import path, include
from ykuser.urls import router_user

urlpatterns = [
    path('youke/', include('home_page.urls')),  # 首页路由
    path('youke/lesson/', include('lesson_page.urls')),  # 课程详情页路由
    path('back/', include('back_system.urls', namespace='bk')),  # 后台管理路由
    path('image/<image>/', image_head_view),  # 查询头像图片路由
    path('video_img/<image_url>/', image_video_view),  # 查看视频图片路由
    path('youke/', include(router_user.urls)),  # 我的页面路由
    path('video/', include("video_rtmp.urls")),  # 课程视频路由
    path('cart/',include('cart.urls')),
    path('gate/',include('class_ls.urls'))
]





