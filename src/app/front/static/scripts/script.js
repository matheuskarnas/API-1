document.addEventListener('DOMContentLoaded', function () {
    const openModalButtons = document.querySelectorAll('.open-modal');
    const modal = document.getElementById('modal');
    const fade = document.getElementById('fade');
    const closeModalButton = document.getElementById('close-modal');
  
    // Elementos do modal a serem preenchidos dinamicamente
    const modalNome = document.getElementById('modal-nome');
    const modalImg = document.getElementById('modal-img');
    const modalTel = document.getElementById('modal-tel');
    const modalPartido = document.getElementById('modal-partido');
    const modalEmail = document.getElementById('modal-email');
  
    // Função para abrir o modal e preencher as informações
    openModalButtons.forEach(button => {
      button.addEventListener('click', function () {
        const nome = this.getAttribute('data-nome');
        const img = this.getAttribute('data-img');
        const tel = this.getAttribute('data-tel');
        const partido = this.getAttribute('data-partido');
        const email = this.getAttribute('data-email');
  
        // Preencher os dados no modal
        modalNome.textContent = nome;
        modalImg.src = img;
        modalTel.textContent = tel;
        modalPartido.textContent = partido;
        modalEmail.textContent = email;
  
        // Mostrar o modal e o fundo escurecido
        modal.classList.remove('hide');
        fade.classList.remove('hide');
      });
    });
  
    // Função para fechar o modal
    closeModalButton.addEventListener('click', function () {
      modal.classList.add('hide');
      fade.classList.add('hide');
    });
  
    // Fechar o modal ao clicar no fundo escurecido
    fade.addEventListener('click', function () {
      modal.classList.add('hide');
      fade.classList.add('hide');
    });
  });
  