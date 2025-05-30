const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".menu .nav");
const navLink = document.querySelectorAll(".nav-link");

hamburger.addEventListener("click", mobileMenu);
navLink.forEach(n => n.addEventListener("click", closeMenu));

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}


// const hamburger = document.querySelector(".hamburger");
// const navMenu = document.querySelector(".menu .nav");
// const navLink = document.querySelectorAll(".nav-link");

// hamburger.addEventListener("click", mobileMenu);
// navLink.forEach(n => n.addEventListener("click", closeMenu));

// function mobileMenu() {
//     hamburger.classList.toggle("active");
//     navMenu.classList.toggle("active");
// }

// function closeMenu() {  
//     hamburger.classList.remove("active");
//     navMenu.classList.remove("active");
// }