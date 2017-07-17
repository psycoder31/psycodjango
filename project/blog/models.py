import re

from django.forms import ValidationError
from django.db import models

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.

class Post(models.Model):
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
