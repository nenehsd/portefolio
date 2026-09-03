/* =========================================================
   Portfolio — Nene H. S. Diallo
   Interactions & animations
   ========================================================= */
(function () {
  'use strict';

  /* ---------- Header : ombre au scroll ---------- */
  const header = document.getElementById('header');
  const toTop = document.getElementById('to-top');

  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 10);
    toTop.classList.toggle('show', window.scrollY > 600);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  toTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* ---------- Menu mobile ---------- */
  const burger = document.getElementById('burger');
  const nav = document.getElementById('nav');

  const closeNav = () => {
    nav.classList.remove('open');
    burger.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
  };

  burger.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    burger.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', String(open));
  });

  nav.querySelectorAll('a').forEach((a) => a.addEventListener('click', closeNav));
  document.addEventListener('click', (e) => {
    if (nav.classList.contains('open') && !nav.contains(e.target) && !burger.contains(e.target)) closeNav();
  });

  /* ---------- Apparition au scroll (reveal) ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  const revealObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );
  revealEls.forEach((el) => revealObs.observe(el));

  /* ---------- Compteurs animés ---------- */
  const counters = document.querySelectorAll('[data-count]');
  const counterObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = parseInt(el.dataset.count, 10);
        const duration = 1400;
        const start = performance.now();
        const tick = (now) => {
          const p = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased);
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        counterObs.unobserve(el);
      });
    },
    { threshold: 0.6 }
  );
  counters.forEach((el) => counterObs.observe(el));

  /* ---------- Barres de langues ---------- */
  const bars = document.querySelectorAll('.bar i');
  const barObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.style.width = entry.target.dataset.level + '%';
        barObs.unobserve(entry.target);
      });
    },
    { threshold: 0.5 }
  );
  bars.forEach((el) => barObs.observe(el));

  /* ---------- Lien de nav actif ---------- */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const setActive = (id) => {
    navLinks.forEach((link) => {
      link.classList.toggle('active', link.getAttribute('href') === '#' + id);
    });
  };

  const sectionObs = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) setActive(entry.target.id);
      });
    },
    { rootMargin: '-45% 0px -50% 0px' }
  );
  sections.forEach((s) => sectionObs.observe(s));

  /* ---------- Effet machine à écrire ---------- */
  const typedEl = document.getElementById('typed');
  const roles = [
    'Technicienne agricole',
    'Spécialiste Suivi & Évaluation',
    'Développement rural',
    'Fondatrice de Sadiya Digital Agri'
  ];
  let roleIndex = 0;
  let charIndex = 0;
  let deleting = false;

  const typeLoop = () => {
    const word = roles[roleIndex];
    charIndex += deleting ? -1 : 1;
    typedEl.textContent = word.slice(0, charIndex);

    let delay = deleting ? 40 : 75;
    if (!deleting && charIndex === word.length) {
      delay = 1900;
      deleting = true;
    } else if (deleting && charIndex === 0) {
      deleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      delay = 400;
    }
    setTimeout(typeLoop, delay);
  };
  typeLoop();

  /* ---------- Formulaire de contact (mailto) ---------- */
  const form = document.getElementById('contact-form');
  const note = document.getElementById('form-note');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('f-name').value.trim();
    const email = document.getElementById('f-email').value.trim();
    const subject = document.getElementById('f-subject').value.trim() || 'Message depuis votre portfolio';
    const message = document.getElementById('f-message').value.trim();

    if (!name || !email || !message) {
      note.textContent = 'Merci de renseigner votre nom, votre email et votre message. 🌿';
      return;
    }

    const body = encodeURIComponent(
      message + '\n\n—\n' + name + '\n' + email
    );
    window.location.href =
      'mailto:diallonene2000@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + body;

    note.textContent = 'Votre messagerie s’ouvre… Merci ' + name + ' ! 🌱';
    form.reset();
  });

  /* ---------- Année du footer ---------- */
  document.getElementById('year').textContent = new Date().getFullYear();
})();
