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


#delete later
p1 = cria_posicao("a", "1")

