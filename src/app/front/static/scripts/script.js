document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('modal');
    const fade = document.getElementById('fade');
    const modalNome = document.getElementById('modal-nome');
    const modalImg = document.getElementById('modal-img');
    const modalTel = document.getElementById('modal-tel');
    const modalPartido = document.getElementById('modal-partido');
    const modalEmail = document.getElementById('modal-email');
    const openModalButtons = document.querySelectorAll('.open-modal');
    const closeModalButton = document.getElementById('close-modal');
    const aboutMoreButton = document.querySelector('.aboutmore');
  
    openModalButtons.forEach(button => {
       button.addEventListener('click', () => {
          // Preencher as informações no modal
          modalNome.textContent = button.getAttribute('data-nome');
          modalImg.src = button.getAttribute('data-img');
          modalTel.textContent = button.getAttribute('data-tel');
          modalPartido.textContent = button.getAttribute('data-partido');
          modalEmail.textContent = button.getAttribute('data-email');
  
          // Atualizar o link "Saiba mais" com o ID correto
          const vereadorId = button.getAttribute('data-id');
  
          // Mostrar o modal
          modal.classList.remove('hide');
          fade.classList.remove('hide');
  
          // Adicionar evento de clique ao botão "Saiba mais"
          aboutMoreButton.addEventListener('click', function () {
             window.location.href = `/detalhes/${vereadorId}`;
          });
       });
    });
  
    // Fechar modal ao clicar no botão "Voltar"
    closeModalButton.addEventListener('click', () => {
       modal.classList.add('hide');
       fade.classList.add('hide');
    });
  
    // Fechar modal ao clicar fora dele (no fundo escuro "fade")
    fade.addEventListener('click', () => {
       modal.classList.add('hide');
       fade.classList.add('hide');
    });
  });

// Captura as estrelas e define a avaliação inicial
const stars = document.querySelectorAll('.star');
let currentRating = 0;

// Função para atualizar as estrelas com base na avaliação
function updateStars(rating) {
    stars.forEach((star, index) => {
        if (index < rating) {
            star.style.color = 'gold'; 
            star.classList.add('selected');
        } else {
            star.style.color = 'gray'; 
            star.classList.remove('selected');
        }
    });
}

// Adiciona o evento de clique para cada estrela
stars.forEach(star => {
    star.addEventListener('click', function() {
        currentRating = parseInt(star.getAttribute('data-index'));
        updateStars(currentRating); 
    });

    star.addEventListener('mouseover', function() {
        updateStars(parseInt(star.getAttribute('data-index')));
    });

    star.addEventListener('mouseout', function() {
        updateStars(currentRating); 
    });
});

// Inicializa as estrelas como vazias
updateStars(0);

document.querySelector("form").addEventListener("submit", function(e) {
   if (currentRating === 0) {
       e.preventDefault();
       alert("Por favor, selecione uma avaliação.");
       return;
   }

   const inputRating = document.createElement("input");
   inputRating.type = "hidden";
   inputRating.name = "come_avaliacao"; 
   inputRating.value = currentRating;  
   this.appendChild(inputRating); 
});