from rest_framework import @@@@@빈칸@@@@@
from .models import Comment
from user.serializers import UserSerializer

class CommentSerializer(@@@@@빈칸@@@@@):
    author = UserSerializer(read_only=True)

    class Meta:
        model = @@@@@빈칸@@@@@
        fields = ('id', 'content', 'author', 'created_at', 'updated_at')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        validated_data['article_id'] = self.context['view'].kwargs['article_pk']
        return super().create(validated_data)

class CommentListSerializer(@@@@@빈칸@@@@@):
    author = UserSerializer(read_only=True)

    class Meta:
        model = @@@@@빈칸@@@@@
        fields = ('id', 'content', 'author', 'created_at')
