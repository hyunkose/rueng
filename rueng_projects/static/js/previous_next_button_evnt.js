function previous_article_button(){
    const article_id = window.location.href.split('/').slice(-2)[0];
    const view_option = window.location.href.split('/').slice(-3)[0];
    const website_type = window.location.href.split('/').slice(-4)[0];

    let request_url;


    if (website_type == 'yesasia_article_list'){
        request_url = '/yesasia/yesasia_article_previous/' + view_option + '/' + article_id;
    } else if (website_type == 'yandex_article_list'){
        request_url = '/yandex/yandex_article_previous/' + view_option + '/' + article_id;
    }

    const response = fetch(request_url, {
        method: 'GET',
    })
    .then((reponse) => reponse.json())
    .then(({ redirect_url }) => {
        window.location.href = redirect_url;
    })
    .catch(console.log('bad get request'))

}


function next_article_button(){
    const article_id = window.location.href.split('/').slice(-2)[0];
    const view_option = window.location.href.split('/').slice(-3)[0];
    const website_type = window.location.href.split('/').slice(-4)[0];
    
    let request_url;

    if (website_type == 'yesasia_article_list'){
        request_url = '/yesasia/yesasia_article_next/' + view_option + '/' + article_id;
    } else if (website_type == 'yandex_article_list'){
        request_url = '/yandex/yandex_article_next/' +  view_option + '/' + article_id;
    }

    const response = fetch(request_url, {
        method: 'GET',
    })
    .then((reponse) => reponse.json())
    .then(({ redirect_url }) => {
        window.location.href = redirect_url;
    })
    .catch(console.log('bad get request'))

}