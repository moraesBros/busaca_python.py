def estados_representados(cidades: dict) -> set:
    # Extrai os valores do dicionário (que são as siglas dos estados)
    # e os converte em um conjunto para eliminar duplicatas.
    return set(cidades.values())

# Exemplo de uso
cidades = {
    'Osasco': 'SP',
    'Caldas': 'MG',
    'Uberaba': 'MG',
    'Vitória': 'ES',
    'Cláudio': 'MG'
}

estados = estados_representados(cidades)
print(estados)  # Exemplo de saída: {'ES', 'SP', 'MG'}
