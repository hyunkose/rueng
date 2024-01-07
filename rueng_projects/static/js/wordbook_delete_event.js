function delete_word(event){
    const confirm_result = window.confirm("are you sure you want to delete the word from the wordbook?");
    const request_url = window.location.href;
    const delete_word_id = event.target.closest('.word').classList[1];

    if(confirm_result === true){
        fetch(request_url,{
            method: 'DELETE',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(
                {
                    delete_word_id: delete_word_id,
                })

        })
        .then(() => {
            window.location.href='';
            alert('successfully deleted')
        })
        .catch(console.log('delete failed'));
    };

}