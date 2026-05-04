// Nav scroll effect
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });
}

// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const navMobile = document.getElementById('navMobile');
if (navToggle && navMobile) {
  navToggle.addEventListener('click', () => {
    navMobile.classList.toggle('open');
    const spans = navToggle.querySelectorAll('span');
    const isOpen = navMobile.classList.contains('open');
    spans[0].style.transform = isOpen ? 'rotate(45deg) translate(5px, 5px)' : '';
    spans[1].style.transform = isOpen ? 'rotate(-45deg) translate(5px, -5px)' : '';
  });
}

// Scroll fade-in
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(
  '.step, .governess-card, .directory-card, .process-step, .pricing-card, .compare-col, .philosophy-quote, .stat, .families-item'
).forEach((el, i) => {
  el.classList.add('fade-in');
  el.style.transitionDelay = `${(i % 4) * 80}ms`;
  observer.observe(el);
});

// Auto-dismiss flash messages
const flashMessages = document.getElementById('flashMessages');
if (flashMessages) {
  setTimeout(() => {
    flashMessages.style.transition = 'opacity 0.5s ease';
    flashMessages.style.opacity = '0';
    setTimeout(() => flashMessages.remove(), 500);
  }, 4000);
}
