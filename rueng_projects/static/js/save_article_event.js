function save_article(){
    const article_save_button = document.querySelector('.article-save-button');
    const article_state = article_save_button.innerText;
    const checked_img = document.querySelector('.read-checked');
    const page_url = window.location.href;
    const request_url = page_url;

    if(article_state === 'done reading?'){
        const request_type = 'article_save';

        fetch(request_url, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                request_type: request_type,
            }),
        })
            .then((response) => {
                response.json()
                    .then(data => {
                        // 저장 결과에 따른 boolean 값 받기
                        save_result = data['save_result'];

                        if (save_result === 'success'){
                            checked_img.style.display = 'inline';
                            article_save_button.innerText = 'finished reading!';
                        };

                    });
        
            })
            .catch(console.log('server data successfully loaded'));
    } else if (article_state === 'finished reading!'){
        const request_type = 'article_unsave';

        fetch(request_url, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                request_type: request_type,
            }),
        })
            .then((response) => {
                response.json()
                    .then(data => {
                        // 저장 결과에 따른 boolean 값 받기
                        save_result = data['save_result'];

                        if (save_result === 'success'){
                            checked_img.style.display = 'none';
                            article_save_button.innerText = 'done reading?';
                        };

                    });
        
            })
            .catch(console.log('server data successfully loaded'));
    };
}