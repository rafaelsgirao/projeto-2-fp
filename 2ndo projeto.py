#ist199309 Rafael Girao - Projeto 2 de FP


#TAD posicao
# Representacao interna: dicionario de duas chaves "c" e "l", sendo os seus
#valores possiveis "a","b","c" e "1","2","3";respetivamente
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str
# obter_posicoes_adjacentes: posicao -> tuplo de posicoes


def cria_posicao(c, l): 
    """str x str -> posicao

    cria posicao(c,l) recebe duas cadeias de carateres correspondentes 
    a coluna c e a linha l de uma posicao e devolve a posicao correspondente.

    O construtor verifica a validade dos seus argumentos, gerando um ValueError
    com a mensagem "cria posicao: argumentos invalidos" caso os seus argumentos
    nao sejam validos.
"""
    cols = ("a","b","c") 
    linhas = ("1","2","3") 
    if not(c in cols and l in linhas): 
        raise ValueError("cria_posicao: argumentos invalidos") 
     
    return {"c": c, "l":l} 

def cria_copia_posicao(p):
    """posicao -> posicao

    cria copia posicao(p) recebe uma posicao e devolve 
    uma copia nova da posicao.
    O construtor verifica a validade dos seus argumentos, gerando um ValueError
    caso os seus argumentos nao sejam validos.
"""
    if not eh_posicao(p):
        raise ValueError("cria_posicao: argumentos invalidos")
    return p.copy()

#Seletores
def obter_pos_c(p):
    """posicao -> str

       obter_pos_c(p) devolve a componente coluna c da posicao p.
"""
    return p["c"]

def obter_pos_l(p):
    """posicao -> str

       obter_pos_l(p) devolve a componente linha l da posicao p.
"""
    return p["l"]

#Reconhecedores 
def eh_posicao(p): 
    """universal -> booleano

    eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao 
    e False caso contrario.
"""
    return isinstance(p, dict) and "c" in p and "l" in p and \
        p["c"] in ("a","b","c") and \
        p["l"] in ("1","2","3") and len(p) == 2

#Teste
def posicoes_iguais(p1, p2):
    """posicao x posicao -> booleano
    
    posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes e sao
iguais.
"""
    if eh_posicao(p1) and eh_posicao(p2):
        return p1 == p2
    return False

#Transformador
def posicao_para_str(p):
    """posicao_para_str: posicao -> str

    posicao_para_str(p) devolve a cadeia de caracteres "cl" que representa o seu
argumento, sendo os valores c e l as componentes coluna e linha de p.
"""
    return p["c"] + p["l"]

#Funcao auxiliar
def obter_todas_posicoes():
    """{} -> universal

    obter_todas_posicoes_ devolve a lista que contem todas os TAD posicoes
    existentes, por ordem de leitura do tabuleiro.
"""
    return [cria_posicao(c,l) for l in "123" for c in "abc"]
    
#Funcao de alto nivel
def obter_posicoes_adjacentes(p):
    """posicao -> tuplo de posicoes

    obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes
    ah posicao p de acordo com a ordem de leitura do tabuleiro.
"""
    c, l = obter_pos_c(p), obter_pos_l(p)
    
    centro, posicoes = cria_posicao("b", "2"), obter_todas_posicoes()

    #Caso de ser o centro
    if posicoes_iguais(p, centro):
        posicoes.remove(centro)
        return tuple(posicoes)
    #Todos os outros casos
    else:
        rslt = []
        if c == "a" or c == "c":    
            rslt.append(cria_posicao("b", l))
        elif c == "b":
            rslt.append(cria_posicao("a", l))    
            rslt.append(cria_posicao("c", l))    
        if l == "1" or l == "3":
            rslt.append(cria_posicao(c, "2"))
        elif l == "2":
            rslt.append(cria_posicao(c, "1"))
            rslt.append(cria_posicao(c, "3"))

        if c != "b" and l != "2":
            rslt.append(centro)

        #Ordenar o resultado (rslt_ordenado = resultado ordenado)
        rslt_ordenado = ()
        for pos in posicoes:
            if pos in rslt:
                rslt_ordenado = rslt_ordenado + (pos,)
    return rslt_ordenado
    
#TAD peca
# Representacao interna: dicionario com uma unica chave "p", sendo o seu
#valor um inteiro (1, -1 ou 0)
# cria_peca: str -> peca
# eh_peca: universal -> peca
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str
# peca_para_inteiro: peca -> Z

#Construtores
def cria_peca(p):
    """str -> peca

    cria_peca(s) recebe uma cadeia de carateres correspondente ao identificador
    de um dos dois jogadores ("X" ou "O") ou a uma peca livre (" ") e devolve a
    peca correspondente. 
    
    O construtor verifica a validade dos seus argumentos, gerando um ValueError 
    com a mensagem "cria peca: argumento invalido"
    caso o seu argumento nao seja valido.
"""
    if p == "X":
        return {"p": 1}
    elif p == "O":
        return {"p": -1}
    elif p == " ":
        return {"p": 0}
    else:
        raise ValueError("cria_peca: argumento invalido")


def cria_copia_peca(p):
    """peca -> peca

    cria_copia_peca(j) recebe uma peca e devolve uma copia nova da peca.
"""
    return p.copy()

#Reconhecedor
def eh_peca(p):
    """universal -> peca

    eh_peca(arg) devolve True caso o seu argumento seja um TAD peca e False
    caso contrario.
"""
    if not isinstance(p, dict):
        return False
    if "p" not in p:
        return False
    return isinstance(p, dict) and p["p"] in (-1, 0, 1) \
        and len(p) == 1

#Teste
def pecas_iguais(p1, p2):
    """peca x peca -> booleano

    pecas_iguais(j1, j2) devolve True apenas se p1 e p2 sao pecas e sao iguais.
"""
    if not (eh_peca(p1) and eh_peca(p2)):
        return False
    return p1 == p2

#Transformador

def peca_para_str(p):
    """peca -> str

    peca_para_str(j) devolve a cadeia de caracteres que representa o jogador
    dono da peca, isto eh, "[X]", "[O]" ou "[ ]".
"""
    p = p["p"]
    if p == -1:
        return ("[O]")
    elif p == 0:
        return ("[ ]")
    elif p == 1:
        return("[X]")
    else:
        raise ValueError("peca_para_str: argumento invalido")

#Funcao de alto nivel
def peca_para_inteiro(p):
    """peca -> Z

    peca_para_inteiro(j) devolve um inteiro valor 1, -1 ou 0, dependendo se 
    a peca eh do jogador "X", "O" ou livre, respetivamente.
"""
    peca = peca_para_str(p)
    if peca == "[X]":
        return 1
    elif peca == "[O]":
        return -1
    elif peca == "[ ]":
        return 0
    
#TAD tabuleiro
# Representacao interna: Dicionario de 9 chaves, sendo estas as representacoes
#externas de todas as posicoes possiveis. Tomam como valores o TAD peca.
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de pecas
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booleano
# eh_posicao_livre: tabuleiro x posicao -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro
# obter_ganhador: tabuleiro -> peca
# obter_posicoes_livres: tabuleiro -> tuplo de posicoes
# obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes

#Construtores
def cria_tabuleiro():
    """{} -> tabuleiro

    cria_tabuleiro() devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes
    ocupadas por pecas de jogador.
"""
    t = {}
    peca_vazia = cria_peca(" ")
    for pos in obter_todas_posicoes():
        t[posicao_para_str(pos)] = peca_vazia
    return t

def cria_copia_tabuleiro(t):
    """tabuleiro -> tabuleiro

    cria_copia_tabuleiro(t) recebe um tabuleiro e devolve uma copia nova 
    do tabuleiro.
"""
    if not eh_tabuleiro(t):
        print(t)
        #raise ValueError("cria_copia_tabuleiro: argumento invalido")
    return t.copy()
    
#Seletores

def obter_peca(t, pos):
    """tabuleiro x posicao -> peca

    obter_peca(t, p) devolve a peca na posicao p do tabuleiro. Se a posicao nao
estiver ocupada, devolve uma peca livre.
"""
    return t[posicao_para_str(pos)]

def obter_vetor(t, vect):
    """tabuleiro x str -> tuplo de pecas

    obter_vetor(t, s) devolve todas as pecas da linha ou coluna especificada
    pelo seu argumento.
"""
    cols = "abc"
    linhas = "123"
    rslt = ()
    #Caso do vetor pedido ser coluna
    if vect in cols:
        #vect_posicoes = Vetor com as posicoes do vetor pedido)
        vect_posicoes = [cria_posicao(vect, l) for l in linhas]
    #Caso do vetor pedido ser linha
    else:
        vect_posicoes = [cria_posicao(c, vect) for c in cols]
    
    for pos in vect_posicoes:
        rslt = rslt + (t[posicao_para_str(pos)],)
    return rslt
#Modificadores
def coloca_peca(tab, peca, pos):
    """tabuleiro x peca x posicao -> tabuleiro

    coloca_peca(t, j, p) modifica destrutivamente o tabuleiro t colocando
     a peca j na posicao p, e devolve o proprio tabuleiro.
"""
    tab[posicao_para_str(pos)] = peca
    return tab

def remove_peca(tab, pos):
    """tabuleiro x posicao -> tabuleiro

    remove_peca(t, p) modifica destrutivamente o tabuleiro t removendo a peca
    da posicao p, e devolve o proprio tabuleiro.
"""
    tab[posicao_para_str(pos)] = cria_peca(" ")
    return tab

def move_peca(t, pos1, pos2):
    """tabuleiro x posicao x posicao -> tabuleiro

    move_peca(t, p1, p2) modifica destrutivamente o tabuleiro t movendo a peca
    que se encontra na posicao p1 para a posicao p2, e devolve o 
    proprio tabuleiro.
"""
    str_pos1, str_pos2 = posicao_para_str(pos1), posicao_para_str(pos2)
    peca = t[str_pos1]
    t[str_pos1] = cria_peca(" ")
    t[str_pos2] = peca

    return t

#Reconhecedores
    
def eh_tabuleiro(t):
    """universal -> booleano

    eh_tabuleiro(arg) devolve True caso o seu argumento seja um TAD tabuleiro
    e False caso contrario. 
    
    Um tabuleiro valido pode ter um maximo de 3 pecas
    de cada jogador, nao pode conter mais de 1 peca mais de um jogador que do
    contrario, e apenas pode haver um ganhador em simultaneo.
"""
    #Verificar se t eh dicionario de 9 elementos
    if not isinstance(t, dict):
        return False
    if len(t) != 9:
        return False

    count_x, count_o = 0,0

    #Contar pecas de cada jogador
    for pos in obter_todas_posicoes():
        str_pos = posicao_para_str(pos)
        peca = t[str_pos]
        if not(str_pos in t and eh_peca(peca)):
            return False
        else:
            str_peca = peca_para_str(peca)
            if str_peca == "[X]":
                count_x += 1
            elif str_peca == "[O]":
                count_o += 1
    #Verificar que cada jogador apenas tem 3 pecas e nao tem 2 ou mais colocadas
    #que o adversario
    if abs(count_o - count_x) >= 2 or count_o > 3 or count_x > 3:
        return False
    return len(obter_ganhadores_aux(t)) == 1


def eh_posicao_livre(t, p):
    """tabuleiro x posicao -> booleano

    eh_posicao_livre(t, p) devolve True apenas no caso da posicao p do tabuleiro
    corresponder a uma posicao livre.
"""
    return obter_peca(t, p) == cria_peca(" ")

#Teste
def tabuleiros_iguais(t1, t2):
    """tabuleiro x tabuleiro -> booleano

    tabuleiros_iguais(t1, t2) devolve True apenas se t1 e t2 sao tabuleiros 
    e sao iguais.
"""
    if not(eh_tabuleiro(t1) and eh_tabuleiro(t2)):
        return False
    return t1 == t2


def tabuleiro_para_str(t):
    """tabuleiro -> str

    tabuleiro_para_str(t) devolve a cadeia de caracteres que representa o TAD
    tabuleiro.
"""
    tabstr = """   a   b   c
1 {}-{}-{}
   | \ | / |
2 {}-{}-{}
   | / | \ |
3 {}-{}-{}"""
    pecas_ordenadas = []
    for pos in obter_todas_posicoes():
        pecas_ordenadas.append(peca_para_str(obter_peca(t, pos)))
    return tabstr.format(*tuple(pecas_ordenadas))


    
def tuplo_para_tabuleiro(tpl):
    """tuplo -> tabuleiro

    tuplo_para_tabuleiro(t) devolve o tabuleiro que eh representado pelo tuplo t
    com 3 tuplos, cada um deles contendo 3 valores inteiros iguais a 1, -1 ou 0,
    tal como no primeiro projeto.
"""
    t = cria_tabuleiro()
    #Achatar o tuplo recebido
    tpl = [valor for linha in tpl for valor in linha]
    i = 0
    posicoes = obter_todas_posicoes()
    for valor in tpl:
        if valor == -1:
            peca = cria_peca("O")
        elif valor == 1:
            peca = cria_peca("X")
        else:
            peca = cria_peca(" ")
        coloca_peca(t, peca, posicoes[i])
        i+=1
    return t
    
#funcao auxiliar
def obter_ganhadores_aux(t):
    """tabuleiro -> lista de pecas

    obter_ganhadores_aux(t) devolve uma lista com todos os ganhadores(conforme
    criterios descritos na obter_ganhador(t)).
    
    Obviamente que se esta funcao devolver mais que uma peca na lista o
    tabuleiro fornecido eh invalido.
"""
    linhas = [obter_vetor(t, l) for l in "123"]
    cols = [obter_vetor(t, c) for c in "abc"]
    ganhadores = []
    peca_vazia = cria_peca(" ")
    #Verificar ganhadores nas linhas
    for linha in linhas:
        if linha[0] == linha[1] == linha[2] and linha[0] != peca_vazia:
            if linha[0] not in ganhadores:
                ganhadores.append(linha[0])
    #Verificar em colunas
    for col in cols:
        if col[0] == col[1] == col[2] and linha[0] != peca_vazia:
            if col[0] not in ganhadores:
                ganhadores.append(col[0])
    #Se nao houve ganhadores, devolver peca vazia
    if ganhadores == []:
        return [peca_vazia]
    else:
        return ganhadores

def obter_ganhador(t):
    """tabuleiro -> peca

    obter_ganhador(t) devolve uma peca do jogador que tenha as suas 3 pecas em
    linha na vertical ou na horizontal no tabuleiro. Se nao existir nenhum
    ganhador, devolve uma peca livre.
"""
    return obter_ganhadores_aux(t)[0]

#funcao auxiliar
def obter_posicoes_peca(t, peca):
    """tabuleiro x peca -> tuplo de posicoes

    obter_posicoes_peca(t) devolve um tuplo com as posicoes ocupadas pelas pecas
    "peca" na ordem de leitura do tabuleiro.
"""
    rslt = []
    for pos in obter_todas_posicoes():
        if obter_peca(t, pos) == peca:
            rslt.append(pos)
    return tuple(rslt)

def obter_posicoes_livres(t):
    """tabuleiro -> tuplo de posicoes

    obter_posicoes_livres(t) devolve um tuplo com as posicoes nao ocupadas pelas
    pecas de qualquer um dos dois jogadores na ordem de leitura do tabuleiro.
"""
    return obter_posicoes_peca(t, cria_peca(" "))
        
def obter_posicoes_jogador(t, j):
    """tabuleiro x peca -> tuplo de posicoes

    obter_posicoes_jogador(t, j) devolve um tuplo com as posicoes ocupadas pelas
    pecas j de um dos dois jogadores na ordem de leitura do tabuleiro.
"""
    return obter_posicoes_peca(t, j)

#------------------------Funcoes adicionais------------------

#Funcao auxiliar
def eh_vetor(vect):
    """str -> booleano

    eh_vetor(vect) devolve True se vect for um argumento valido de
    obter_vetor(t, vect), False caso contrario.

    Por outras palavras, devolve True se vect representar uma linha ou coluna
    de um tabuleiro.
"""

    return (len(vect) == 2 and vect[0] in "abc" and vect[1] in "123")

#Funcao auxiliar
def obter_peca_oponente(peca):
    """peca -> peca

    obter_peca_oponente(peca) devolve a peca do oponente do jogador.
"""
    repr = peca_para_str(peca)
    if repr == "[X]":
        return cria_peca("O")
    elif repr == "[O]":
        return cria_peca("X")
    return cria_peca(" ")

#Funcao auxiliar
def obter_livres_adjacentes(t, pos):
    """tabuleiro x posicao -> lista de posicoes

    obter_livres_adjacentes devolve as posicoes que sao adjacentes ah posicao
    pos e ao mesmo tempo nao estao ocupadas por nenhum dos dois jogadores.
"""
    livres = obter_posicoes_livres(t)
    adjacentes = obter_posicoes_adjacentes(pos)
    rslt = []
    for pos in adjacentes:
        if pos in livres:
            rslt.append(pos)
    return rslt

def obter_movimento_manual(t, peca):
    """tabuleiro x peca -> tuplo de posicoes

    Funcao auxiliar que recebe um tabuleiro e uma peca de um jogador, e devolve
    um tuplo com uma ou duas posicoes que representam uma posicao ou um
    movimento introduzido manualmente pelo jogador.

    Se o valor introduzido pelo jogador nao corresponder a posicao ou movimento
    validos, a funcao gera um erro com a mensagem "obter_movimento_manual:
    escolha invalida".
"""
    erro, peca_vazia="obter_movimento_manual: escolha invalida", cria_peca(" ")
    #Verificar se eh fase de movimento ou posicao
    if len(obter_posicoes_jogador(t, peca)) == 3:
        mov = input("Turno do jogador. Escolha um movimento: ")
        pos1,pos2 = mov[:2], mov[2:]
        #Validar se podemos invocar cria_posicao com estas posicoes
        if not(eh_vetor(pos2) and eh_vetor(pos1)): raise ValueError(erro)
        #Se chegahmos aqui entao criar posicoes
        pos1, pos2 = cria_posicao(*pos1), cria_posicao(*pos2)
        #Validar se a escolha eh valida
        adjacentes = obter_posicoes_adjacentes(pos1)
        if not ((pos2 in adjacentes or (pos1 == pos2 and \
    obter_livres_adjacentes(t,pos1) == [])) and obter_peca(t, pos1) == peca \
        and obter_peca(t, pos2) != obter_peca_oponente(peca)):
            raise ValueError(erro)
        return (pos1, pos2)
    else:
        pos = input("Turno do jogador. Escolha uma posicao: ")
        #Validar se podemos usar cria_posicao com esta posicao
        if not eh_vetor(pos): raise ValueError(erro)
        pos = cria_posicao(pos[0], pos[1])
        if not (obter_peca(t, pos) == peca_vazia): raise ValueError(erro)
        return (pos,)

def minimax(t, jgdr, profundidade, seq_movimentos):
    """tabuleiro x jogador x inteiro x lista -> tuplo

    Esta funcao implementa o algoritmo "minimax" descrito em Algoritmo 1.
    
    Esta funcao nao gera erros.
"""
    ganhador = obter_ganhador(t)
    oponente = obter_peca_oponente(jgdr)
    melhor_seq_movimentos = None
    #Reprint_jgdr = representacao inteira do jogador
    reprint_jgdr = peca_para_inteiro(jgdr)
    if ganhador != cria_peca(" ") or profundidade == 0:
        #valor_tabuleiro eh pegar no obter_ganhador e converter p/ int
        return (peca_para_inteiro(ganhador), seq_movimentos)
    else:
        melhor_resultado = peca_para_inteiro(oponente)
        livres = obter_posicoes_livres(t)
        for pos_jgdr in obter_posicoes_jogador(t, jgdr):
            for pos_adj in obter_posicoes_adjacentes(pos_jgdr):
                if pos_adj in livres:
                    copia_tab = cria_copia_tabuleiro(t)
                    novo_movimento = [pos_jgdr, pos_adj]
                    move_peca(copia_tab, *novo_movimento)
                    novo_resultado, nova_seq_movimentos= \
                        minimax(copia_tab, oponente, profundidade-1, \
                            seq_movimentos + novo_movimento)
                    if not(melhor_seq_movimentos) or \
    (reprint_jgdr == cria_peca("X") and novo_resultado > melhor_resultado) or \
    (reprint_jgdr == cria_peca("O") and novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos

#Funcao auxiliar
def indice_para_pos(ind):
    """inteiro -> posicao

    indice_para_pos(ind) devolve a posicao correspondente ao indice fornecido,
    seguindo a ordem de leitura do tabuleiro e tendo em conta que "a1" = 0
    e "c3" = 8.
"""
    i = 0 
    for pos in obter_todas_posicoes(): 
        if i == ind: 
            return pos 
        i+=1 
 
#Criterios de colocacao do obter_movimento_auto
#Criterio 1e2: Vitoria ou bloqueio de vitoria 
def crit_1e2(jgdr, linhas, cols):
    """tabuleiro x peca x lista de linhas x lista de colunas -> posicao

    Esta funcao implementa o criterio 1 e 2 (Vitoria e Bloqueio),
    descritos para a fase de colocacao.
"""

    i = 0 
    peca_vazia = cria_peca(" ")
    for linha in linhas: 
        if linha.count(jgdr) == 2: 
            for p in linha: 
                if pecas_iguais(p, peca_vazia): 
                    return indice_para_pos(i) 
                i+=1 
        else: 
            i+=3 
    for col in cols: 
        if col.count(jgdr) == 2:
            for p in col: 
                if pecas_iguais(p, peca_vazia): 
                    return indice_para_pos(i) 
                i+=1 
        else: 
            i+=3
     
def crit_3(t):
    """tabuleiro -> posicao

    Esta funcao implementa o criterio 3(Centro), descrito para a fase de
    colocacao.
"""
    centro = cria_posicao("b", "2") 
    if obter_peca(t, centro) == cria_peca(" "): 
        return centro 
def crit_4(t):
    """tabuleiro -> posicao

    Esta funcao implementa o criterio 4(Canto Vazio), descrito para a fase de
    colocacao.
"""
    cantos = [cria_posicao(c, l) for l in "13" for c in "ac"] 
    for c in cantos: 
        if obter_peca(t, c) == cria_peca(" "): 
            return c  
def crit_5(t): 
    """tabuleiro -> posicao

    Esta funcao implementa o criterio 5(Lateral Vazio), descrito para a fase de
    colocacao.
"""
    #Escolheu-se nao obter as laterais programaticamente porque 
    #diminui bastante a complexidade deste criterio 
    posicoes = ["b1", "a2", "c2", "b3"] 
    posicoes = [cria_posicao(*pos) for pos in posicoes] 
    for pos in posicoes: 
        if pecas_iguais(obter_peca(pos), cria_peca()): 
            return pos 

 
def obter_movimento_auto(t, jgdr, modo):
    """tabuleiro x peca x str -> tuplo de posicoes

    Funcao auxiliar que recebe um tabuleiro, uma peca de um jogador e uma
    cadeia de caracteres e devolve um tuplo com uma ou duas posicoes que 
    representam uma posicao ou um movimento escolhido automaticamente.

    
"""
    linhas = [obter_vetor(t, l) for l in "123"]
    cols = [obter_vetor(t, c) for c in "abc"]
    peca_vazia = cria_peca(" ")
    if len(obter_posicoes_jogador(t, jgdr)) == 3:
        #Fase de movimento
        if modo == "facil":
            for pos in obter_posicoes_jogador(t, jgdr):
                for livre_adj in obter_livres_adjacentes(t, pos):
                    return(pos, livre_adj)
        elif modo == "normal":
            return tuple(minimax(t, jgdr, 1, [])[1])
        elif modo == "dificil":
            return tuple(minimax(t, jgdr, 5, [])[1])
    else:
        #Fase de posicionamento
        return((crit_1e2(jgdr, linhas, cols) or \
            crit_1e2(obter_peca_oponente(jgdr), linhas, cols) or \
                crit_3(t) or crit_4(t) or crit_5(t)), )


def moinho(jgdr, modo):
    """str x str -> str

    Funcao principal que permite jogar um jogo completo do jogo do moinho de
    um jogador contra o computador. A funcao recebe duas cadeias de caracteres
    e devolve a representacao externa da peca ganhadora("[X]" ou "[O]").

    O 1o argumento corresponde a representacao externa da peca com que deseja
    jogar o jogador humano, e o segundo seleciona o nivel de dificuldade
    do jogo.

    Se algum dos argumentos dados forem invalidos, a funcao gera um erro.
"""
    if not (len(jgdr) == 3 and jgdr[1] in "XO" and \
        modo in ("facil", "normal", "dificil")):
        raise ValueError("moinho: agumentos invalidos")
    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.".format(modo))
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    turno_jgdr = False
    if jgdr[1] == "X": turno_jgdr = True
    jgdr, ganhador = cria_peca(jgdr[1]), cria_peca(" ")
    #Loop enquanto nenhum dos jogadores ganhar
    while obter_ganhador(t) == cria_peca(" "):
        if turno_jgdr:
            mov = obter_movimento_manual(t, jgdr)
            if len(mov) == 1: coloca_peca(t, jgdr, mov[0])
            else: move_peca(t, mov[0], mov[1])
            print(tabuleiro_para_str(t))
            turno_jgdr = False
        else:
            print("Turno do computador ({}):".format(modo))
            print(tabuleiro_para_str(t))
            turno_jgdr=True
    return peca_para_str(obter_ganhador(t))