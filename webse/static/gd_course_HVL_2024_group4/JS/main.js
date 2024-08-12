/* CURSOR */
const cursor = document.querySelector(".cursor");
const EXPAND_TIMEOUT = 500;

document.addEventListener("mousemove", (e) => {
  cursor.style.top = e.pageY - window.scrollY - 10 + "px";
  cursor.style.left = e.pageX - window.scrollX - 10 + "px";
});

document.addEventListener("click", (e) => {
  cursor.classList.add("expand");
  setTimeout(() => {
    cursor.classList.remove("expand");
  }, EXPAND_TIMEOUT);
});

//menu

document.addEventListener("DOMContentLoaded", function () {
  var lastScrollTop = 0;
  var menuContainer = document.getElementById("menu-container");

  if (window.pageYOffset || document.documentElement.scrollTop === 0) {
    menuContainer.style.top = "0";
  }

  window.addEventListener(
    "scroll",
    function () {
      var currentScroll =
        window.pageYOffset || document.documentElement.scrollTop;

      if (currentScroll <= 0) {
        menuContainer.style.top = "0";
      } else if (currentScroll > lastScrollTop) {
        menuContainer.style.top = "-15%";
      } else {
        menuContainer.style.top = "0";
      }
      lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    },
    false
  );
});

//active

document.addEventListener("DOMContentLoaded", function () {
  // Get the current URL
  const currentUrl = window.location.href;

  // Select all 'a' elements inside 'nav > ul > li'
  const navLinks = document.querySelectorAll("nav ul li a");

  // Loop through each 'a' element
  navLinks.forEach((link) => {
    // Check if the 'href' of the current 'a' element matches the current URL
    if (link.href === currentUrl) {
      // Add the 'active' class to the 'a' element
      link.classList.add("active");
    }
  });
});
