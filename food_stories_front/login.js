let loginForm = document.querySelector('form');

loginForm.addEventListener('submit', async function(event){
    event.preventDefault();
    
    let formData = {
        'username': loginForm.username.value,
        'password': loginForm.password.value
    }
    let res = await fetch('http://127.0.0.1:8000/api/auth/token/', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
    });
    let resData = await res.json();
    if (!res.ok) {
        alert(resData.detail);
    }else{
        localStorage.setItem('token', resData.access);
        window.location = 'index.html';
    }
    // console.log(await res.json());
})