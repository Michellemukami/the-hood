


from django.http  import HttpResponse,Http404
from .models import Image,NewsLetterRecipients,Profile
from django.shortcuts import render,redirect
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm, NewsLetterForm, NewsProfileForm,CommentForm
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def home(request):
    current_user =request.user
    posts = Project.objects.all()
    profile = Profile.objects.all()
    users = Profile.objects.all()
    views = Profile.objects.all()
    to_follow = User.objects.all().exclude(id=request.user.id)
    return render(request, 'home.html', {"posts":posts,"profile":profile, "users":users,"views":to_follow, })

# Create your views here.
def login_page(request):
    return render(request, 'registration/welcome.html')

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
        return redirect('user')
    else:
        form = NewsProfileForm()
    return render(request, 'profile.html', {"form":form})
@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('user')

    else:
        form = NewArticleForm()
    return render(request, 'new-article.html', {"form": form}) 
@login_required(login_url='/accounts/login/')
def user(request):
    user = request.user
    profile = Profile.objects.get(username=user)
    posts=Image.objects.filter(id=user.id)
    return render(request, 'user-post.html',{"profile":profile,"posts":posts})
@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor = current_user
            comment.save()
        return redirect('user')

    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form}) 