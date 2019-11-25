from django.urls import path, include

urlpatterns = [
    path(r'', include('back_system.urls', namespace='bk')),
]
