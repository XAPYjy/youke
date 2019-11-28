#!/usr/bin/python3
# coding: utf-8
import json

from tools import rd2 as rd

import random


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def _gen_code():
    return str(random.randint(100000, 999999))


def _send_sms(phone, code):
    client = AcsClient('LTAIRiQGIywYBeYN', 'ZOHiNBYPr72dCFog2fLU5Pu9RvVAIf', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "Disen工作室")
    request.add_query_param('TemplateCode', "SMS_128646125")
    request.add_query_param('TemplateParam', json.dumps(dict(code=code)))

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))


def send_code(phone):
    # 生成code
    code = _gen_code()

    # 缓存中存储验证号和手机号
    rd.set(phone, code, ex=6000)  # ex 设置有效时长（秒）
    print(rd.get(phone))

    # 发送短信
    _send_sms(phone, code)


def validate_code(phone, code):
    print(phone, code, type(code))
    # 验证手机与验证号是否匹配
    if rd.exists(phone):
        if code == rd.get(phone):
            return True

    return False