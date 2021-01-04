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
    return isinstance(p, dict) and "c" in p and "l" in p and \
        p["c"] in ("a","b","c") and \
        p["l"] in ("1","2","3") and len(p) == 2

#Teste
def posicoes_iguais(p1, p2):
    if eh_posicao(p1) and eh_posicao(p2):
        return p1 == p2
    return False

#Transformador
def posicao_para_str(p):
    return p["c"] + p["l"]

#Funcao auxiliar: Retorna todas as posicoes existentes

def obter_todas_posicoes():
    return [cria_posicao(c,l) for l in "123" for c in "abc"]
    
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
    tab[posicao_para_str(pos)] = peca
    return tab

def remove_peca(tab, pos):
    tab[posicao_para_str(pos)] = cria_peca(" ")
    return tab

def move_peca(t, pos1, pos2):

    str_pos1, str_pos2 = posicao_para_str(pos1), posicao_para_str(pos2)
    peca = t[str_pos1]
    t[str_pos1] = cria_peca(" ")
    t[str_pos2] = peca

    return t

#Reconhecedores
    
def eh_tabuleiro(t):
    #Verificar se t eh dicionario de 9 elementos
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
def print_tab(t):
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
    return tabstr.format(*tuple(pecas_ordenadas))


    
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
    linhas = [obter_vetor(t, l) for l in "123"]
    cols = [obter_vetor(t, c) for c in "abc"]
    ganhadores = []
    peca_vazia = cria_peca(" ")
    for linha in linhas:
        if linha[0] == linha[1] == linha[2] and linha[0] != peca_vazia:
            if linha[0] not in ganhadores:
                ganhadores.append(linha[0])
    for col in cols:
        if col[0] == col[1] == col[2] and linha[0] != peca_vazia:
            if col[0] not in ganhadores:
                ganhadores.append(col[0])
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
    return (len(vect) == 2 and vect[0] in "abc" and vect[1] in "123")

#funcao auxiliar
def obter_peca_oponente(peca):
    repr = peca_para_str(peca)
    if repr == "[X]":
        return cria_peca("O")
    elif repr == "[O]":
        return cria_peca("X")
    return cria_peca(" ")

def obter_livres_adjacentes(t, pos):
    livres = obter_posicoes_livres(t)
    adjacentes = obter_posicoes_adjacentes(pos)
    rslt = []
    for pos in adjacentes:
        if pos in livres:
            rslt.append(pos)
    return rslt

def obter_movimento_manual(t, peca):
    erro = "obter_movimento_manual: escolha invalida"
    #Verificar se eh fase de movimento ou posicao
    peca_vazia = cria_peca(" ")
    if len(obter_posicoes_jogador(t, peca)) == 3:
        mov = input("Turno do jogador. Escolha um movimento: ")
        pos1,pos2 = mov[:2], mov[2:]
        #Validar se podemos invocar cria_posicao com estas posicoes
        if not(eh_vetor(pos2) and eh_vetor(pos1)): raise ValueError(erro)
        #Se chegahmos aqui entao criar posicoes
        pos1 = cria_posicao(pos1[0], pos1[1])
        pos2 = cria_posicao(pos2[0], pos2[1])

        livres = obter_livres_adjacentes(t,pos1)
        #Validar se a escolha eh valida
        adjacentes = obter_posicoes_adjacentes(pos1)
        if not ((pos2 in adjacentes or (pos1 == pos2 and livres == [])) and \
              obter_peca(t, pos1) == peca and \
                    obter_peca(t, pos2) != obter_peca_oponente(peca)):
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
    ganhador = obter_ganhador(t)
    oponente = obter_peca_oponente(jgdr)
    #Reprint_jgdr = representacao inteira do jogador
    reprint_jgdr = peca_para_inteiro(jgdr)
    if ganhador != obter_peca(" ") or profundidade == 0:
        #valor_tabuleiro eh pegar no obter_ganhador e converter p/ int
        return (peca_para_inteiro(ganhador), seq_movimentos)
    #end
    else:
        #A assumir que melhor_resultado = repr inteira do adversario?
        melhor_resultado = peca_para_inteiro(oponente)
        livres = obter_posicoes_livres(t)
        for pos_jgdr in obter_posicoes_jogador(t, jgdr):
            for pos_adj in obter_posicoes_adjacentes(pos_jgdr):
                if pos_adj in livres:
                    copia_tab = cria_copia_tabuleiro(t) #ver se eh shallow copy ou nao
                    novo_movimento = [pos_jgdr, pos_adj] #ver se tenho q criar copia
                    move_peca(copia_tab, *novo_movimento)
                    novo_resultado, nova_seq_movimentos= \
                        minimax(copia_tab, oponente, profundidade-1, seq_movimentos)
                    if (not melhor_seq_movimentos) or \
    (reprint_jgdr == cria_peca("X") and novo_resultado > melhor_resultado) or \
    (reprint_jgdr == cria_peca("O") and novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = novo_resultado, nova_seq_movimentos

        return melhor_resultado, melhor_seq_movimentos

def indice_para_pos(ind): 
    i = 0 
    for pos in obter_todas_posicoes(): 
        if i == ind: 
            return pos 
        i+=1 
 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$CRITERIOS DO OBTER_POSICAO_AUTO$$$$$$$$$$$$$$$$$$$ 
    #Criterio 1e2: Vitoria ou bloqueio de vitoria 
def crit_1e2(t, jgdr, linhas, cols): 
    i = 0 
    for linha in linhas: 
        if linha.count(jgdr) == 2: 
            for p in linha: 
                if pecas_iguais(p, jgdr): 
                    return indice_para_pos(i) 
                i+=1 
        else: 
            i+=3 
    for col in cols: 
        if col.count(jgdr) == 2:             
            for p in col: 
                if pecas_iguais(p, jgdr): 
                    return indice_para_pos(i) 
                i+=1 
        else: 
            i+=3    
     
def crit_3(t): 
    centro = cria_posicao("b", "2") 
    if obter_peca(t, centro) == cria_peca(" "): 
        return centro 
def crit_4(t):     
    cantos = [cria_posicao(c, l) for l in "13" for c in "ac"] 
    for c in cantos: 
        if obter_peca(t, c) == cria_peca(" "): 
            return c  
def crit_5(t): 
    #Escolheu-se nao obter as laterais programaticamente porque 
    #diminui bastante a complexidade deste criterio 
    posicoes = ["b1", "a2", "c2", "b3"] 
    posicoes = [cria_posicao(*pos) for pos in posicoes] 
    for pos in posicoes: 
        if pecas_iguais(obter_peca(pos), cria_peca()): 
            return pos 
def crit_6(t): 
    return 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$ EOF CRITERIOS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 

 
def obter_movimento_auto(t, jgdr, modo):
    peca_vazia = cria_peca(" ")
    if len(obter_posicoes_jogador(t, jgdr)) == 3:
        #Fase de movimento
        if modo == "facil":
            for pos in obter_posicoes_jogador(t, jgdr):
                for livre_adj in obter_livres_adjacentes(t, pos):
                    return livre_adj


def teste():
    a = [[],["banana"]]
    for i in a:
        print(i)

def moinho(jgdr, modo):
    if not (len(jgdr) == 3 and jgdr[1] in "XO" and \
        modo in ("facil", "normal", "dificil")):
        raise ValueError("moinho: agumentos invalidos")
    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.".format(modo))
    t = cria_tabuleiro()
    print_tab(t)
    print()

    turno_jgdr = False
    if jgdr[1] == "X":
        turno_jgdr = True
    jgdr = cria_peca(jgdr[1])
    ganhador = cria_peca(" ")
    while ganhador == cria_peca(" "):
        if turno_jgdr:
            mov = obter_movimento_manual(t, jgdr)
            if len(mov) == 1:
                coloca_peca(t, jgdr, mov[0])
            else:
                move_peca(t, mov[0], mov[1])
            print_tab(t)
            turno_jgdr = False
        else:
            print("Turno do computador ({}):".format(modo))
            print_tab(t)
            turno_jgdr=True
        
        ganhador = obter_ganhador(t)
        if obter_ganhador(t) != cria_peca(" "):
            return ganhador