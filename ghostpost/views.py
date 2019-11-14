from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost.models import Post
from ghostpost.forms import PostSubmit

def index(request):
    html = 'index.html'
    posts = Post.objects.all().order_by("-datetime")

    return render(request, html, {'posts': posts})

def PostAdd(request):
    html = "postform.html"

    if request.method == "POST":
        form = PostSubmit(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                boast_roast = data['boast_roast'],
                content = data['content']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = PostSubmit()

    return render(request, html, {'form': form})


def boast(request):
    html = "index.html"
    posts = Post.objects.filter(boast_roast=True).order_by("-datetime")

    return render(request, html, {'posts': posts})

def roast(request):
    html = 'index.html'
    posts = Post.objects.filter(boast_roast=False).order_by("-datetime")

    return render(request, html, {'posts': posts})

def voteFilter(request):
    html = "index.html"
    posts = sorted(Post.objects.all(),  key=lambda m: m.vote_count)[::-1]

    return render(request, html, {'posts': posts})
    

def likePost(request, id):
    # breakpoint()
    post = Post.objects.get(id=id)
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def dislikePost(request, id):
    post = Post.objects.get(id=id)
    post.downvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))