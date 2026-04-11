(function () {

    const cpfSalvo = localStorage.getItem("cpf_validado");

    // Se não existir ou estiver inválido
    if (!cpfSalvo || cpfSalvo.length !== 11) {
        console.log("CPF não encontrado. Redirecionando...");
        window.location.replace("../index.html");
    }

})();