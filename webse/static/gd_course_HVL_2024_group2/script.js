// Select the image elements
const lifestyleImage = document.querySelector('.lifestyle-image');
const emissionsCard = document.querySelector('.emissions-card');
const ImpactChart = document.querySelector('.impact-chart');
const CategoryCard = document.querySelector('.category-card');

// Function to handle scroll events for lifestyle image
function handleScrollLifestyle() {
    const scrollTop = window.scrollY;
    const translateY = -0.1 * scrollTop;
    lifestyleImage.style.transform = `translate3d(0px, ${translateY}px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)`;
}

// Function to handle scroll events for emissions card
function handleScrollEmissions() {
    const scrollTop = window.scrollY;
    const translateY = -0.25 * scrollTop;
    emissionsCard.style.transform = `translate3d(0px, ${translateY}px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)`;
}

function handleScrollImpact() {
    const scrollTop = window.scrollY;
    const translateY = -0.2 * scrollTop;
    ImpactChart.style.transform = `translate3d(0px, ${translateY}px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)`;
}

function handleScrollCategory() {
    const scrollTop = window.scrollY;
    const translateY = -0.15 * scrollTop;
    CategoryCard.style.transform = `translate3d(0px, ${translateY}px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg)`;
}

// Attach scroll event listeners
window.addEventListener('scroll', handleScrollLifestyle);
window.addEventListener('scroll', handleScrollEmissions);
window.addEventListener('scroll', handleScrollImpact);
window.addEventListener('scroll', handleScrollCategory);

