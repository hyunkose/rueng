from django.shortcuts import render, redirect
from yesasia.models import YesasiaArticletitle, YesasiaArticlebody, WordCanonical, WordDeclension
from .models import SavedVocab
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError

import json
import re
import datetime
import dictionary_search


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def article_detail(request, view_option, article_id):
    if request.method == 'GET':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id = article_id)[0]
        article_body_obj = YesasiaArticlebody.objects.filter(article_id = article_id)
        
        article_title_original = article_title_obj.title 
        article_title_list = article_title_obj.title.split()
        article_body_list = [obj.contents.split() for obj in article_body_obj if obj.contents is not None]
        is_read = article_title_obj.is_read

        ## 다음 페이지로 넘기기 화살표 아이콘
        is_next_page = True
        try:
            if view_option == 'view-all':
                YesasiaArticletitle.objects.filter(article_id__gt = article_id).order_by('article_id')[0]
            elif view_option == 'not-read-only':
                YesasiaArticletitle.objects.filter(article_id__gt = article_id, is_read = 0).order_by('article_id')[0]
            elif view_option == 'read-only':
                YesasiaArticletitle.objects.filter(article_id__gt = article_id, is_read = 1).order_by('article_id')[0]
        except IndexError:
            is_next_page = False
        
        ## 이전 페이지로 넘기기 화살표 아이콘
        is_previous_page = True
        try:
            if view_option == 'view-all':
                article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id).order_by('-article_id')[0]
            elif view_option == 'not-read-only':
                article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id, is_read = 0).order_by('-article_id')[0]
            elif view_option == 'read-only':
                article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id, is_read = 1).order_by('-article_id')[0]
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

        if request_type == 'word_search':
            search_word = json.loads(request.body).get('search_word')

            word_obj = WordDeclension.objects.filter(clean_form = search_word)
            
            if word_obj.exists() == False:
                no_result_dic = [{'pos': 'no_result'}]
                return JsonResponse(no_result_dic, safe=False)


            canonical_id_list = set([obj.canonical_id.canonical_id for obj in word_obj])
            canonical_id_list = list(canonical_id_list)

            pos_list = []

            for id_ in canonical_id_list:
                canonical_queryset = WordCanonical.objects.filter(canonical_id = id_)
                pos_list.extend([q.pos for q in canonical_queryset])


            for pos in pos_list:
                if pos == 'noun':
                    noun_dic_list = dictionary_search.noun_search(canonical_id_list)
                    return JsonResponse(noun_dic_list, safe=False)
                elif pos == 'adj':
                    adj_dic_list = dictionary_search.adj_search(canonical_id_list)
                    return JsonResponse(adj_dic_list, safe=False)
                elif pos =='verb':
                    verb_dic_list = dictionary_search.verb_search(canonical_id_list)
                    return JsonResponse(verb_dic_list, safe=False)


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

                sw = SavedVocab(
                    canonical_form = canonical_form,
                    canonical_id = canonical_id,
                    saved_date = saved_date,
                )

                try:
                    sw.save()
                    save_result = 'success'
                except IntegrityError:
                    save_result = 'duplicate_word'
                    return JsonResponse({'save_result':save_result})

                return JsonResponse({'save_result':save_result})
            
        elif (request_type == 'article_save') | (request_type == 'article_unsave'):
            article_title_obj = YesasiaArticletitle.objects.get(article_id = article_id)
            
            if request_type == 'article_save':
                article_title_obj.is_read = 1
            elif request_type == 'article_unsave':
                article_title_obj.is_read = 0
            
            article_title_obj.save()

            save_result = 'success'

            return JsonResponse({'save_result':save_result})

@csrf_exempt
def article_list(request, view_option):
    article_list = ''
    view_option_list = zip(['view-all','not-read-only','read-only',],
                           ['View all','Not read only','Already read only',])

    if view_option == 'view-all':
        article_list = YesasiaArticletitle.objects.all()
    elif view_option == 'not-read-only':
        article_list = YesasiaArticletitle.objects.filter(is_read = 0)
        view_option_list = zip(['not-read-only','view-all','read-only',],
                               ['Not read only','View all','Already read only',])
    elif view_option == 'read-only':
        article_list = YesasiaArticletitle.objects.filter(is_read = 1)
        view_option_list = zip(['read-only','view-all','not-read-only',],
                               ['Already read only','View all','Not read only',])

    pattern = r'[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}'
    update_date_list = [re.match(pattern, c.update_date).group() for c in article_list]

    for new_date, q_obj in zip(update_date_list, article_list):
        q_obj.update_date = new_date

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
    article_title_obj = ''

    if view_option == 'view-all':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__gt = article_id).order_by('article_id')[0]
    elif view_option == 'not-read-only':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__gt = article_id, is_read = 0).order_by('article_id')[0]
    elif view_option == 'read-only':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__gt = article_id, is_read = 1).order_by('article_id')[0]

    redirect_url = "/yesasia/yesasia_article_list/"+ view_option + '/' +str(article_title_obj.article_id)

    return JsonResponse({"redirect_url": redirect_url})

def show_previous_article(request, view_option, article_id):
    article_title_obj = ''

    if view_option == 'view-all':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id).order_by('-article_id')[0]
    elif view_option == 'not-read-only':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id, is_read = 0).order_by('-article_id')[0]
    elif view_option == 'read-only':
        article_title_obj = YesasiaArticletitle.objects.filter(article_id__lt = article_id, is_read = 1).order_by('-article_id')[0]

    redirect_url = "/yesasia/yesasia_article_list/"+ view_option + '/' + str(article_title_obj.article_id)

    return JsonResponse({"redirect_url": redirect_url})