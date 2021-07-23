import logging
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from user.models import User


class APIResponse(Response):
    def __init__(self, data_status=0, data_msg='ok', data=None, http_status=None, headers=None, exception=False,
                 **kwargs):
        # data的初始状态：状态码与状态信息
        results = {
            'status': data_status,
            'msg': data_msg,
        }
        # data的响应数据体
        # results可能是False、0等数据，这些数据某些情况下也会作为合法数据返回
        if data is not None:
            results['data'] = data
        results.update(kwargs)

        super().__init__(
            data=results,
            status=http_status,
            headers=headers,
            exception=exception)


# 异常
def exception_handler(exc, context):
    # drf的exception_handler做基础处理
    response = drf_exception_handler(exc, context)
    # 为空，自定义二次处理
    if response is None:
        if isinstance(exc, MyError):
            logging.warning(
                '%s - %s - %s' %
                (context['view'], context['request'].method, exc))
            return APIResponse(2, exc.msg)
    return response


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

# 自定制jwt认证返回


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'status': 'ok',
        'data': {
            "token": token
        }
    }
# 登录接口


class UserAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 支持用户名和手机号登录
            user = User.objects.filter(is_active=True).get(
                Q(username=username) | Q(phone=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return
