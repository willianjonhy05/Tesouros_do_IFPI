import re

def limpar_cpf(cpf):
    return re.sub(r'\D', '', cpf)


def formatar_cpf(cpf):
    cpf = limpar_cpf(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    # Validação do segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{dig1}{dig2}"