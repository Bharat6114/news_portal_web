from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from account.apis.serializers import UserSerializer


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer