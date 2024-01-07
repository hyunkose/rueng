function dictionary_icon_event(){
    const dictionary_icon = document.querySelector(".dictionary-icon>img");
    const dictionary_div  = document.querySelector('aside');

    if (dictionary_div.style.display == 'none'){
        dictionary_div.style.display = 'block';

    } else if(dictionary_div.style.display == 'block'){
        dictionary_div.style.display = 'none';
    }
};