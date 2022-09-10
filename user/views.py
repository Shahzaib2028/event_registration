from django.contrib import auth

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

class RegisterUserAPI(APIView):

    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response( serializer.data ,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class loginAPI(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        paswd = request.data.get('password')

        user = auth.authenticate(username = username , password = paswd)
        if user:
            auth.login(request , user)
            return Response ("Successfully Login",  status=status.HTTP_200_OK)
        else:
            return Response ("Invalid credits",  status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        auth.logout(request)
        return Response( "Logged out successfully" ,status=status.HTTP_200_OK)



