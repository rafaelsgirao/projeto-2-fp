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
    centro = "b", "2"
    if (c, l) == centro:
        rslt = [(a, b) for a in cols for b in linhas]
        rslt = rslt.remove(centro)
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
    return [0,0,0,0,0,0,0,0,0]

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



#delete later
p1 = cria_posicao("a", "1")

