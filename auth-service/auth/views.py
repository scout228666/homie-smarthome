from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from auth.serializer import RegisterSerializer, InviteCheckSerializer, LogInSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InviteCheckView(APIView):
    def post(self, request):
        serializer = InviteCheckSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"detail": "ok"}, status=status.HTTP_200_OK)
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
                secure=True,   
                samesite='Lax',
                max_age=60 * 15, 
            )
            response.set_cookie(
                key='refresh_token',
                value=refresh,
                httponly=True,
                secure=True,
                samesite='Lax',
                max_age=60 * 60 * 24 * 7,
            )

        return response