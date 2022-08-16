from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    # post_id = models.IntegerField() #PK는 장고에서 자동으로 생성.PK : not null&auto increment, 이름은 id로
    post_date = models.DateField(auto_now_add=True) # views.py에서 시간 저장함수 사용할 때 : timezone.localtime()로 하기
    post_content = models.CharField(max_length=400)
    post_img = models.ImageField(upload_to='images/', blank=True)
    
    #외래키 # 실제 테이블에서 외래키로 지정된 컬럼은 _id 접미사가 붙는다
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank = True)
    
    # 좋아요 #user model과 M:N 관계를 가지는 field
    post_like = models.ManyToManyField('accounts.User', related_name='like_users', blank=True)
    like_count = models.PositiveIntegerField(default=0) #0 또는 양수만 받는 필드

    def __str__(self):
        return self.post_content

class Comment(models.Model):
    # comment_id = models.IntegerField()
    comment_date = models.DateField(auto_now_add=True) # views.py에서 시간 저장함수 사용할 때 : timezone.localtime()로 하기
    comment_content = models.CharField(max_length=400)

    def __str__(self):
        return self.comment_content

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): #url name
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('posts:category')