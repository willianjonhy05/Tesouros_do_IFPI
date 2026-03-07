document.addEventListener("DOMContentLoaded", function () {

    const termos = document.querySelector(".termos-texto");
    const checkbox = document.getElementById("concordo");
    const botao = document.getElementById("iniciar");

    let leuTudo = false;

    function verificarLiberacao() {
        if (leuTudo && checkbox.checked) {
            botao.disabled = false;
            botao.classList.add("ativo");
        } else {
            botao.disabled = true;
            botao.classList.remove("ativo");
        }
    }

    termos.addEventListener("scroll", function () {

        if (termos.scrollTop + termos.clientHeight >= termos.scrollHeight - 5) {
            leuTudo = true;
            verificarLiberacao();
        }

    });

    checkbox.addEventListener("change", verificarLiberacao);

});