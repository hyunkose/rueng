function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function signup_submit(){
    
    const request_url = window.location.href;
    const csrfToken = getCookie('csrftoken');
    
    nickname = document.querySelector('.nickname-input-box').value;
    user_id = document.querySelector('.id-input-box').value;
    password1 = document.querySelector('.password1-input-box').value;
    password2 = document.querySelector('.password2-input-box').value;
    
    fetch(request_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            'first_name': nickname,
            'username': user_id,
            'password1': password1,
            'password2': password2,
        })
    })
    .then(() => {
        alert('Welcome to Rueng!');
        window.location.href = 'http://localhost:8000/accounts/login';
    })

}

function login_submit(){
    const request_url = window.location.href;
    const csrfToken = getCookie('csrftoken');
    
    user_id = document.querySelector('.userid-input-box').value;
    password = document.querySelector('.user-password-input-box').value;
    
    fetch(request_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            'user_id': user_id,
            'password': password,
        })
    })
    .then(() => {
        window.location.href = 'http://localhost:8000/'
    })
}

function move_to_signup_page(){
    window.location.href = 'http://localhost:8000/accounts/signup/'
}