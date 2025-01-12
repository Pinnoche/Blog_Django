from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'articles': articles })

@login_required(login_url="{% url 'accounts:login' %}")
def article_create(request):
    return render(request, "articles/article_create.html")

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_detail.html", {'article': article})
    

def create(request):
    return render(request, "articles/create.html")