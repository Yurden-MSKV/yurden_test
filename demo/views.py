from django.shortcuts import get_object_or_404, render, redirect

from demo.forms import PostForm
from demo.models import Post


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    print(request.method)
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post.id)

    else:
        form = PostForm()

    return render(request, 'post_edit.html', {'form': form})