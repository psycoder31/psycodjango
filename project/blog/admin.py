

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']
    actions = ['make_published', 'make_draft']

    def content_size(self, post):                      #post에 현제 인스턴스가 들어간다.
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description = '글자수'          #이름 바꾸기

    def make_published(self, request, queryset):        #여기서 queryset에 관한 부분은 추후 queryset 관련 강좌에서 학습
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 published 상태로 변경'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경'       #이름 바꾸기
    

# admin.site.register(Post, PostAdmin)