
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

def valida_questoes(lista):
    erros = []
    for questao in lista:
        valida = valida_questao(questao)
        erros.append(valida)
    return erros
        
    
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

def questao_para_texto(questao, num):
    for j, i in questao.items():
        if j == 'titulo':
            ti = i 
        elif j == 'opcoes':
            for op, resp in questao['opcoes'].items():
                if op == 'A':
                    a = resp
                elif op == 'B':
                    b = resp
                elif op == 'C':
                    c = resp
                elif op == 'D':
                    d = resp


    pergunta = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}'.format(num,ti,a,b,c,d)

    return pergunta

def gera_ajuda(questao):
    i = 1
    maximo = 3
    dica = []
    opcoes = [ "A", "B", "C", "D"]
    opcoes.remove(questao["correta"])
    num_dicas = random.randint(1,2)
    sorteio = random.randint(1,maximo-1)
    while num_dicas >= i:
        sorteio = random.randint(0,maximo-1)
        if questao["opcoes"][opcoes[sorteio]] not in dica:
            dica.append(questao["opcoes"][opcoes[sorteio]])
            i += 1
    traco = " | ".join(dica)
    return f"DICA:\nOpções certamente erradas: {traco}"

quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}

         {'titulo': 'Considere que os ângulos internos de um triângulo formam uma progressão aritmética. Dado que a,b,c são as medidas dos lados do triângulo, sendo a < b, é correto afirmar que:',
         'nivel': 'dificil',
         'opcoes': {'A': 'b^2 + ac = a^2 + c^2 ','B': 'a^2 + bc = b^2 + c^2 ', 'C': 'a^2 – bc = b^2 + c^2', 'D': 'b^2 – ac = a^2 + c^2' },
         'correta': 'A'}

        
        ] 
pular = 3
ajuda = 2


#introducao = input('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
print ('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
nome = input('\n Qual o seu nome?')
print ('\n OK {0}, você tem direito a pular {1} vezes e {2} ajudas! \n As opçoes de resposta são "A","B","C","D","ajuda","pula" e "parar" !'.format(nome,pular,ajuda))
enter = input('\n Aperte ENTER para começar...')
print ('\n O jogo ja vai começar!, la vem a primeira pergunta!')


