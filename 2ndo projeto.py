
debug = True

def debug_msgs(input):
    global debug
    if debug:
        print(input)
#ist199309 Rafael Girao - Projeto 2 de FP

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
    return isinstance(p, dict) and p["c"] in ("a","b","c") and \
        p["l"] in ("1","2","3") and len(p1) == 2

#Teste
def posicoes_iguais(p1, p2):
    return p1 == p2


#Transformador
def posicao_para_str(p):
    return p["c"] + p["l"]

#Funcao de alto nivel

#ACABAR ESTA FUNCAO
def obter_posicoes_adjacentes(p):

    c, l = obter_pos_c(p), obter_pos_l(p)

    cols = ("a", "b", "c")
    linhas = ("1","2","3")
    

    centro = cria_posicao("b", "2")

    #Caso de ser o centro
    if posicoes_iguais(p, centro):
        rslt = [cria_posicao(c,l) for c in cols for l in linhas]
        rslt.remove(centro)
        return rslt
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
            debug_msgs("c = {} and l = {}".format(c, l))
            rslt.append(centro)
    return rslt
   


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
    return isinstance(p, dict) and p["p"] in (-1, 0, 1) and \
        len(p1) == 1

#Teste

def pecas_iguais(p1, p2):
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
    cols, linhas = ("a","b","c"), ("1","2","3")
    posicoes = [cria_posicao(c,l) for c in cols for l in linhas]
    peca_vazia = cria_peca(" ")
    for pos in posicoes:
        t[pos] = peca_vazia
    return t

def cria_copia_tabuleiro(t):
    return t.copy()
    
#Seletores

def obter_peca(t, pos):
    return t[pos-1]

def obter_vetor(t, vect):
    #Caso do vetor pedido ser de uma linha
    i = False
    if vect == "a":
        i = 0
    if vect == "b":
        i = 1
    if vect == "c":
        i = 2
    if i is not False:
        return [t[i], t[i+3], t[i+6]]
    if vect == "1":
        i = 0
    elif vect == "2":
        i = 3
    elif vect == "3":
        i = 6
    return [t[i], t[i+1], t[i+2]]

#Modificadores
def coloca_peca(tab, peca, pos):
    tab[pos-1] = peca
    return tab

def remove_peca(tab, pos):
    tab[pos-1] = cria_peca(" ")
    return tab

def move_peca(tab, pos1, pos2):
    tab[pos2-1] = tab[pos1-1]
    tab[pos1-1] = cria_peca("")
    return tab

#Reconhecedores

def eh_tabuleiro(t):
    #Verificar se t eh lista de 9 elementos
    if not isinstance(t, list) and len(t) == 9: return False

    count_x, count_o = 0,0
    for peca in t:
        #repr_peca = Representacao externa da peca
        repr_peca = peca_para_str(peca)

        if not eh_peca(peca): 
            return False
        elif repr_peca == "[X]":
            count_x += 1
        elif repr_peca == "[O]":
            count_o += 1
        #Testar se o tab tem 2 ou mais pecas que o adversario
        if abs(count_x - count_o) >= 2:
            return False

    return True

#Teste

def tabuleiros_iguais(t1, t2):
    return t1 == t2

def tabuleiro_para_str(t):
    tabstr = """   a b c
    1 {}-{}-{}
    | \ | / |
    2 {}-{}-{}
    | / | \ |
    3 {}-{}-{}
    """

    pecas = []
    for i in range(1,10):
        pecas.append(peca_para_str(obter_peca(t , i)))
    tabstr = tabstr.format(pecas)
    return tabstr

def tuplo_para_tabuleiro(tpl):
    t = cria_tabuleiro()
    
    i = 1
    for linha in tpl:
        for p in linha:
            if p == -1:
                nova_p = cria_peca("O")
                
            elif p == 0:
                nova_p = cria_peca(" ")
            elif p == 1:
                nova_p = cria_peca("X")
            coloca_peca(t, nova_p, i)


#delete later
p1 = cria_posicao("b", "2")

p2 = cria_posicao("b", "3")