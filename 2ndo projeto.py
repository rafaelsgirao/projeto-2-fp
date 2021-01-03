debug = False
def debug_vars():
    global debug
    if debug:
        global pos1, pos2, t

        pos1 = cria_posicao("b", "2")
        pos2 = cria_posicao("b", "3")
        tpl = ((0, 1, -1), (-0, 1, -1), (1, 0, -1))
        t = tuplo_para_tabuleiro(tpl)


def dbg_msgs(input):
    global debug
    if debug:
        print(input)

#ist199309 Rafael Girao - Projeto 2 de FP

def minimax(t, jgdr, profnd, seq_movs):
    if obter_ganhador(t) != cria_peca(" ") or profnd == 0:
        return(obter_ganhador(t),)
#------------------------TAD posicao (1.5 valores)------------------

#Construtores

def cria_posicao(c, l):

    cols = ("a","b","c")
    linhas = ("1","2","3")
    if not(c in cols and l in linhas):
        raise ValueError("cria_posicao: argumentos invalidos")
    
    return {"c": c, "l":l}

def cria_copia_posicao(p):
    if not eh_posicao(p):
        raise ValueError("cria_posicao: argumentos invalidos")
    return p.copy()

#Seletores
def obter_pos_c(p):
    return p["c"]

def obter_pos_l(p):
    return p["l"]

#Reconhecedores
def eh_posicao(p):
    return isinstance(p, dict) and "c" in p and "l" in p and \
        p["c"] in ("a","b","c") and \
        p["l"] in ("1","2","3") and len(p) == 2

#Teste
def posicoes_iguais(p1, p2):
    return p1 == p2


#Transformador
def posicao_para_str(p):
    return p["c"] + p["l"]

#Funcao auxiliar: Retorna todas as posicoes existentes

def obter_todas_posicoes():
    cols = ("a","b","c")
    linhas = ("1","2","3")
    return [cria_posicao(c,l) for l in linhas for c in cols]
    
#Funcao de alto nivel

#Done, i guess
def obter_posicoes_adjacentes(p):

    c, l = obter_pos_c(p), obter_pos_l(p)
    
    centro = cria_posicao("b", "2")
    posicoes = obter_todas_posicoes()

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
            dbg_msgs("c = {} and l = {}".format(c, l))
            rslt.append(centro)

        #Ordenar o resultado (rslt_ordenado = resultado ordenado)
        rslt_ordenado = ()
        for pos in posicoes:
            if pos in rslt:
                rslt_ordenado = rslt_ordenado + (pos,)

    return rslt_ordenado
   


#------------------------TAD peca (1.5 valores)------------------

#Construtores
def cria_peca(p):
    if p == "X":
        return {"p": 1}
    elif p == "O":
        return {"p": -1}
    elif p == " ":
        return {"p": 0}
    else:
        raise ValueError("cria_peca: argumento invalido")


def cria_copia_peca(p):
    return p.copy()

#Reconhecedores
def eh_peca(p):
    if not isinstance(p, dict):
        return False
    if "p" not in p:
        return False
    return isinstance(p, dict) and p["p"] in (-1, 0, 1) \
        and len(p) == 1

#Teste

def pecas_iguais(p1, p2):
    if not (eh_peca(p1) and eh_peca(p2)):
        return False
    return p1 == p2

#Transformador

def peca_para_str(p):
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
    peca = peca_para_str(p)
    if peca == "[X]":
        return 1
    elif peca == "[O]":
        return -1
    elif peca == "[ ]":
        return 0
    
#------------------------TAD tabuleiro (3 valores)------------------

#Construtores
def cria_tabuleiro():
    t = {}
    peca_vazia = cria_peca(" ")
    for pos in obter_todas_posicoes():
        t[posicao_para_str(pos)] = peca_vazia
    return t

def cria_copia_tabuleiro(t):
    if not eh_tabuleiro(t):
        raise ValueError("cria_copia_tabuleiro: argumento invalido")
    return t.copy()
    
#Seletores

def obter_peca(t, pos):
    return t[posicao_para_str(pos)]

def obter_vetor(t, vect):

    rslt = ()
    cols = ("a","b","c")
    linhas = ("1", "2", "3")
    #Caso do vetor pedido ser coluna
    if vect in cols:
        #vect_posicoes = Vetor com as posicoes do vetor pedido)
        vect_posicoes = [cria_posicao(vect, l) for l in linhas]
        #dbg_msgs("obter_vetor | vect_posicoes = {}".format(vect_posicoes))
    #Caso do vetor pedido ser linha
    else:
        vect_posicoes = [cria_posicao(c, vect) for c in cols]
       # dbg_msgs("obter_vetor | vect_posicoes = {}".format(vect_posicoes))
    
    for pos in vect_posicoes:
        rslt = rslt + (t[posicao_para_str(pos)],)
    return rslt
#Modificadores
def coloca_peca(tab, peca, pos):
    tab[posicao_para_str(pos)] = peca
    return tab

def remove_peca(tab, pos):
    tab[posicao_para_str(pos)] = cria_peca(" ")
    return tab

def move_peca(tab, pos1, pos2):
    str_pos1, str_pos2 = posicao_para_str(pos1), posicao_para_str(pos2)
    tab[str_pos2] = tab[str_pos1]
    tab[str_pos1] = cria_peca("")
    return tab

#Reconhecedores
    
def eh_tabuleiro(t):
    #Verificar se t eh dicionario de 9 elementos
    #dbg_msgs("eh_tabuleiro|t ={}".format(t))
    if not isinstance(t, dict):
        return False
    if len(t) != 9:
        return False

    count_x, count_o = 0,0

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
        if abs(count_o - count_x) >= 2 or count_o > 3 or count_x > 3:
            return False
    return len(obter_ganhadores_aux(t)) == 1


def eh_posicao_livre(t, p):
    return obter_peca(t, p) == cria_peca(" ")
#Teste

def tabuleiros_iguais(t1, t2):
    if not(eh_tabuleiro(t1) and eh_tabuleiro(t2)):
        return False
    return t1 == t2

#funcao auxiliar
def print_tabuleiro(t):
    print(tabuleiro_para_str(t))

def tabuleiro_para_str(t):
    tabstr = """   a   b   c
1 {}-{}-{}
   | \ | / |
2 {}-{}-{}
   | / | \ |
3 {}-{}-{}"""
    pecas_ordenadas = []
    for pos in obter_todas_posicoes():
        pecas_ordenadas.append(peca_para_str(obter_peca(t, pos)))
    pecas_ordenadas = tuple(pecas_ordenadas)
#    dbg_msgs("tabuleiro_para_str | pecas_ordenadas = {}".format(pecas_ordenadas))
    tabstr = tabstr.format(*pecas_ordenadas)
    return tabstr


    
def tuplo_para_tabuleiro(tpl):
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
    tpl_cols = ("a","b","c")
    tpl_linhas = ("1","2","3")
    linhas = [obter_vetor(t, l) for l in tpl_linhas]
    cols = [obter_vetor(t, c) for c in tpl_cols]
    ganhadores = []
    peca_vazia = cria_peca(" ")
    for linha in linhas:
        if linha[0] == linha[1] == linha[2] and linha[0] != peca_vazia:
            if linha[0] not in ganhadores:
                ganhadores.append(linha[0])
    for col in cols:
        if col[0] == col[1] == col[2] and linha[0] != peca_vazia:
            if col[0] not in ganhadores:
                ganhadores.append(linha[0])
    if ganhadores == []:
        return [peca_vazia]
    else:
        return ganhadores

def obter_ganhador(t):
    return obter_ganhadores_aux(t)[0]

#funcao auxiliar
def obter_posicoes_peca(t, peca):
    rslt = []
    for pos in obter_todas_posicoes():
        if obter_peca(t, pos) == peca:
            rslt.append(pos)

    return tuple(rslt)

def obter_posicoes_livres(t):
    return obter_posicoes_peca(t, cria_peca(" "))
        
def obter_posicoes_jogador(t, j):
    return obter_posicoes_peca(t, j)

#------------------------Funcoes adicionais------------------

#Funcao auxiliar
def eh_vetor(vect):
    cols = ("a","b","c")
    linhas = ("1","2","3")
    return ((vect[0] in cols or vect[0] in linhas) and \
        (vect[1] in cols or vect[1] in linhas))

def obter_movimento_manual(t, peca):
    #Verificar se todas as pecas foram colocadas
    if len(obter_posicoes_jogador(t, cria_peca("X"))) == 3 \
        and len(obter_posicoes_jogador(t, cria_peca(("O")))) == 3:
        mov = input("Turno do jogador. Escolha um movimento: ")
        pos1,pos2 = mov[:2], mov[2:]

        #Validar se podemos invocar cria_posicao com estas posicoes
        if not eh_vetor(pos1) and eh_vetor(pos2):
            raise ValueError("obter_movimento_manual: escolha invalida")
        #Se chegahmos aqui entao criar posicoes
        pos1 = cria_posicao(pos1[0], pos1[1])
        pos2 = cria_posicao(pos2[0], pos2[1])

        dbg_msgs("obter_movimento_manual | {} {}".format(pos1,pos2))

        #Validar se a escolha eh valida
        if not (pos2 in obter_posicoes_adjacentes(pos1) and \
                obter_peca(t, pos1) == peca and \
                     obter_peca(t, pos2) == cria_peca(" ")):
            raise ValueError("obter_movimento_manual: escolha invalida")

    else:
        mov = input("Turno do jogador: Escolha uma posicao: ")
        if not eh_vetor(mov):
            raise ValueError("obter_movimento_manual: escolha invalida")
def obter_movimento_auto():
    return

def moinho():
    return
