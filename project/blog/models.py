import re

from django.forms import ValidationError
from django.db import models

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.

class Post(models.Model):
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    author = models.CharField(
        max_length = 20,
        verbose_name='작성자',
    )
    title = models.CharField(               # 길이 제한이 있는 문자열
        max_length=100,
        verbose_name='제목', 
        help_text='제목을 입력해 주세요 최대 90자'
    )
    content = models.TextField(             # 길이 제한이 없는 문자열
        verbose_name='내용'
    )                            
    created_at = models.DateTimeField(      
        auto_now_add=True                   #데이터가 최초 저장될 때 저장
    )   
    updated_at = models.DateTimeField(
        auto_now=True                       #데이터가 저장 및 갱신될 때마다 저장됨
    )        
    tags = models.CharField(
        max_length=100, 
        blank=True
    )
    lnglat = models.CharField(
        max_length=50, 
        help_text='경도, 위도 값', 
        blank=True, 
        validators=[lnglat_validator]
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS
    )
    tag_set = models.ManyToManyField('Tag')
    ''' 릴레이션을 지정할 때는 문자열 혹은 클래스 네임을 직접 지정할 수 있다. 
        But tag 클래스는 하위에 구현되었기 때문에 스트링으로 지정
        다른 엡에 있는 경우에는 'app.models'라는 문자열을 지정할 수 있다.
    '''



class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name