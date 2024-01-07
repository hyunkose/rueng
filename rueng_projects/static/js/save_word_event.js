function save_word_event(){
    const page_url = window.location.href
    const save_word = document.querySelector('div.dictionary-search input.search_box').value;
    const request_type = 'word_save';
    const request_url = page_url;


    fetch(request_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            save_word: save_word,
            request_type: request_type, 
        }),
    })
        .then((response) => {
            response.json()
                .then(data => {
                    // 저장 결과에 따른 boolean 값 받기
                    save_result = data['save_result']

                    if (save_result === 'success'){
                        word_saved_checked = document.querySelector('.word-saved-checked');
                        word_saved_checked_label = document.querySelector('.word-saved-checked-label');
                        word_saved_checked.style.display = 'inline';
                        word_saved_checked_label.style.display = 'inline';
                    }
                    else if (save_result === 'duplicate_word'){
                        alert('already added word!');
                    }
                });
    
        })
        .catch(console.log('word successfully added'));
};