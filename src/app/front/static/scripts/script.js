document.addEventListener("DOMContentLoaded", function () {
    const openModalButtons = document.querySelectorAll(".open-modal");
    const modal = document.getElementById("modal");
    const fade = document.getElementById("fade");
    const closeModalButton = document.getElementById("close-modal");

    openModalButtons.forEach(button => {
        button.addEventListener("click", function() {
            const name = button.getAttribute("data-name");
            const telefone = button.getAttribute("data-telefone");
            const partido = button.getAttribute("data-partido");
            const email = button.getAttribute("data-email");
            const img = button.getAttribute("data-img");

            // Preenche o modal com as informações do vereador
            modal.querySelector(".name p").textContent = name;
            modal.querySelector(".tel p").textContent = telefone;
            modal.querySelector(".partido p").textContent = partido;
            modal.querySelector(".email p").textContent = email;
            modal.querySelector("img").src = img;

            // Exibe o modal
            modal.classList.remove("hide");
            fade.classList.remove("hide");
        });
    });

    closeModalButton.addEventListener("click", function() {
        modal.classList.add("hide");
        fade.classList.add("hide");
    });

    fade.addEventListener("click", function() {
        modal.classList.add("hide");
        fade.classList.add("hide");
    });
});
