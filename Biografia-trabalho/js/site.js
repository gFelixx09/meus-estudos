
const elementos= document.querySelectorAll('.scroll-fade');

const observer = new IntersectionObserver((entradas) => {
    entradas.forEach((entrada) => {
      if(entrada.isIntersecting) {
        entrada.target.classList.add('visivel');
      }
    });
});
elementos.forEach(el => observer.observe(el));