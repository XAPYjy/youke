from django.contrib import admin
from django.urls import path, include
from ykuser.urls import router_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('back_system.urls', namespace='bk')),
    path('youke/', include(router_user.urls)),

]
