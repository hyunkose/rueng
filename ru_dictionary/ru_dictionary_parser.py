## crawler
from bs4 import BeautifulSoup
from urllib import parse
import requests
import progressbar

def word_parser(word_links):

    ## get word detail info
    html_source = ''

    word_title_list= []
    word_pos_list = []
    word_meaning_list = []
    declensions_table_content = []

    verb_aspect_list = []
    imperfective_perfective_list = []

    bar = progressbar.ProgressBar(maxval=len(word_links)).start()

    for idx,link in enumerate(word_links):
        
        html_source = requests.get(link)
        soup = BeautifulSoup(html_source.text, "html.parser")
        
        ## word title, pos ,meaning info
        word_titles = soup.select('div.bare span')
        word_pos = soup.select('div.overview p')
        word_meanings = soup.select('div.translations p.tl')
        
        word_title_text = [w.text for w in word_titles][0]
        word_pos_text = [p.text for p in word_pos][0].split(',')[0]
        word_meaning_text = '; '.join([m.text for m in word_meanings])
        
        word_title_list.append((idx, word_title_text))
        word_meaning_list.append((idx, word_meaning_text))
        
        ## word declension info
        word_declensions = soup.select('.declension td')
        declension_list = []

        
        if word_pos_text == 'noun':
            for wd in word_declensions:
                delclension_soup = BeautifulSoup(str(wd), "html.parser")
                declensions_text = delclension_soup.select('p')
                declention_text_list = '/'.join([d.text for d in declensions_text])

                declension_list.append(declention_text_list)

            declension_contents = [
                (idx,'nominative_singular', declension_list[0]),
                (idx,'nominative_plural', declension_list[1]),
                (idx,'genitive_singular', declension_list[2]),
                (idx,'genitive_plural', declension_list[3]),
                (idx,'dative_singular', declension_list[4]),
                (idx,'dative_plural', declension_list[5]),
                (idx,'accusative_singular', declension_list[6]),
                (idx,'accusative_plural', declension_list[7]),
                (idx,'instrumental_singular', declension_list[8]),
                (idx,'instrumental_plural', declension_list[9]),
                (idx,'prepositional_singular', declension_list[10]),
                (idx,'prepositional_plural', declension_list[11]),
            ]

            declensions_table_content.extend(declension_contents)
            word_pos_list.append((idx, word_pos_text))
        
        elif word_pos_text == 'adjective':
            short_form_list = []
            
            for wd in word_declensions:
                delclension_soup = BeautifulSoup(str(wd), "html.parser")
                
                declensions_text = delclension_soup.select('p')
                declension_list.append(declensions_text)
            
                short_forms = soup.select('.shorts td')
                short_form_list = [s.text for s in short_forms]

                declension_list = [d for d in declension_list if len(d) > 0]

            declension_contents = [
                (idx,'masculine_nominative', declension_list[0][0].text),
                (idx,'feminine_nominative', declension_list[1][0].text),
                (idx,'neuter_nominative', declension_list[2][0].text),
                (idx,'nominative_plural', declension_list[3][0].text),
                (idx,'genitive_masculine_neuter', declension_list[4][0].text),
                (idx,'feminine_genitive', declension_list[5][0].text),
                (idx,'genitive_plural', declension_list[7][0].text),
                (idx,'dative_masculine_neuter', declension_list[8][0].text),
                (idx,'dative_feminine', declension_list[9][0].text),
                (idx,'dative_plural', declension_list[11][0].text),
                (idx,'accusative_inanimate_masculine', declension_list[12][0].text),
                (idx,'accusative_animate_masculine', declension_list[12][1].text),
                (idx,'accusative_feminine', declension_list[13][0].text),
                (idx,'accusative_neuter', declension_list[14][0].text),
                (idx,'accusative_animate_plural', declension_list[15][1].text),
                (idx,'instrumental_masculine_neuter', declension_list[16][0].text),
                (idx,'feminine_instrumental', declension_list[17][0].text),
                (idx,'instrumental_plural', declension_list[19][0].text),
                (idx,'feminine_prepositional', declension_list[21][0].text),
                (idx,'masculine_neuter_prepositional', declension_list[22][0].text),
                (idx,'plural_prepositional', declension_list[23][0].text),
            ]

            if len(short_form_list) > 0:
                declension_contents.extend(
                    [(idx,'masculine_short-form', short_form_list[0]),
                    (idx,'neuter_short-form', short_form_list[1]),
                    (idx,'feminine_short-form', short_form_list[2]),
                    (idx,'plural_short-form', short_form_list[3]),]
                )


            declensions_table_content.extend(declension_contents)
            word_pos_list.append((idx, word_pos_text))

        elif word_pos_text == 'verb':
            ## word declension info
            declension_tables = soup.select('.table-container')


            ## conjugations
            for dt in declension_tables[:3]:
                declension_soup = BeautifulSoup(str(dt), "html.parser")
                declension_obj = declension_soup.select('td')
                declension_list.extend([o.text for o in declension_obj])

            ## participles
            participles = []

            declension_soup = BeautifulSoup(str(declension_tables[3]), "html.parser")
            declension_obj = declension_soup.select('td')

            for table_idx, obj in enumerate(declension_obj):
                if table_idx%2 == 0:
                    soup_obj = BeautifulSoup(str(obj), "html.parser")
                    participle_text_obj = soup_obj.select('p')
                    participle_text = '/'.join([obj.text for obj in participle_text_obj])

                    participles.append(participle_text)


            declension_list.extend(participles)

            ## declension_contents list parsing
            declension_contents = [

                (idx,'first-person_present_singular', declension_list[0]),
                (idx,'first-person_future_singular', declension_list[1]),
                (idx,'present_second-person_singular', declension_list[2]),
                (idx,'future_second-person_singular', declension_list[3]),
                (idx,'present_singular_third-person', declension_list[4]),
                (idx,'future_singular_third-person', declension_list[5]),
                (idx,'first-person_plural_present', declension_list[6]),
                (idx,'first-person_future_plural', declension_list[7]),
                (idx,'plural_present_second-person', declension_list[8]),
                (idx,'future_plural_second-person', declension_list[9]),
                (idx,'plural_present_third-person', declension_list[10]),
                (idx,'future_plural_third-person', declension_list[11]),
                (idx,'imperative_singular', declension_list[12]),
                (idx,'imperative_plural', declension_list[13]),
                (idx,'masculine_past_singular', declension_list[14]),
                (idx,'feminine_past_singular', declension_list[15]),
                (idx,'neuter_past_singular', declension_list[16]),
                (idx,'neuter_past_plural', declension_list[17]),
                (idx,'active_participle_present', declension_list[18]),
                (idx,'active_participle_past', declension_list[19]),
                (idx,'participle_passive_present', declension_list[20]),
                (idx,'participle_passive_past', declension_list[21]),
                (idx,'adverbial_participle_present', declension_list[22]),
                (idx,'active_participle_present', declension_list[23]),
            ]
            

            verb_aspect_text = [p.text for p in word_pos][0].split(',')[1].strip()

            ## word-partner
            partner_word_obj = soup.select('a.verb-partner')
            partner_word_text = ', '.join([obj.text for obj in partner_word_obj])
            
            if verb_aspect_text == 'imperfective':
                imperfective_perfective = word_title_text+'/'+partner_word_text
                imperfective_perfective_list.append((idx, imperfective_perfective))
            elif verb_aspect_text == 'perfective':
                imperfective_perfective = partner_word_text+'/'+word_title_text
                imperfective_perfective_list.append((idx, imperfective_perfective))

            
            declensions_table_content.extend(declension_contents)
            verb_aspect_list.append((idx, verb_aspect_text))
            word_pos_list.append((idx, word_pos_text))
            
        else:
            word_pos_list.append((idx, 'etc'))
                
        ## progress check point
        bar.update(idx)

    bar.finish()
    return (word_title_list, word_pos_list, word_meaning_list, declensions_table_content, verb_aspect_list, imperfective_perfective_list)
        