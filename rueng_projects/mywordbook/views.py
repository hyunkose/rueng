from django.shortcuts import render, redirect
from .models import SavedVocab, WordCanonical, WordDeclension
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import dictionary_search

@csrf_exempt
def mywordbook_main(request):
    if request.method == 'GET':
        saved_word_obj = SavedVocab.objects.all()
        saved_word_ids = [obj.canonical_id.canonical_id for obj in saved_word_obj]
        
        saved_canonical_list = []

        for id_ in saved_word_ids:
            canonical_obj = WordCanonical.objects.filter(canonical_id = id_)[0]
            
            canonical_id = canonical_obj.canonical_id
            canonical_form = canonical_obj.canonical_form
            word_meaning = canonical_obj.meaning

            saved_canonical_list.append({'canonical_id':canonical_id,
                                         'canonical_form':canonical_form,
                                         'word_meaning': word_meaning})
            
        page = request.GET.get('page', '1')
        paginator = Paginator(saved_canonical_list, 15)

        try:
            page_obj = paginator.get_page(page)
        except PageNotAnInteger:
            page = 1
            page_obj = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            page_obj = paginator.page(page)
        
        context = {'page_obj_list': page_obj, 'paginator': paginator,}

        return render(request, 'mywordbook/wordbook.html', context)

    elif request.method == 'POST':
        search_word = json.loads(request.body).get('search_word')

        saved_vocab_obj = SavedVocab.objects.filter(canonical_form = search_word)

        canonical_id_list = set([obj.canonical_id.canonical_id for obj in saved_vocab_obj])
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

    elif request.method == 'DELETE':
        delete_word_id = json.loads(request.body).get('delete_word_id')
        delete_word_obj = SavedVocab.objects.get(canonical_id = delete_word_id)
        delete_word_obj.delete()

        return redirect('/mywordbook')
