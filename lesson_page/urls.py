from django.urls import path
from lesson_page.views import *

urlpatterns = [
    path('detail', detail_view),
    path('detail/discuss',discuss_view),
    path('detail/add2cart',add2cart),
    #path('detail/buy_lesson',buy_lesson),
    #path('detail/after_buy',after_buy)
]