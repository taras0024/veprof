from django.conf import settings
from django.contrib.auth import get_user_model
from requests import HTTPError
from rest_framework import viewsets, views, response, generics
from rest_framework.permissions import IsAuthenticated

from fb_auth.auth import CustomFBAuth
from fb_auth.serializers import UserSerializer, SignInSerializer

User = get_user_model()


class SignInView(generics.GenericAPIView):
    http_method_names = ['post', ]
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        auth = settings.FIREBASE.auth()

        try:
            user = auth.sign_in_with_email_and_password(data['email'], data['password'])
        except HTTPError:
            return response.Response(status=404)
        return response.Response({'token': user['idToken']})


class GetUsersView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomFBAuth,)
