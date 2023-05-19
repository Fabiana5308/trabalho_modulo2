candidato1 = {'nome': 'Capitão Caverna', 'entrevista': 8, 'teste teórico': 7, 'teste prático': 6, 'avaliação Soft skills': 9}
candidato2 = {'nome': 'Esqueleto', 'entrevista': 6, 'teste teórico': 7, 'teste prático': 8, 'avaliação Soft skills': 7}
candidato3 = {'nome': 'Zé Colmeia', 'entrevista': 9, 'teste teórico': 5, 'teste prático': 8, 'avaliação Soft skills': 8}
candidato4 = {'nome': 'Mestre dos Magos', 'entrevista': 4, 'teste teórico': 4, 'teste prático': 5, 'avaliação Soft skills': 4}
candidato5 = {'nome': 'Harry Potter', 'entrevista': 7, 'teste teórico': 6, 'teste prático': 8, 'avaliação Soft skills': 8}

#Armazenando os resultados dos candidatos em uma lista
lista_candidatos = [candidato1, candidato2, candidato3, candidato4, candidato5]

#Definindo função que busca os candidatos de acordo com as notas do usuário
def buscar_candidatos_por_notas():
    notas_entrevista = int(input('Digite a nota mínima da entrevista: '))
    notas_teste_teórico = int(input('Digite a nota mínima do teste teórico: '))
    notas_teste_prático = int(input('Digite a nota mínima do teste prático: '))
    notas_avaliação_soft_skills = int(input('Digite a nota mínima da avaliação de soft skills: '))

    candidatos_compatíveis = []
    for candidato in lista_candidatos:
       if (candidato['entrevista'] >= notas_entrevista) and (candidato['teste teórico'] >= notas_teste_teórico) and (candidato['teste prático'] >= notas_teste_prático) and (candidato['avaliação Soft skills'] >= notas_avaliação_soft_skills):
            candidatos_compatíveis.append(candidato)

    return candidatos_compatíveis

#Exemplo de uso da função
candidatos_compatíveis = (buscar_candidatos_por_notas())
if len(candidatos_compatíveis) > 0:
    for candidato in candidatos_compatíveis:
        print(f"{candidato['nome']} - e{candidato['entrevista']}_t{candidato['teste teórico']}_p{candidato['teste prático']}_s{candidato['avaliação Soft skills']}")
else:
    print('Nenhum candidato encontrado.')