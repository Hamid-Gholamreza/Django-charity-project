from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )
    


class UserRegistration(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer



class LoginAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            return Response(data={'message': f"Hello {request.user.username}!"}, status=status.HTTP_200_OK)
        except:
            return Response(data={'message': f"Hello {request.user.username}!"}, status=status.HTTP_401_UNAUTHORIZED)


