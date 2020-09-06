from django.db import models

# Create your models here.
class Post(models.Model):
    subject=models.CharField(max_length=50, blank=False) #제목
    created_date=models.DateTimeField(null=True, blank=True) #글쓴시간 / 수정시간
    memo=models.CharField(max_length=200, blank=False) #내용
    selectType=models.CharField(max_length=20, blank=False, default="Django") #카테고리