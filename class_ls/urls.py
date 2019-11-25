from django.contrib import admin
from django.urls import path, include

from class_ls.views import *

urlpatterns = [
    path('all_/',first_class), #分类界面路由
    # path('second/',second_class),
    path('lesson/',lesson_list), #
    path('sort/',sort_lesson)
]