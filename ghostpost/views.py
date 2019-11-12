from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost.models import Post
from ghostpost.forms import PostSubmit

def index(request):
    html = 'index.html'
    posts = Post.objects.all()

    return render(request, html, {'posts': posts})

def PostAdd(request):
    html = "postform.html"

    if request.method == "POST":
        form = PostSubmit(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                boast_roast = post['boast_roast'],
                content = post['content']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = PostSubmit()

    return render(request, html, {'form': form})

    
def timeFilter(request):
    pass

def voteFilter(request):
    pass