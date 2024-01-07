function view_option_select(event){
    selected_option = document.querySelector('#view-option-dropdown').value;

    if(window.location.href.includes('yesasia') === true){
        request_url = '/yesasia/yesasia_article_list/'+selected_option;
        window.location.href = request_url;
    }
    else if(window.location.href.includes('yandex') === true){
        request_url = '/yandex/yandex_article_list/'+selected_option;
        window.location.href = request_url;
    }
}