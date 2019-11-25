from django.urls import path
from lesson_page.views import *

urlpatterns = [
    path('detail', detail_view),
    path('detail/discuss',discuss_view)
]