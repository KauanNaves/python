# List Comprehension

'''
    - [x]  Filtragem e Transformação Matemática
    
    Dada a lista: `numeros = [1,2,3,4,5,6,7,8,9,10]`, escreva uma list comprehension que gere uma nova lista contendo o cubo ³ apenas dos números que são ímpares.
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_cubo = [x**3 for x in numeros if (x % 2) != 0]

print(f"Os {numeros=} ímpares elevados ao cubo são: {numeros_cubo=}")

print("***" * 20)

'''
    - [x]  Mapeamento de Strings
    
    Dada a lista `tecnologias = ["python", "flask", "sql", "react", "css"]`, construa um dicionário utilizando *dict comprehension* onde a chave seja o nome da tecnologia convertido para letras maiúsculas (método `.upper()`) e o valor seja o número de caracteres da respectiva string.
'''

tecnologias = ["python", "flask", "sql", "react", "css"]

dict_tecnologias = {tecno.upper():len(tecno) for tecno in tecnologias}

print(f"Lista original: {tecnologias=} \nDict Comprehension: {dict_tecnologias=}")

