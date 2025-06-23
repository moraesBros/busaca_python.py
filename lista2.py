# Função que recebe um dicionário de cidades e retorna um conjunto dos estados representados
def estados_representados(cidades: dict) -> set:
    return set(cidades.values())

# Função que recebe dois dicionários e retorna uma lista dos estados que estão em ambos,
# em ordem alfabética (cada estado aparece apenas uma vez)
def estados_comuns(dict1: dict, dict2: dict) -> list:
    # Extrai os estados dos dois dicionários
    estados1 = set(dict1.values())
    estados2 = set(dict2.values())
    
    # Calcula a interseção
    intersecao = estados1.intersection(estados2)
    
    # Retorna os estados comuns em uma lista ordenada alfabeticamente
    return sorted(list(intersecao))


# Exemplo de uso:

# Primeiro dicionário (cidades com seus estados)
cidades = {
    'Osasco': 'SP',
    'Caldas': 'MG',
    'Uberaba': 'MG',
    'Vitória': 'ES',
    'Cláudio': 'MG'
}

# Utiliza a função estados_representados para "gerar" o segundo dicionário.
# Neste exemplo, vamos criar um segundo dicionário similar a partir de outras cidades.
outras_cidades = {
    'São Paulo': 'SP',
    'Belo Horizonte': 'MG',
    'Rio de Janeiro': 'RJ',
    'Vitória': 'ES'
}

# Se o objetivo for usar o "resultado do primeiro programa" (ou seja, o conjunto retornado por estados_representados)
# como o segundo "dicionário", teremos que transformá-lo num dicionário com os estados como valor.
# Mas aqui, considerando que ambos são dicionários com o mesmo padrão (cidades: estados), 
# chamamos a função estados_comuns:
estados_em_comum = estados_comuns(cidades, outras_cidades)
print(estados_em_comum)  # Saída: ['ES', 'MG', 'SP']
