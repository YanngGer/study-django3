import logging
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from user.models import User


class APIResponse(Response):
    def __init__(self, data_status=0, data_msg='ok', data=None, http_status=None, headers=None, exception=False,
                 **kwargs):
        # data的初始状态：状态码与状态信息
        results = {
            'code': data_status,
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
        "token": token
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


'''
自定义返回处理
'''
class custom_renderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:

            # print(renderer_context)
            # print(renderer_context["response"].status_code)

            # 响应的信息，成功和错误的都是这个
            # 成功和异常响应的信息，异常信息在前面自定义异常处理中已经处理为{'message': 'error'}这种格式
            # print(data)

            # 如果返回的data为字典
            if isinstance(data, dict):
                # 响应信息中有message和code这两个key，则获取响应信息中的message和code，并且将原本data中的这两个key删除，放在自定义响应信息里
                # 响应信息中没有则将msg内容改为请求成功 code改为请求的状态码
                msg = data.pop('message', 'success')
                code = data.pop('code', renderer_context["response"].status_code)
            # 如果不是字典则将msg内容改为请求成功 code改为请求的状态码
            else:
                msg = 'success'
                code = renderer_context["response"].status_code

            # 自定义返回的格式
            ret = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
