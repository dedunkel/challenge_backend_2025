from django.db import models
from user.models import User
from article.models import @@@@@빈칸@@@@@

class Comment(@@@@@빈칸@@@@@):
    content = models.TextField()
    article = @@@@@빈칸@@@@@(@@@@@빈칸@@@@@, on_delete=models.CASCADE, related_name='comments')
    author = @@@@@빈칸@@@@@(@@@@@빈칸@@@@@, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        verbose_name = '댓글'
        verbose_name_plural = '댓글들'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author.username}의 댓글: {self.content[:20]}'
