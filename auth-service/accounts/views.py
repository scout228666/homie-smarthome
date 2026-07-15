from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializer import RegisterSerializer, InviteCheckSerializer, LogInSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response["HX-Redirect"] = "http://localhost:8000/login"
            return 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InviteCheckView(APIView):
    def post(self, request):
        serializer = InviteCheckSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data["invite_code"]
            response = Response(status=status.HTTP_200_OK)
            response["HX-Redirect"] = f"http://localhost:8000/register?invite_code={code}"
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    serializer_class = LogInSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access = response.data.pop('access')
            refresh = response.data.pop('refresh')

            response.set_cookie(
                key='access_token',
                value=access,
                httponly=True,
                secure=False,   
                samesite='Lax',
                max_age=60 * 15, 
            )
            response.set_cookie(
                key='refresh_token',
                value=refresh,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=60 * 60 * 24 * 7,
            )
            
            response["HX-Redirect"] = "http://localhost:8000/dashboard"

        return response
