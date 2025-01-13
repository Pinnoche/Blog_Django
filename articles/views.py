from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . models import Article
from . forms import CreateArticle

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'articles': articles })

@login_required(login_url="accounts:login")
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, "articles/article_create.html", {'form': form})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    side = Article.objects.all().get(slug=slug)
    return render(request, "articles/article_detail.html", {'article': article})


# The views in Django are the functions that take a web request and return a web response.