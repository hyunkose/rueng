function view_option_select(event){
    selected_option = document.querySelector('#view-option-dropdown').value;

    if(window.location.href.includes('yesasia') === true){
        request_url = 'http://localhost:8000/yesasia_article_list/'+selected_option;
        window.location.href = request_url;
    }
    else if(window.location.href.includes('yandex') === true){
        request_url = 'http://localhost:8000/yandex_article_list/'+selected_option;
        window.location.href = request_url;
    }
}