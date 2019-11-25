from rest_framework.renderers import JSONRenderer


class YKrender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            code = data.pop("code")
            msg = data.pop("msg")
        except:
            code = 200
            msg = "ok"

        # 手动将HTTP状态码变为200，因为用户认证失败，抛出异常(UserTokenAuthentication中进行认证，抛出的异常对象)，HTTP状态码为500
        renderer_context['response'].status_code = 200
        renter = {
            "code": code,
            "msg": msg,
            "data": data
        }
        return super().render(renter)