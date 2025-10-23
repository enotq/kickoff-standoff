function initCarousel() {
    let currentSlide = 0;
    const slides = document.querySelectorAll('.carousel-slide');
    const indicators = document.querySelectorAll('.indicator');
    const totalSlides = slides.length;
    let autoSlideInterval;

    if (totalSlides === 0) return; // No slides

    function showSlide(index) {
        slides.forEach(slide => {
            slide.classList.remove('opacity-100');
            slide.classList.add('opacity-0');
        });
        slides[index].classList.remove('opacity-0');
        slides[index].classList.add('opacity-100');

        indicators.forEach(ind => {
            ind.classList.remove('bg-white');
            ind.classList.add('bg-white', 'bg-opacity-50');
        });
        indicators[index].classList.remove('bg-opacity-50');
        indicators[index].classList.add('bg-white');
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(currentSlide);
    }

    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 4000);
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    document.getElementById('nextBtn')?.addEventListener('click', (e) => {
        e.preventDefault();
        nextSlide();
        stopAutoSlide();
        startAutoSlide();
    });

    document.getElementById('prevBtn')?.addEventListener('click', (e) => {
        e.preventDefault();
        prevSlide();
        stopAutoSlide();
        startAutoSlide();
    });

    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            currentSlide = index;
            showSlide(currentSlide);
            stopAutoSlide();
            startAutoSlide();
        });
    });

    startAutoSlide();

    document.getElementById('carouselSlides')?.addEventListener('mouseenter', stopAutoSlide);
    document.getElementById('carouselSlides')?.addEventListener('mouseleave', startAutoSlide);
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCarousel);
} else {
    initCarousel();
}