document.addEventListener("DOMContentLoaded", async function(event) {
    let res = await fetch('http://localhost:8000/api/categories/');
    let categories = await res.json();
    let categorySelectField = document.querySelector('[name="category"]');
    for (let category of categories){
        categorySelectField.innerHTML += 
        `<option value="${category.id}">${category.title}</option>`
    }
    res = await fetch('http://localhost:8000/api/tags/');
    let tags = await res.json();
    let tagSelectField = document.querySelector('[name="tags"]');
    for (let tag of tags){
        tagSelectField.innerHTML += 
        `<option value="${tag.id}">${tag.title}</option>`
    }
});

let recipeCreationForm = document.querySelector('form');

recipeCreationForm.addEventListener('submit', function(event){
    event.preventDefault();
    let formData = new FormData(recipeCreationForm);
    // let formData = {
    //     'title': recipeCreationForm.title.value,
    //     'description': recipeCreationForm.description.value,
    //     'tags'
    // }
    fetch('http://localhost:8000/api/recipes/', {
        method: 'POST',
        headers:{
            // 'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMzAzMzc0LCJpYXQiOjE2NzIzMDIxNzQsImp0aSI6ImE0YzU2ZDQ1MGJhZjQxNDU5MTE3ZWQxZjRlMjY1NzBkIiwidXNlcl9pZCI6MX0.titH46FsN4pbgMb7ptiQTFtZU0CuIm8OMqw3w1JwMH0'
        },
        body: formData,
    });
})