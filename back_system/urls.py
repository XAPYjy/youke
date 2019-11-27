from django.urls import path
from back_system.views.sys_mgr.sys_mgr_user import SUserView
from back_system.views.sys_mgr.sys_mgr_role import SRoleView
from back_system.views.user_mgr.user_order import UserOrderView
from back_system.views.user_mgr.user_user import UserUserView
from back_system.views.lesson_mgr.lesson_message import LessonMessageView
from back_system.views.lesson_mgr.lesson_firstlist import LessonFirstView
from back_system.views.lesson_mgr.lesson_secondlist import LessonSecondView
from back_system.views.total_mgr.total_lesson import TotalLessonView
from back_system.views.total_mgr.total_order import TotalOrderView
from back_system.views.total_mgr.total_user import TotalUserView
from back_system.views.view import BaseView

from back_system.views.views import *

app_name = "back_system"

urlpatterns = [
    path(r'',index_view,name='in'),
    path('login/',login_view,name='lg'),
    path('logout/',logout_view,name='lo'),
    path('role/', SRoleView.as_view(),name='ro'),
    path('syuser/',SUserView.as_view(),name='su'),
    path('uuser/',UserUserView.as_view(),),
    path('uorder/',UserOrderView.as_view(),),
    path('lfirst/',LessonFirstView.as_view(),),
    path('lsecond/',LessonSecondView.as_view(),),
    path('lmessage/',LessonMessageView.as_view(),),
    path('tlesson/', TotalLessonView.as_view(), ),
    path('torder/',TotalOrderView.as_view(), ),
    path('tuser/',TotalUserView.as_view(), ),
    path('init_es/', ESView.as_view()),
    path('upload_log/', ESLogView.as_view()),
    path('base/',BaseView.as_view()),
]
