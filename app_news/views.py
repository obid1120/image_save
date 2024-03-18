from django.shortcuts import render, get_list_or_404, redirect

from .models import News, Category


def news_list(request):
    news = News.objects.all()  # SELECT * from news
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    # news = get_list_or_404(News, pk)
    # SELECT * from news where id=pk
    return render(request, 'news/news_detail.html', {'news': news})


def add_news(request):
    if request.method == 'POST':
        title = request.POST['title']
        txt = request.POST['text']
        news_image = request.FILES['image']
        cat_id = Category.objects.get(pk=int(request.POST['category']))
        news = News(news_title=title, news_txt=txt, news_category=cat_id, news_image=news_image)
        news.save()
        return redirect('news_detail', pk=news.pk)
    else:
        category = Category.objects.all()
        return render(request, 'news/news_add.html', {'categories': category})


def edit_news(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        news.news_title = request.POST['title']
        news.news_txt = request.POST['text']
        news.news_category = Category.objects.get(pk=int(request.POST['category']))
        news_image = request.FILES['image']
        if news_image:
            news.news_image = news_image
        news.save()
        return redirect('news_detail', pk=news.pk)
    else:
        category = Category.objects.all()
        return render(request, 'news/news_edit.html', {'news': news, 'categories': category})
