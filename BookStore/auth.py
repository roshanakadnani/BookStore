import jwt, time
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

secret_key = 'some long text'
auth_timeout = 60 * 60  # seconds


class RestAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION'][7:]
            claims = jwt.decode(token, secret_key, algorithms=["HS256"])
            user = User.objects.filter(id=claims['id']).first()
            if not user or not user.is_active:
                raise exceptions.AuthenticationFailed('No such user')
            return (user, None)
        except Exception:
            raise exceptions.AuthenticationFailed('No such user')


def encode_user(user):
    x = {
        'exp': int(time.time() + auth_timeout),
        'id': user.id,
    }
    return jwt.encode(x, secret_key, algorithm="HS256")
