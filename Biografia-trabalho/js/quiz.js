// Clique no botão "Ver Resultado"
document.getElementById("verResultado").addEventListener("click", function() {
  let respostasCorretas = {
    q1: "q1b",
    q2: "q2a",
    q3: "q3b",
    q4: "q4c",
    q5: "q5c"
  };

  let pontuacao = 0;

  // Limpa cores anteriores
  document.querySelectorAll(".option").forEach(opt => {
    opt.style.backgroundColor = "";
  });

  // Verifica respostas
  for (let pergunta in respostasCorretas) {
    let respostaCorreta = respostasCorretas[pergunta];
    let selecionada = document.querySelector(`input[name="${pergunta}"]:checked`);
    if (selecionada) {
      let labelSelecionada = selecionada.parentElement;
      if (selecionada.id === respostaCorreta) {
        pontuacao++;
        labelSelecionada.style.backgroundColor = "rgba(0, 255, 0, 0.3)"; // verde
      } else {
        labelSelecionada.style.backgroundColor = "rgba(255, 0, 0, 0.3)"; // vermelho
      }
    }
  }

  // Mostra a div do resultado junto com texto e botão
  let resultDiv = document.getElementById("result");
  let resultadoTexto = document.getElementById("resultado");

  // Texto de resultado com incentivo e quebra de linha
  resultadoTexto.innerHTML = `PARABÉNS! Você acertou ${pontuacao} de 5 perguntas! 🎯\nVocê é muito inteligente e está arrasando nos conhecimentos! 💡✨`;

  resultDiv.style.display = "block"; // mostra a div inteira (texto + botão)
});

// Clique no botão "Tentar novamente"
document.getElementById("tente").addEventListener("click", function(event) {
  event.preventDefault(); // evita que o href # navegue

  // 1. Limpa todos os radios
  document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.checked = false;
  });

  // 2. Limpa cores das opções
  document.querySelectorAll(".option").forEach(opt => {
    opt.style.backgroundColor = "";
  });

  // 3. Limpa o texto do resultado
  document.getElementById("resultado").textContent = "";

  // 4. Esconde a div do resultado junto com o botão
  document.getElementById("result").style.display = "none";

  // 5. Rola para o topo da página
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
