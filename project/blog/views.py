from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list' : qs})

def post_detail(request, id):
    # try :
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404 
    post = get_object_or_404(Post, id=id) 
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })