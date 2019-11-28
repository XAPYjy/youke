from rest_framework.routers import SimpleRouter
#from cart.views import CartViewSet

#cart_router = SimpleRouter()
#cart_router.register(r'cart',CartViewSet)
from django.urls import path
from cart.views import *

urlpatterns = [
    path('get_cart', get_cart),
    path('buy_lesson',buy_lesson),
    path('after_buy',after_buy),
    path('bag',My_Bought)
]