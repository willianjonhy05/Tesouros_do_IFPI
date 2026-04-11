
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const inputs = form.querySelectorAll("input[required]");
    const botaoSubmit = form.querySelector("button[type='submit']");

    function verificarCampos() {
        let todosPreenchidos = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                todosPreenchidos = false;
            }
        });

        botaoSubmit.disabled = !todosPreenchidos;
    }

    // Escuta mudanças em todos os inputs
    inputs.forEach(input => {
        input.addEventListener("input", verificarCampos);
    });
});
