
import random
def transforma_base(lista):
    dici = {}
    if len(lista) == 0:
        return dici
    for ex in lista:
        if ex['nivel'] not in dici:
            dici[ex['nivel']] = []
        dici[ex['nivel']].append(ex)
    return dici

def valida_questao(questao):
    # chaves = []
    dicio = {}
    chaves = (questao.keys())
    chaves = len(chaves)
    if 'titulo' not in questao.keys():
            dicio['titulo'] = 'nao_encontrado'
    if 'nivel' not in questao.keys():
            dicio['nivel'] = 'nao_encontrado'
    if 'opcoes' not in questao.keys():
            dicio['opcoes'] = 'nao_encontrado'
    if 'correta' not in questao.keys():
            dicio['correta'] = 'nao_encontrado'
    if chaves != 4:
        dicio['outro'] = 'numero_chaves_invalido'
    # Trabalha "Título"
    if 'titulo' in questao:
        if len(questao['titulo'].strip()) == 0:
            dicio['titulo'] = 'vazio'
    #trabalha 'nivel'
    if 'nivel'in questao:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            dicio['nivel'] = 'valor_errado'
    # Trabalha 'opcoes'
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
                dicio['opcoes'] = 'tamanho_invalido'
        elif 'A' not in questao['opcoes'] and 'B' not in questao['opcoes'] and 'C' not in questao['opcoes'] and 'D' not in questao['opcoes']:
                dicio['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        elif 'A' in questao['opcoes'].keys() and 'B' in questao['opcoes'].keys() and 'C' in questao['opcoes'].keys() and 'D' in questao['opcoes'].keys():
            for letra, texto in questao['opcoes'].items():
                if texto.strip() == '':
                    if 'opcoes'not in dicio:
                        dicio['opcoes'] ={}
                    dicio['opcoes'][letra] = 'vazia'
    # Trabalha "correta"
    if 'correta' in questao:
        if questao['correta'] != 'A'and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            dicio['correta'] = 'valor_errado'
    return dicio
ex = []
def sorteia_questao(questoes, nivel):
    for dif in questoes.keys():
        if dif == nivel:
            ex = questoes[dif]
    tam = len(ex)

        
    sorteio = random.randint(0,tam-1)
    return(ex[sorteio])

def sorteia_questao_inedita(questoes, nivel, lista):
    questao_sorteada = sorteia_questao(questoes, nivel)
    while questao_sorteada in lista:
        questao_sorteada = sorteia_questao(questoes, nivel)
    lista.append(questao_sorteada)
    return questao_sorteada