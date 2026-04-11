// Função para preencher o modal com os dados digitados
function preencherModal() {

    // Aluno Atual
    document.getElementById("revNomeAluno").textContent =
        document.getElementById("NomeDoAlunoAtual").value;

    document.getElementById("revCursoAluno").textContent =
        document.getElementById("ModuloDoAlunoAtual").value;

    // Ex-Aluno
    document.getElementById("revNomeExAluno").textContent =
        document.getElementById("NomeDoExAluno").value;

    document.getElementById("revCursoExAluno").textContent =
        document.getElementById("CursoDoExAluno").value;

    document.getElementById("revFuncaoExAluno").textContent =
        document.getElementById("FuncaoDoExAluno").value;

    // Professor Atual
    document.getElementById("revNomeProfessor").textContent =
        document.getElementById("NomeDoProfessorAtual").value;

    document.getElementById("revDepartamentoProfessor").textContent =
        document.getElementById("DepartamentoDoProfessorAtual").value;

    // Ex-Professor
    document.getElementById("revNomeExProfessor").textContent =
        document.getElementById("NomeDoExProfessor").value;

    document.getElementById("revDepartamentoExProfessor").textContent =
        document.getElementById("DepartamentoDoExProfessor").value;

    document.getElementById("revFuncaoExProfessor").textContent =
        document.getElementById("FuncaoDoExProfessor").value;

    // Técnico Atual
    document.getElementById("revNomeTecnico").textContent =
        document.getElementById("NomeDoTecnicoAtual").value;

    document.getElementById("revFuncaoTecnico").textContent =
        document.getElementById("FuncaoDoTecnicoAtual").value;

    document.getElementById("revSetorTecnico").textContent =
        document.getElementById("SetorDoTecnicoAtual").value;

    // Ex-Técnico
    document.getElementById("revNomeExTecnico").textContent =
        document.getElementById("NomeDoExTecnico").value;

    document.getElementById("revFuncaoExTecnico").textContent =
        document.getElementById("FuncaoDoExTecnico").value;

    document.getElementById("revSetorExTecnico").textContent =
        document.getElementById("SetorDoExTecnico").value;

    document.getElementById("revFuncaoAtualExTecnico").textContent =
        document.getElementById("FuncaoAtualDoExTecnico").value;

    // Terceirizado
    document.getElementById("revNomeTerceirizado").textContent =
        document.getElementById("NomeDoTerceirizado").value;

    document.getElementById("revFuncaoTerceirizado").textContent =
        document.getElementById("FuncaoDoTerceirizado").value;

    document.getElementById("revSetorTerceirizado").textContent =
        document.getElementById("SetorDoTerceirizado").value;

    document.getElementById("revEmpresaTerceirizado").textContent =
        document.getElementById("EmpresaPrestadoraTerceirizado").value;
}


// Evento que executa quando o modal for aberto
document.getElementById('modalConfirmacao')
    .addEventListener('show.bs.modal', function () {
        preencherModal();
    });


// Função chamada ao confirmar
function finalizarVotacao() {
    alert("Votação confirmada com sucesso!");
    window.location.href = "obrigado.html";
}
