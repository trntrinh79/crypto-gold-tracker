document.addEventListener("DOMContentLoaded", () => {
    // Scroll Reveal Effect
    const fadeElements = document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Chỉ chạy 1 lần
            }
        });
    }, {
        threshold: 0.1, // Hiện khi 10% phần tử xuất hiện trên màn hình
        rootMargin: "0px 0px -50px 0px"
    });

    fadeElements.forEach(el => observer.observe(el));
});
