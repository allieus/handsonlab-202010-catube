from django.db import models


# 생성될 테이블명 : catube_video
class Video(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField()
    photo = models.ImageField()
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
