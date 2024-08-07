from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    object_list = Article.objects.all()
    for article in object_list:
        scopes = article.scopes.all()
        main_scope = scopes.filter(is_main=True).first()
        other_scopes = scopes.filter(is_main=False).order_by('tag__name')
        if main_scope:
            article.scopes_sorted = [main_scope] + list(other_scopes)
        else:
            article.scopes_sorted = list(other_scopes)

    template = 'articles/news.html'
    context = {
        'object_list': object_list,
    }

    return render(request, template, context)
