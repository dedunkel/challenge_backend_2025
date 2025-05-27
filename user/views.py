from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import @@@@@빈칸@@@@@
from django.contrib.auth import login, logout
from .serializers import @@@@@빈칸@@@@@

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [@@@@@빈칸@@@@@]
    serializer_class = @@@@@빈칸@@@@@

class UserLoginView(APIView):
    permission_classes = [@@@@@빈칸@@@@@]

    def post(self, request):
        serializer = @@@@@빈칸@@@@@(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(@@@@@빈칸@@@@@(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
