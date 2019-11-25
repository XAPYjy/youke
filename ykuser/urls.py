from rest_framework.routers import SimpleRouter

from ykuser.views import UserViewSet

router_user = SimpleRouter()
router_user.register(r'auth', UserViewSet)
