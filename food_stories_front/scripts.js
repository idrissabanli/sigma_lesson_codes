document.addEventListener("DOMContentLoaded", async function(event) {
    let res = await fetch('http://localhost:8000/api/recipes/');
    let recipes = await res.json();
    let recipeSection = document.querySelector('#recipes');
    for (let recipe of recipes){
        recipeSection.innerHTML += `
        <div class="col-3 mb-3">
                <div class="card" >
                    <img src="${recipe.image}" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${recipe.title} ${recipe.category.title}</h5>
                      <p class="card-text">${recipe.description}</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
        `
    }
});
