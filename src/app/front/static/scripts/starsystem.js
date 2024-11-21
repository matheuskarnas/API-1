//Arquivo criado para testar a função de notas utilizando estrelas na cessão comentarios.//
//Caso seja melhor ter menos arquivos js pode posteriormente ser trasferido para o arquivo scrip.js//

// Captura as estrelas e define a avaliação inicial
const stars = document.querySelectorAll('.star');
let currentRating = 0;

// Função para atualizar as estrelas com base na avaliação
function updateStars(rating) {
    stars.forEach((star, index) => {
        if (index < rating) {
            star.style.color = 'gold'; 
        } else {
            star.style.color = 'gray'; 
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

