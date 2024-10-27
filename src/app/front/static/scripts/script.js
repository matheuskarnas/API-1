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
