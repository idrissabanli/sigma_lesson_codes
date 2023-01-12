from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.utils import swagger_auto_schema
from accounts.api.serializers import UserProfileSerializer, UserProfileResponseSerializer


class LoginApiView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserProfileResponseSerializer()})
    def post(self, *args, **kwargs):
        return super().post( *args, **kwargs)
