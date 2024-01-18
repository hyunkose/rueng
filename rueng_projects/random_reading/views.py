from django.shortcuts import redirect
from yandex_news.models import YandexArticletitle
from yesasia.models import YesasiaArticletitle
from random_reading.models import AuthUser, UserSavedArticle
import random
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required(redirect_field_name=None)
def article_detail(request):

    yesasia_saved_obj = UserSavedArticle.objects.filter(user_id = request.user.id, article_type = 'yesasia')
    yesasia_saved_ids = [obj.yesasia_article_id.article_id for obj in yesasia_saved_obj] 

    yandex_saved_obj = UserSavedArticle.objects.filter(user_id = request.user.id, article_type = 'yandex')
    yandex_saved_ids = [obj.yandex_article_id.article_id for obj in yandex_saved_obj] 

    yesasia_ids = YesasiaArticletitle.objects.exclude(article_id__in = yesasia_saved_ids)
    yandex_ids = YandexArticletitle.objects.exclude(article_id__in = yandex_saved_ids)

    yesasia_urls = ["yesasia/yesasia_article_list/not-read-only/"+str(obj.article_id) for obj in yesasia_ids]
    yandex_urls = ["yandex/yandex_article_list/not-read-only/"+obj.article_id for obj in yandex_ids]

    urls = []
    urls.extend(yesasia_urls)
    urls.extend(yandex_urls)

    random_idx = random.randint(0, len(urls))
    redirect_url = "/"+urls[random_idx]
    
    return redirect(redirect_url)