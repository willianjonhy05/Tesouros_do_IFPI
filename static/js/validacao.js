document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.getElementById("cpf");
    const form = document.querySelector("form");
    const button = form.querySelector("button");

    // Estado inicial
    button.disabled = true;
    
    button.style.cursor = "not-allowed";

    // Máscara + validação em tempo real
    cpfInput.addEventListener("input", function (e) {
        let value = e.target.value.replace(/\D/g, "");
        value = value.substring(0, 11);

        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

        e.target.value = value;

        const cpfLimpo = value.replace(/\D/g, "");

        if (validarCPF(cpfLimpo)) {
            button.disabled = false;
            button.style.backgroundColor = "green";            
            button.style.cursor = "pointer";
        } else {
            button.disabled = true;
            button.style.cursor = "not-allowed";

            
        }
    });


    function validarCPF(cpf) {
        if (cpf.length !== 11) return false;
        if (/^(\d)\1+$/.test(cpf)) return false;

        let soma = 0;
        let resto;

        for (let i = 1; i <= 9; i++)
            soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);

        resto = (soma * 10) % 11;
        if (resto === 10 || resto === 11) resto = 0;
        if (resto !== parseInt(cpf.substring(9, 10))) return false;

        soma = 0;

        for (let i = 1; i <= 10; i++)
            soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);

        resto = (soma * 10) % 11;
        if (resto === 10 || resto === 11) resto = 0;
        if (resto !== parseInt(cpf.substring(10, 11))) return false;

        return true;
    }
});
