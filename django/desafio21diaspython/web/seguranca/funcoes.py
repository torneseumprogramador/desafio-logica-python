from django.http import HttpResponseRedirect
import json
import datetime


def usuario_logado(request):
    value = request.COOKIES.get('usuario_logado')
    if value is not None:
        return json.loads(value)

def set_cookie(response, key, value, days_expire=None):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60 # por 1 ano
    else:
        max_age = days_expire * 24 * 60 * 60
    
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires
    )

def required_decorator(func):
    def containing_func(*args):
        request = args[0]

        value = request.COOKIES.get('usuario_logado')

        if value is None:
            return HttpResponseRedirect("/login")

        # try:
        #     print("=========[DECORATOR]============")
        #     print("=========[cookie]============")
        #     print(value)
        #     print("=========[args]============")
        #     print(args)
        #     print("=============================")
        # except Exception as e:
        #     raise e
        return func(*args)
    return containing_func