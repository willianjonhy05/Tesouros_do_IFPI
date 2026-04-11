document.addEventListener("DOMContentLoaded", function () {
    const botaoModal = document.getElementById("confirmarVoto");
    const resumoDiv = document.getElementById("resumoVoto");
    const form = document.getElementById("formVoto");

    botaoModal.addEventListener("click", () => {
        resumoDiv.innerHTML = ""; // limpa antes de montar

        const campos = form.querySelectorAll("input, textarea, select");

        campos.forEach(campo => {
            if (campo.type === "hidden") return;

            let label = form.querySelector(`label[for="${campo.id}"]`);
            let nomeCampo = label ? label.innerText : campo.name;

            let valor = "";

            if (campo.type === "checkbox") {
                valor = campo.checked ? "Sim" : "Não";
            } else if (campo.type === "radio") {
                if (!campo.checked) return;
                valor = campo.value;
            } else {
                valor = campo.value;
            }

            if (valor) {
                resumoDiv.innerHTML += `
                    <div class="border rounded p-2 mb-2">
                        <strong>${nomeCampo}:</strong><br>
                        <span>${valor}</span>
                    </div>
                `;
            }
        });
    });
});