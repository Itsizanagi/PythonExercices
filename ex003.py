entrada = input("Digite algo: ")

# Obtém o tipo primitivo da entrada
tipo_primitivo = type(entrada).__name__

# Obtém todas as informações possíveis sobre a entrada
informacoes = {
    'Tipo primitivo': tipo_primitivo,
    'Tamanho': len(entrada),
    'É alfanumérico?': entrada.isalnum(),
    'É numérico?': entrada.isnumeric(),
    'É alfabético?': entrada.isalpha(),
    'É maiúsculo?': entrada.isupper(),
    'É minúsculo?': entrada.islower(),
    'É capitalizado?': entrada.istitle(),
}

# Exibe as informações na tela
print("=== Informações sobre a entrada ===")
for chave, valor in informacoes.items():
    print(f'{chave}: {valor}')