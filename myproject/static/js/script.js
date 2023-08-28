let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick=()=>{
  menu.classList.toggle('bx-x');
  navbar.classList.toggle('open');
} ;


$(document).ready(function() {
  $("#toggleList").click(function() {
    $(".page-list").toggleClass("hidden");
  });
})