from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication


from tools.error import YKException
from ykuser.models import YKUser


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.data.get("token") if request.data.get("token") else request.query_params.get("token")
        user_id = cache.get(token)
        try:
            user = YKUser().select_all(id=user_id)
            return (user, token)   #  返回的该元祖的两个元素会做这样处理，request.user=user,request.auth=token
        except:
            result = {
                "code": 900,
                "msg": "您还没有登陆，请先登陆"
                }
        raise YKException(result)
