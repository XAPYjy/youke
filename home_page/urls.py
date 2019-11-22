from django.urls import path
from home_page.views import home_view,search_view

urlpatterns = [
    path('home/', home_view),
    path('search/',search_view)
]