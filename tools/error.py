from rest_framework.exceptions import APIException


class YKException(APIException):
    def __init__(self, detail):
        self.detail = detail