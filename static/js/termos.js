document.addEventListener("DOMContentLoaded", () => {

    const termos = document.querySelector(".termos-texto");
    const checkbox = document.getElementById("concordo");
    const botao = document.getElementById("iniciar");

    let leuTudo = false;

    function verificarLiberacao() {
        botao.disabled = !(leuTudo && checkbox.checked);
    }

    termos.addEventListener("scroll", () => {

        const chegouFim =
            termos.scrollTop + termos.clientHeight >= termos.scrollHeight - 5;

        if (chegouFim) {
            leuTudo = true;
        }

        verificarLiberacao();
    });

    checkbox.addEventListener("change", verificarLiberacao);

});