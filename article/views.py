from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer

# Create your views here.

class ArticleViewSet(@@@@@빈칸@@@@@):
    queryset = @@@@@빈칸@@@@@
    serializer_class = ArticleSerializer
    permission_classes = [@@@@@빈칸@@@@@]

    def get_serializer_class(self):
        if self.action == 'list':
            return @@@@@빈칸@@@@@
        return @@@@@빈칸@@@@@

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
