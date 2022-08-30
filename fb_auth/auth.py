from django.conf import settings
from django.contrib.auth import get_user_model
from requests import HTTPError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class CustomFBAuth(BaseAuthentication):
    def authenticate(self, request):
        auth = settings.FIREBASE.auth()
        token = self.authenticate_header(request).replace('Bearer ', '')

        try:
            user = auth.get_account_info(token)['users'][0]
        except HTTPError:
            raise AuthenticationFailed

        dju = User.objects.filter(email=user['providerUserInfo'][0]['email']).first()
        if not dju:
            raise AuthenticationFailed
        return dju, token

    def authenticate_header(self, request):
        return request.META.get('HTTP_AUTHORIZATION')
