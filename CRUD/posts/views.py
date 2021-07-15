from django.shortcuts import render
from .models import Post


def post_list(request):  # 리퀘스트 받고
    posts = Post.objects.all()  # 모델에서 객체를 모두 가져온다. 리스트에서 다 보고 싶으니까
    ctx = {'posts': posts}  # 딕셔너리로 만들고

    return render(request, template_name='list.html', context=ctx)  # 템플릿에게 전달.


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post': post}

    return render(request, template_name='detail.html', context=ctx)
