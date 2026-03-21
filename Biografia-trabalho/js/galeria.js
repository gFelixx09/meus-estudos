const imagens = document.querySelectorAll('.carousel img');
let index = 0;

function mostrarProximaImagem() {
  imagens[index].classList.remove('active'); // esconde a imagem atual
  index = (index + 1) % imagens.length;     // próximo índice (looping)
  imagens[index].classList.add('active');   // mostra a próxima imagem
}

// Troca a imagem a cada 3 segundos
setInterval(mostrarProximaImagem, 3000);
