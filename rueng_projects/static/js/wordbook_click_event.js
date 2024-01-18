const declension_html = function (data){
    let html_raw_list = []
    
    for (let d of data){

        pos = d['pos']
    
        if (pos == 'noun'){
            let html_raw = `
            <div class="close-button-wrapper">
                <button class="close-button" onclick="close_btn_click_event()"><img src = "../../static/img/x-circle.png"></button>        
            </div>
    
            <p class="original-word">${d['nominative_singular']}</p>
    
            <p class="word-meaning-title">1. meaning</p>
            <p class="word-meaning">${d['meaning']}</p>
    
            <p class="pos-title">2. Part of Speech</p>
            <p class="pos">${d['pos']}</p>
            
            <p class="word-table-title">3. Declension Table</p>
            <table class="word-table">
                <thead>
                    <tr>
                        <th scope="col" style="background-color: #33c9e4;"></th>
                        <th scope="col" style="background-color: #33c9e4;">Singular</th>
                        <th scope="col" style="background-color: #33c9e4;">Plural</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Nominative</th>
                        <td>${d['nominative_singular']}</td>
                        <td>${d['nominative_plural']}</td>
                    </tr>
                    <tr>
                        <th scope="row">Genitive</th>
                        <td>${d['genitive_singular']}</td>
                        <td>${d['genitive_plural']}</td>
                    </tr>
                    <tr>
                        <th scope="row">Dative</th>
                        <td>${d['dative_singular']}</td>
                        <td>${d['dative_plural']}</td>
                    </tr>
                    <tr>
                        <th scope="row">Accusative</th>
                        <td>${d['accusative_singular']}</td>
                        <td>${d['accusative_plural']}</td>
                    </tr>
                    <tr>
                        <th scope="row">Instrumental</th>
                        <td>${d['instrumental_singular']}</td>
                        <td>${d['instrumental_plural']}</td>
                    </tr>
                    <tr>
                        <th scope="row">Prepositional</th>
                        <td>${d['prepositional_singular']}</td>
                        <td>${d['prepositional_plural']}</td>
                    </tr>
    
                </tbody>
            </table>
        `;
    
        html_raw_list.push(html_raw);
        }
        else if (pos == 'verb'){
            let html_raw =`
                <div class="close-button-wrapper">
                    <button class="close-button" onclick="close_btn_click_event()"><img src = "../../static/img/x-circle.png"></button>        
                </div>
                
                <p class="original-word">${d['infinitive']}</p>
            
                <p class="word-meaning-title">1. meaning</p>
                <p class="word-meaning">${d['meaning']}</p>
        
                <p class="pos-title">2. Part of Speech</p>
                <p class="pos">
                    <span>${d['pos']}</span>
                    <span>;</span>
                    <span>${d['imperfective_perfective']}</span>
                </p>
                
                <p class="word-table-title">3. Declension Table</p>

                <table class="word-table" style="text-align: center;">
                    <thead>
                        <tr>
                            <th scope="col" style="background-color: #33c9e4;">participles</th>
                            <th scope="col" style="background-color: #33c9e4;">present tense</th>
                            <th scope="col" style="background-color: #33c9e4;">past tense</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">active</th>
                            <td>${d['active_participle_present']}</td>
                            <td>${d['active_participle_past']}</td>
                        </tr>
                        <tr>
                            <th scope="row">passive</th>
                            <td>${d['participle_passive_present']}</td>
                            <td>${d['participle_passive_past']}</td>
                        </tr>
                        <tr>
                            <th scope="row">adverbial</th>
                            <td>${d['adverbial_participle_present']}</td>
                            <td>${d['adverbial_participle_past']}</td>
                        </tr>
                        <tr>
                            <th scope="row" style="background-color: #33c9e4;"></th>
                            <th scope="col" style="background-color: #33c9e4;">present tense</th>
                            <th scope="col" style="background-color: #33c9e4;">future tense</th>
                        </tr>
                        <tr>
                            <th scope="row">1st singular</th>
                            <td>${d['first-person_present_singular']}</td>
                            <td>${d['first-person_future_singular']}</td>
                        </tr>
                        <tr>
                            <th scope="row">2nd singular</th>
                            <td>${d['present_second-person_singular']}</td>
                            <td>${d['future_second-person_singular']}</td>
                        </tr>
                        <tr>
                            <th scope="row">3rd singular</th>
                            <td>${d['present_singular_third-person']}</td>
                            <td>${d['future_singular_third-person']}</td>
                        </tr>
                        <tr>
                            <th scope="row">1st plural</th>
                            <td>${d['first-person_plural_present']}</td>
                            <td>${d['first-person_future_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row">2nd plural</th>
                            <td>${d['plural_present_second-person']}</td>
                            <td>${d['future_plural_second-person']}</td>
                        </tr>
                        <tr>
                            <th scope="row">3rd plural</th>
                            <td>${d['plural_present_third-person']}</td>
                            <td>${d['future_plural_third-person']}</td>
                        </tr>
                        <tr>
                            <th scope="row" style="background-color: #33c9e4;">imperative</th>
                            <th scope="col" style="background-color: #33c9e4;">singular</th>
                            <th scope="col" style="background-color: #33c9e4;">plural</th>
                        </tr>
                        <tr>
                            <th scope="row"></th>
                            <td>${d['imperative_singular']}</td>
                            <td>${d['imperative_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row" style="background-color: #33c9e4;">past tense</th>
                            <th scope="col" style="background-color: #33c9e4;">singular</th>
                            <th scope="col" style="background-color: #33c9e4;">plural</th>
                        </tr>
                        <tr>
                            <th scope="row">masculine</th>
                            <td>${d['masculine_past_singular']}</td>
                            <td rowspan=3>${d['masculine_past_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row">feminine</th>
                            <td>${d['feminine_past_singular']}</td>

                        </tr>
                        <tr>
                            <th scope="row">neuter</th>
                            <td>${d['neuter_past_singular']}</td>
                        </tr>
                    </tbody>
                </table>
                `;
            html_raw_list.push(html_raw);
        }
        else if (pos == 'adjective'){
            let html_raw =`  
                <div class="close-button-wrapper">
                    <button class="close-button" onclick="close_btn_click_event()"><img src = "../../static/img/x-circle.png"></button>        
                </div>

                <p class="original-word">${d['masculine_nominative']}</p>
        
                <p class="word-meaning-title">1. meaning</p>
                <p class="word-meaning">${d['meaning']}</p>
        
                <p class="pos-title">2. Part of Speech</p>
                <p class="pos">adjective</p>
                
                <p class="word-table-title">3. Declension Table</p>

                <table class="word-table" style="text-align: center;">
                    <thead>
                        <tr>
                            <th colspan="2" style="background-color: #33c9e4;"></th>
                            <th scope="col" style="background-color: #33c9e4;">Masculine</th>
                            <th scope="col" style="background-color: #33c9e4;">Neuter</th>
                            <th scope="col" style="background-color: #33c9e4;">Feminine</th>
                            <th scope="col" style="background-color: #33c9e4;">plural</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row" colspan="2">Nominative</th>
                            <td>${d['masculine_nominative']}</td>
                            <td>${d['neuter_nominative']}</td>
                            <td>${d['feminine_nominative']}</td>
                            <td>${d['nominative_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row" colspan="2">Genitive</th>
                            <td colspan="2">${d['genitive_masculine_neuter']}</td>
                            <td>${d['feminine_genitive']}</td>
                            <td>${d['genitive_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row" colspan="2">Dative</th>
                            <td colspan="2">${d['dative_masculine_neuter']}</td>
                            <td>${d['dative_feminine']}</td>
                            <td>${d['dative_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row" rowspan="2">Accusative</th>
                            <td style="font-weight: bold;">Animate</td>
                            <td>${d['accusative_animate_masculine']}</td>
                            <td rowspan="2">${d['accusative_neuter']}</td>
                            <td rowspan="2">${d['accusative_feminine']}</td>
                            <td>${d['accusative_animate_plural']}</td>
                        </tr>
                        <tr>
                            <td style="font-weight: bold;">Inanimate</td>
                            <td>${d['masculine_nominative']}</td>
                            <td>${d['accusative_inanimate_masculine']}</td>
                        </tr>
                        <tr>
                            <th scope="row" colspan="2">Instrumental</th>
                            <td colspan="2">${d['instrumental_masculine_neuter']}</td>
                            <td>${d['feminine_instrumental']}</td>
                            <td>${d['instrumental_plural']}</td>
                        </tr>
                        <tr>
                            <th scope="row" colspan="2">Prepositional</th>
                            <td colspan="2">${d['masculine_neuter_prepositional']}</td>
                            <td>${d['feminine_prepositional']}</td>
                            <td>${d['plural_prepositional']}</td>
                        </tr>
                        <tr>
                            <th scope="row" colspan="2">Short-form</th>
                            <td>${d['masculine_short-form']}</td>
                            <td>${d['neuter_short-form']}</td>
                            <td>${d['feminine_short-form']}</td>
                            <td>${d['plural_short-form']}</td>
                        </tr>

        
                    </tbody>
                </table>
            `;
            html_raw_list.push(html_raw);

        }
        else if(pos == 'etc'){
            let html_raw = `
            <p class="original-word">${d['main_form']}</p>

            <p class="word-meaning-title">1. meaning</p>
            <p class="word-meaning">${d['meaning']}</p>

            <p class="pos-title">2. Part of Speech</p>
            <p class="pos">${d['pos']}</p>`;

            html_raw_list.push(html_raw);
        }

        else if(pos == 'no_result'){
            let html_raw =`<p class="no-result-msg">No result</p>`;
            html_raw_list.push(html_raw);
        }


    }

    const html_source = html_raw_list.join('\n');
    return html_source;
};


function wordcard_click_event(clicked_div, event) {   

    const search_word = clicked_div.querySelector('.word-title').innerText;
    const word_info_div = document.querySelector('.clicked-word')
    const request_url = window.location.href

//    clicked_div.classList.add(search_word);

    fetch(request_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            search_word: search_word, 
        }),
    })
        .then((response) => {
            response.json()
                .then(data => {
                    // 여기서 부터 데이터 하나씩 꺼내서 사전 테이블 생성
                    word_info_div.style.visibility  = 'visible';
                    word_info_div.style.display = 'inline-block';
                    word_info_div.style.border = 'black solid 1px';

                    html_source = declension_html(data)
                    word_info_div.innerHTML = html_source;
                });
    
        })
        .catch(console.log('server data successfully loaded'));
};

function close_btn_click_event(){
    const word_info_div = document.querySelector('.clicked-word');
    const word_cards = document.querySelectorAll('.word')
    word_info_div.style.visibility  = 'hidden';
    word_info_div.innerHTML = '';

}