from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="shop_post_set")
    ''' related_name = '+' 이렇게 넣으면 related_name을 사용하지 않는 방법으로 지정할 수 있다.
    '''
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)