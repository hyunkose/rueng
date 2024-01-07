from django.shortcuts import redirect
from yandex_news.models import YandexArticletitle
from yesasia.models import YesasiaArticletitle
import random


def article_detail(request):
    yesasia_ids = YesasiaArticletitle.objects.filter(is_read = 0)
    yandex_ids = YandexArticletitle.objects.filter(is_read = 0)

    yesasia_urls = ["yesasia/yesasia_article_list/not-read-only/"+str(obj.article_id) for obj in yesasia_ids]
    yandex_urls = ["yandex/yandex_article_list/not-read-only/"+obj.article_id for obj in yandex_ids]

    urls = []
    urls.extend(yesasia_urls)
    urls.extend(yandex_urls)

    random_idx = random.randint(0, len(urls))
    redirect_url = "/"+urls[random_idx]
    
    return redirect(redirect_url)