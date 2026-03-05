document.addEventListener("DOMContentLoaded", function () {
    const checkbox = document.getElementById("concordo");
    const botao = document.getElementById("iniciar");

    checkbox.addEventListener("change", function () {
        if (checkbox.checked) {
            botao.disabled = false;
            botao.classList.add("ativo");
        } else {
            botao.disabled = true;
            botao.classList.remove("ativo");
        }
    });

    botao.addEventListener("click", function () {
        if (checkbox.checked) {
            window.location.href = "votacao.html";
        }
    });
});