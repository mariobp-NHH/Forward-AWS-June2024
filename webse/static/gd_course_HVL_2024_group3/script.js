document.addEventListener("DOMContentLoaded", function() {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                const targetElement = entry.target;
                setTimeout(() => {
                    targetElement.classList.add("visible-element");
                }, index * 1000); // Forsinkelse øker med 1000 ms for hvert element
            }else {
                    // Elementet forlater viewporten, skjul det igjen
                    entry.target.classList.remove("visible-element");
                }
        });
    }, { threshold: 0.1 });

    const hiddenElements = document.querySelectorAll(".hidden-element");
    hiddenElements.forEach((el) => observer.observe(el));
});