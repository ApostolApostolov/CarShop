
var searchBar = document.getElementById("search-bar")

$("filter-btn").on("click",function(){
    $("filter-menu").toggleClass("hidden");
});

window.addEventListener('resize', function(){
    console.log("resize");
    let windowsWidth = document.documentElement.clientWidth;
    if (windowsWidth <= 992){
        searchBar.classList.remove("show")
    }
    else {
        searchBar.classList.add("show")
    }
  });

window.addEventListener('resize',function(){
    let width = document.documentElement.clientWidth
    console.log(width);
});