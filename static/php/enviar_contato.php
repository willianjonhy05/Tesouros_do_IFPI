<?php
// Detalhes da conexão com o banco de dados
$servername = "sql308.infinityfree.com";  // Endereço do servidor MySQL
$username = "if0_41274817";              // Seu nome de usuário do MySQL
$password = "TesourosTeste26";           // Sua senha do MySQL
$dbname = "if0_41274817_votacao_db";     // Nome do banco de dados

// Conectar ao banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar se a conexão foi bem-sucedida
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Captura os dados do formulário (via POST)
$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];
$assunto = $_POST['assunto'];
$mensagem = $_POST['mensagem'];

// Prepara a consulta SQL para inserir os dados na tabela
$sql = "INSERT INTO contatos (nome, email, telefone, assunto, mensagem) 
        VALUES ('$nome', '$email', '$telefone', '$assunto', '$mensagem')";

// Verifica se a consulta foi executada com sucesso
if ($conn->query($sql) === TRUE) {
    header('Location: /templates/contato_enviado.html');
    exit; // Encerra o script após o redirecionamento
} else {
    echo "Erro ao enviar a mensagem: " . $conn->error;
}

// Fecha a conexão com o banco de dados
$conn->close();
?>