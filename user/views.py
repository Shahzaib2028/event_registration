from django.contrib import auth

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import authentication
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
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class loginAPI(APIView):

    authentication_classes = ()
    permission_classes = ()

    def create_auth_token(self, user):
        token_instance, created =  Token.objects.get_or_create(user=user)
        return token_instance.key

    def post(self, request):
        username = request.data.get('username')
        paswd = request.data.get('password')

        user = auth.authenticate(username = username , password = paswd)
        if user:
            token = self.create_auth_token(user)
            auth.login(request , user)
            return Response ({
                "token": token,
                "message": "Successfully Login",
                "success": True    
            },  status=status.HTTP_200_OK)
        else:
            return Response ({
                "message": "Invalid credentials",
                "success": False    
            },  status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):

    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = ()

    def delete_token(self, user):
        if user.is_authenticated:
            token_instances = Token.objects.filter(user=user)
            if token_instances.exists():
                token_instances.delete()

    def post(self, request):
        self.delete_token(request.user)
        auth.logout(request)
        return Response( "Logged out successfully" ,status=status.HTTP_200_OK)



