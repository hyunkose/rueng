from django.shortcuts import render, redirect
from yesasia.models import YesasiaArticletitle, YesasiaArticlebody, WordCanonical, WordDeclension, UserSavedArticle
from .models import UserSavedWord
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from .models import AuthUser
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


import json
import re
import datetime
import dictionary_search

def index(request):
    return render(request, 'index.html')

@csrf_exempt
@login_required(redirect_field_name=None)
def article_detail(request, view_option, article_id):
    if request.method == 'GET':

        article_title_obj = YesasiaArticletitle.objects.filter(article_id = article_id)[0]
        article_body_obj = YesasiaArticlebody.objects.filter(article_id = article_id)
        user_saved_obj = UserSavedArticle.objects.filter(user_id = request.user.id, yesasia_article_id = article_title_obj.article_id)
        user_obj = AuthUser.objects.get(id = request.user.id)

        article_title_original = article_title_obj.title 
        article_title_list = article_title_obj.title.split()
        article_body_list = [obj.contents.split() for obj in article_body_obj if obj.contents is not None]
        
        is_read = 1
    
        if not user_saved_obj.exists():
            is_read = 0
        
        ## 다음 페이지로 넘기기 화살표 아이콘
        is_next_page = True
        try:
            if view_option == 'view-all':
                YesasiaArticletitle.objects.filter(article_id__gt = article_id).order_by('article_id')[0]

            elif view_option == 'not-read-only':
                read_article_obj = UserSavedArticle.objects.filter(user_id = user_obj)
                read_article_ids = [obj.yesasia_article_id.article_id for obj in read_article_obj if obj.yesasia_article_id is not None]
                article_title_obj = YesasiaArticletitle.objects.exclude(article_id__in = read_article_ids).filter(article_id__gt = article_id).order_by('article_id')[0]

            elif view_option == 'read-only':
                article_title_obj = UserSavedArticle.objects.filter(user_id = user_obj, yesasia_article_id__gt = article_id).order_by('yesasia_article_id')[0]
                
        except IndexError:
            is_next_page = False
        
        ## 이전 페이지로 넘기기 화살표 아이콘
        is_previous_page = True
        try:
            if view_option == 'view-all':
                YesasiaArticletitle.objects.filter(article_id__lt = article_id).order_by('article_id')[0]

            elif view_option == 'not-read-only':
                read_article_obj = UserSavedArticle.objects.filter(user_id = user_obj)
                read_article_ids = [obj.yesasia_article_id.article_id for obj in read_article_obj if obj.yesasia_article_id is not None]
                article_title_obj = YesasiaArticletitle.objects.exclude(article_id__in = read_article_ids).filter(article_id__lt = article_id).order_by('article_id')[0]

            elif view_option == 'read-only':
                article_title_obj = UserSavedArticle.objects.filter(user_id = user_obj, yesasia_article_id__lt = article_id).order_by('yesasia_article_id')[0]
        except IndexError:
            is_previous_page = False

        context = {'article_title_original': article_title_original,
                   'article_title_list': article_title_list,
                   'article_body_list':article_body_list,
                   'is_read': is_read,
                   'is_next_page': is_next_page,
                   'is_previous_page': is_previous_page}
        
        return render(request, 'yesasia/article_main.html', context)
    
    elif request.method == 'POST':

        request_type = json.loads(request.body).get('request_type')
        
        ## 단어 검색
        if request_type == 'word_search':
            search_word = json.loads(request.body).get('search_word')

            word_obj = WordDeclension.objects.filter(clean_form = search_word)
            
            if word_obj.exists() == False:
                no_result_dic = [{'pos': 'no_result'}]
                return JsonResponse(no_result_dic, safe=False)

            canonical_id_list = set([obj.canonical_id.canonical_id for obj in word_obj])
            canonical_id_list = list(canonical_id_list)

            canonical_list = []
            for id_ in canonical_id_list:
                canonical_queryset = WordCanonical.objects.filter(canonical_id = id_)
                canonical_list.extend([(q.canonical_id ,q.pos) for q in canonical_queryset])

            data_list = []
            for id_, pos in canonical_list:
                if pos == 'noun':
                    noun_dic_list = dictionary_search.noun_search(id_)
                    data_list.extend(noun_dic_list)
                elif pos == 'adjective':
                    adj_dic_list = dictionary_search.adj_search(id_)
                    data_list.extend(adj_dic_list)
                elif pos =='verb':
                    verb_dic_list = dictionary_search.verb_search(id_)
                    data_list.extend(verb_dic_list)
                elif pos =='etc':
                    etc_dic_list = dictionary_search.etc_search(id_)
                    data_list.extend(etc_dic_list)

            return JsonResponse(data_list, safe=False)
        ## 단어 저장
        elif request_type == 'word_save':
            save_word = json.loads(request.body).get('save_word')

            word_obj = WordDeclension.objects.filter(clean_form = save_word)

            canonical_id_list = set([obj.canonical_id.canonical_id for obj in word_obj])
            canonical_id_list = list(canonical_id_list)

            for id_ in canonical_id_list:
                canonical_word_obj = WordCanonical.objects.filter(canonical_id = id_)
                
                canonical_id = [w for w in canonical_word_obj][0]
                canonical_form = [w.canonical_form for w in canonical_word_obj][0]
                
                saved_date_obj = datetime.datetime.now()
                saved_date = str(saved_date_obj.year)+'-'+str(saved_date_obj.month)+'-'+str(saved_date_obj.day)

                user_id_obj = AuthUser.objects.get(id = request.user.id)

                sw = UserSavedWord(
                    user_id = user_id_obj,
                    canonical_id = canonical_id
                )

                try:
                    sw.save()
                    save_result = 'success'
                except IntegrityError:
                    save_result = 'duplicate_word'
                    return JsonResponse({'save_result':save_result})

                return JsonResponse({'save_result':save_result})
            
        ## article 저장
        elif (request_type == 'article_save') | (request_type == 'article_unsave'):
            
            user_id = request.user.id

            user_saved_article_obj = UserSavedArticle()
            user_obj = AuthUser.objects.get(id = user_id)
            article_obj = YesasiaArticletitle.objects.get(article_id = article_id)

            
            if request_type == 'article_save':
                
                user_saved_article_obj.user_id = user_obj
                user_saved_article_obj.article_type = 'yesasia'
                user_saved_article_obj.yesasia_article_id = article_obj
                user_saved_article_obj.yandex_article_id = None
                user_saved_article_obj.save()
            
            elif request_type == 'article_unsave':
                UserSavedArticle.objects.filter(user_id = user_obj, yesasia_article_id = article_obj)[0].delete()
                
            
            ## 화면 article 저장 표시 관련 토큰 값 발급
            article_obj = YesasiaArticletitle.objects.get(article_id = article_id)
            save_result = ''

            try:            
                user_saved_article_obj = UserSavedArticle.objects.get(user_id = user_obj, yesasia_article_id = article_obj)
                save_result = 'success'
            except UserSavedArticle.DoesNotExist:
                save_result = 'failure'

            return JsonResponse({'save_result':save_result})

@csrf_exempt
@login_required(redirect_field_name=None)
def article_list(request, view_option):
    article_list = ''
    view_option_list = zip(['view-all','not-read-only','read-only',],
                           ['View all','Not read only','Already read only',])
    
    user_obj = AuthUser.objects.get(id = request.user.id)
    user_saved_article_obj = UserSavedArticle.objects.filter(user_id = user_obj, article_type='yesasia')
    article_ids = [obj.yesasia_article_id.article_id for obj in user_saved_article_obj]
    read_article_ids = [obj.yesasia_article_id.article_id for obj in user_saved_article_obj]
    is_read_list = []

    if view_option == 'view-all':
        article_list = YesasiaArticletitle.objects.all()

    elif view_option == 'not-read-only':
        article_list = YesasiaArticletitle.objects.exclude(article_id__in = article_ids)
        view_option_list = zip(['not-read-only','view-all','read-only',],
                               ['Not read only','View all','Already read only',])
        
    elif view_option == 'read-only':
        article_list = YesasiaArticletitle.objects.filter(article_id__in = article_ids)
        view_option_list = zip(['read-only','view-all','not-read-only',],
                               ['Already read only','View all','Not read only',])

    pattern = r'[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}'
    update_date_list = [re.match(pattern, c.update_date).group() for c in article_list]


    for id_ in [obj.article_id for obj in article_list]:
        if id_ in read_article_ids:
            is_read_list.append(1)
        else:
            is_read_list.append(0)

    for new_date, q_obj, is_read in zip(update_date_list, article_list, is_read_list):
        q_obj.update_date = new_date
        q_obj.is_read = is_read

    page = request.GET.get('page', '1')
    paginator = Paginator(article_list, 12)

    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    
    context = {'page_obj_list': page_obj, 'paginator': paginator, 'view_options':view_option_list}

    return render(request, 'yesasia/list_main.html', context)

def show_next_article(request, view_option, article_id):
    redirect_article_id = ''
    user_obj = AuthUser.objects.get(id = request.user.id)
    
    if view_option == 'view-all':

        article_title_obj = YesasiaArticletitle.objects.filter(article_id__gt = article_id).order_by('article_id')[0]
        redirect_article_id = article_title_obj.article_id

    elif view_option == 'not-read-only':

        read_article_obj = UserSavedArticle.objects.filter(user_id = user_obj)
        read_article_ids = [obj.yesasia_article_id.article_id for obj in read_article_obj if obj.yesasia_article_id is not None]       
        article_title_obj = YesasiaArticletitle.objects.exclude(article_id__in = read_article_ids).filter(article_id__gt = article_id).order_by('article_id')[0]
        redirect_article_id = article_title_obj.article_id

    elif view_option == 'read-only':

        article_title_obj = UserSavedArticle.objects.filter(user_id = user_obj, yesasia_article_id__gt = article_id).order_by('yesasia_article_id')[0]
        redirect_article_id = article_title_obj.yesasia_article_id.article_id


    redirect_url = "/yesasia/yesasia_article_list/"+ view_option + '/' +str(redirect_article_id)

    return JsonResponse({"redirect_url": redirect_url})

def show_previous_article(request, view_option, article_id):
    article_title_obj = ''
    user_obj = AuthUser.objects.get(id = request.user.id)

    if view_option == 'view-all':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id).order_by('-article_id')[0]
        redirect_article_id = article_title_obj.article_id

    elif view_option == 'not-read-only':
        read_article_obj = UserSavedArticle.objects.filter(user_id = user_obj)
        read_article_ids = [obj.yesasia_article_id.article_id for obj in read_article_obj if obj.yesasia_article_id is not None]
        article_title_obj = YesasiaArticletitle.objects.exclude(article_id__in = read_article_ids).filter(article_id__lt = article_id).order_by('-article_id')[0]
        redirect_article_id = article_title_obj.article_id

    elif view_option == 'read-only':
        article_title_obj = UserSavedArticle.objects.filter(user_id = user_obj,yesasia_article_id__lt = article_id).order_by('-yesasia_article_id')[0]
        redirect_article_id = article_title_obj.yesasia_article_id.article_id

    redirect_url = "/yesasia/yesasia_article_list/"+ view_option + '/' + str(redirect_article_id)

    return JsonResponse({"redirect_url": redirect_url})