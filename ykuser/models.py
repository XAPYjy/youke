from django.db.models import Q

from yk_models.models import YkUser


class YKUser(YkUser):
    def save_user(self, name=None, pwd=None, phone=None, emil=None,auth=True):
        YkUser.objects.create(yk_name=name, yk_auto_string=pwd, yk_phone=int(phone), yk_emil=emil,sys_auth=auth)

    def select_all(self,  id=0, name=0, phone=0, pwd=0, emil=0):
        try:
            q = Q(id=id) | Q(yk_name=name) | Q(yk_phone=int(phone)) | Q(yk_auto_string=pwd) | Q(yk_emil=emil)
            item = YkUser.objects.filter(q)
            return item
        except:
            return None
