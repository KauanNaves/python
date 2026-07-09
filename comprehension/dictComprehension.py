# Dict Comprehension

'''
    - [ ]  Extração de Dados Estruturados
    
    Dada a lista de dicionários abaixo, que simula o retorno de uma API ou consulta a banco de dados:
    
    usuarios = [
        {"id": 101, "ativo": True},
        {"id": 102, "ativo": False},
        {"id": 103, "ativo": True},
        {"id": 104, "ativo": False}
    ]
    
    Escreva uma *list comprehension* para extrair e gerar uma lista que contenha estritamente os valores numéricos correspondentes à chave `"id"` dos usuários cujo status na chave `"ativo"` seja `True`. O resultado final deve ser `[101, 103]`.
'''

usuarios = [
    {"id": 101, "ativo": True},
    {"id": 102, "ativo": False},
    {"id": 103, "ativo": True},
    {"id": 104, "ativo": False}
]

list_usuarios = [usuario['id'] for usuario in usuarios if usuario['ativo']]

print(f"Os id's dos usuários ativos são: {list_usuarios=}")
