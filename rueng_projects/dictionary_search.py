from yesasia.models import YesasiaArticletitle, YesasiaArticlebody, WordCanonical, WordDeclension

def tag_return(declension_list, tag_list):
    word_dic = {}
    
    for tag in tag_list:
        tag_set = set(tag.split('_'))
        word_dic[tag] = '/'.join([d[0] for d in declension_list if (tag_set == set(d[1].split('_')).intersection(tag_set)) & ('dated' not in set(d[1].split('_')))])
    
    return word_dic

def noun_search(id_):
    noun_dic_list = []

    declension_queryset = WordDeclension.objects.filter(canonical_id = id_)
    canonical_queryset = WordCanonical.objects.filter(canonical_id = id_)
    
    canonical_list = [(q.pos, q.meaning) for q in canonical_queryset]
    declension_list = [(q.form, q.tags) for q in declension_queryset]

    tag_list = ['nominative_singular', 'genitive_singular', 'dative_singular',
                'accusative_singular', 'instrumental_singular', 'prepositional_singular',
                'nominative_plural', 'genitive_plural', 'dative_plural',
                'accusative_plural', 'instrumental_plural', 'prepositional_plural']

    noun_dic = tag_return(declension_list, tag_list)

    noun_dic['meaning'] = canonical_list[0][1]
    noun_dic['pos'] = canonical_list[0][0]

    for key in noun_dic:
        noun_dic[key] = '/'.join(set(noun_dic[key].split('/')))

    noun_dic_list.append(noun_dic)

    return noun_dic_list

def adj_search(id_):
    adj_dic_list = []

    declension_queryset = WordDeclension.objects.filter(canonical_id = id_)
    canonical_queryset = WordCanonical.objects.filter(canonical_id = id_)
    
    canonical_list = [(q.pos, q.meaning) for q in canonical_queryset]
    declension_list = [(q.form, q.tags) for q in declension_queryset]

    tag_list = ['masculine_nominative', 'neuter_nominative', 'feminine_nominative',
                'nominative_plural', 'genitive_masculine_neuter', 'feminine_genitive',
                'genitive_plural', 'dative_masculine_neuter', 'dative_feminine',
                'dative_plural', 'accusative_animate_masculine', 'accusative_neuter',
                'accusative_feminine', 'accusative_animate_plural', 'accusative_inanimate_plural',
                'instrumental_masculine_neuter', 'feminine_instrumental', 'instrumental_plural',
                'masculine_neuter_prepositional', 'feminine_prepositional', 'plural_prepositional',
                'masculine_short-form', 'neuter_short-form', 'feminine_short-form',
                'plural_short-form']

    adj_dic = tag_return(declension_list, tag_list)

    adj_dic['meaning'] = canonical_list[0][1]
    adj_dic['pos'] = canonical_list[0][0]

    for key in adj_dic:
        adj_dic[key] = '/'.join(set(adj_dic[key].split('/')))

    adj_dic_list.append(adj_dic)
    
    return adj_dic_list

def verb_search(id_):
    verb_dic_list = []

    declension_queryset = WordDeclension.objects.filter(canonical_id = id_)
    canonical_queryset = WordCanonical.objects.filter(canonical_id = id_)
    
    canonical_list = [(q.pos, q.meaning,  q.imperfective_perfective, q.canonical_form) for q in canonical_queryset]
    declension_list = [(q.form, q.tags) for q in declension_queryset]
    
    tag_list = ['infinitive',
                'active_participle_present', 'active_participle_past',
                'participle_passive_present', 'participle_passive_past',
                'adverbial_participle_present', 'adverbial_participle_past',
                'first-person_present_singular', 'first-person_future_singular',
                'present_second-person_singular', 'future_second-person_singular',
                'present_singular_third-person', 'future_singular_third-person',
                'first-person_plural_present', 'first-person_future_plural',
                'plural_present_second-person', 'future_plural_second-person',
                'plural_present_third-person', 'future_plural_third-person',
                'imperative_singular','imperative_plural',
                'masculine_past_singular', 'neuter_past_singular', 'feminine_past_singular', 'neuter_past_plural']

    verb_dic = tag_return(declension_list, tag_list)

    verb_dic['meaning'] = canonical_list[0][1]
    verb_dic['pos'] = canonical_list[0][0]
    verb_dic['imperfective_perfective'] = canonical_list[0][2]

    for key in verb_dic:
        try:
            verb_dic[key] = '/'.join(set(verb_dic[key].split('/')))
        except AttributeError:
            verb_dic[key] = None
            continue
    
    verb_dic['infinitive'] = canonical_list[0][3]

    verb_dic_list.append(verb_dic)
    return verb_dic_list

def etc_search(id_):
    etc_dic_list = []

    declension_queryset = WordDeclension.objects.filter(canonical_id = id_)
    canonical_queryset = WordCanonical.objects.filter(canonical_id = id_)
    
    canonical_list = [(q.pos, q.meaning) for q in canonical_queryset]
    declension_list = [(q.form, q.tags) for q in declension_queryset]

    tag_list = ['main_form']
    
    etc_dic = tag_return(declension_list, tag_list)
    
    etc_dic['meaning'] = canonical_list[0][1]
    etc_dic['pos'] = canonical_list[0][0]

    for key in etc_dic:
        etc_dic[key] = '/'.join(set(etc_dic[key].split('/')))

    etc_dic_list.append(etc_dic)

    return etc_dic_list


