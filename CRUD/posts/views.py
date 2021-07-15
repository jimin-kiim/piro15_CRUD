from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def post_list(request):  # 리퀘스트 받고
    posts = Post.objects.all()  # 모델에서 객체를 모두 가져온다. 리스트에서 다 보고 싶으니까
    ctx = {'posts': posts}  # 딕셔너리로 만들고

    return render(request, template_name='list.html', context=ctx)  # 템플릿에게 전달.


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post': post}

    return render(request, template_name='detail.html', context=ctx)


def post_create(request):
    if request.method == 'POST':  # 요청이 포스트로 오면. 저장, 생성, 수정
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:list')  # 이름이 list인 곳으로 이동하고 싶어요
    else:  # 그냥 글 쓸 때. get일 때. 읽어들일 때
        form = PostForm()
        ctx = {'form': form}

        return render(request, template_name='post_form.html', context=ctx)


def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', pk)
    else:
        form = PostForm(instance=post)
        ctx = {'form': form}

        return render(request, template_name='post_form.html', context=ctx)


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('posts:list')
