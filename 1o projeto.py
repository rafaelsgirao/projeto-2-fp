def eh_tabuleiro(arg):
    """universal -> booleano

       Esta funcao recebe um qualquer argumento e retorna True
       se e so se esse argumento for um tabuleiro valido.

       (Ou seja, um tuplo que contem tres tuplos, que por 
       sua vez conteem 3 valores, apenas podendo esses valores ser
       0, 1 ou -1).
       Caso contrario retorna False.    

       Esta funcao nao gera erros.
    """
    if not(isinstance(arg, tuple) and len(arg) == 3):
        return False
    for linha in arg:
        if not isinstance(linha, tuple):
            return False
        if not len(linha) == 3:
            return False
        for elem in linha:
            if not isinstance(elem, int):
                return False
            #Porque isinstance(True,int) retorna true
            if isinstance(elem, bool):
                return False
            if not (-1 <= elem and elem <= 1):
                return False
    return True

def eh_posicao(pos):
    """universal -> booleano

    Esta funcao recebe um qualquer argumento e retorna True
    se e so se esse argumento for uma posicao valida de um tabuleiro.
    (Ou seja, um inteiro entre 1 e 9). Caso contrario retorna False.

    Esta funcao nao gera erros.
    """
    if not isinstance(pos, int):
        return False
    elif isinstance(pos, bool):
        return False
    elif not (1 <= pos and pos <= 9):
        return False
    return True
  
def obter_oponente(jgdr):
    """tabuleiro x inteiro -> vetor

    Esta funcao  recebe um inteiro identificando um jogador e retorna o seu oponente.
   
    Ou seja, recebe -1 ou 1, e retorna o seu oponente: 1 ou -1, respetivamente.

    Como se trata de uma funcao auxiliar esta funcao nao gera erros.
    """
    if jgdr == -1:
        return(1)
    elif jgdr == 1:
        return -1
   
def obter_coluna(tab, col):
    """tabuleiro x inteiro -> vetor

    Esta funcao recebe um tabuleiro e um inteiro de 1 a 3 que representa
    o nr da coluna e devolve um vetor com os valores dessa coluna. 

    Esta funcao gera um erro caso algum dos argumentos seja invalido.
    """
    if not(eh_tabuleiro(tab) and isinstance(col, int) and \
           (1 <= col and col <= 3) \
        #Validacao necessaria orque isinstance(True, int) eh True
        and not isinstance(col, bool)):
        raise ValueError("obter_coluna: algum dos argumentos e invalido")

    #[col-1] porque dentro do tuplo as colunas sao identificadas de 0 a 2
    # e nao de 1 a 3
    return(tab[0][col-1], tab[1][col-1], tab[2][col-1])
    

def obter_linha(tab, linha):
    """tabuleiro x inteiro -> vetor

        Esta funcao recebe um tabuleiro e um inteiro de 1 a 3 que representa
        o nr da linha e devolve um vetor com os valores dessa linha. 
        
        Esta funcao gera um erro caso algum dos argumentos seja invalido.
    """
    if not(eh_tabuleiro(tab) and isinstance(linha, int) and \
           (1 <= linha and linha <= 3) \
        #Validacao necessaria porque isinstance(True, int) eh True
        and not isinstance(linha, bool)):
        raise ValueError("obter_linha: algum dos argumentos e invalido")

    #linha-1 porque as linhas sao identificadas de 0 a 2 dentro do tuplo
    return(tab[linha-1])

def obter_diagonal(tab, diag):
    """tabuleiro x inteiro -> vetor

        Esta funcao recebe um tabuleiro e um inteiro de 1 a 2 que representa
        a diagonal e devolve um vetor com os valores dessa diagonal. 

        Caso diag = 1, sera devolvido um vetor com os valores da diagonal
        composta pelas posicoes 1, 5 e 9, por esta ordem.

        Caso diag = 2, sera devolvido um vetor com os vetores da diagonal
        composta pelas posicoes 7, 5 e 3, por esta ordem.
        
        Esta funcao gera um erro caso algum dos argumentos seja invalido.
    """    
    if not(eh_tabuleiro(tab) and isinstance(diag, int) \
        #Validacao necessaria porque isinstance(True, int) eh True
        and not isinstance(diag, bool)):
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    if diag == 1:
        return(tab[0][0], tab[1][1], tab[2][2])
    elif diag == 2:
        return(tab[2][0], tab[1][1], tab[0][2])
    else:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")
    
def tabuleiro_str(tab):
    """tabuleiro -> cadeira de caracteres

        Esta funcao recebe um tabuleiro e devolve a cadeira de caracteres 
        que contem a representacao externa do tabuleiro, conforme o exemplo dado.

        Esta funcao gera um erro caso o tabuleiro nao seja valido.
    """
    if not eh_tabuleiro(tab):
        raise ValueError("tabuleiro_str: o argumento e invalido")
    # repex_tab = Cadeira de caracteres com a representacao externa do tabuleiro
    repex_tab = "" 
    for linha in tab:
        repex_linha = " " # repex_linha = Representacao externa da linha
        for elem in linha:
            #Substituicao da representacao interna pela externa equivalente
            if elem == -1:
                char = "O"
            elif elem == 1:
                char = "X"
            else:
                char = " "
            repex_linha += char + " | "
            #Remover os ultimos dois caracteres da representacao externa da linha
            #Ou seja, remover o ultimo separador de colunas por ser desnecessario
        repex_linha = repex_linha[:-2]
        repex_tab += repex_linha + "\n-----------\n"
    #Remover os ultimos 13 caracteres da representacao externa, ou seja,
    #remover o ultimo separador de linhas por ser desnecessario
    repex_tab = repex_tab[:-13]
    return(repex_tab)


def eh_posicao_livre(tab, pos):
    """tabuleiro x posicao -> booleano

    Esta funcao recebe um tabuleiro e uma posicao no mesmo, e retorna
    True se essa posicao do tabuleiro estiver livre
    ou False se jah estiver ocupada.

    Gera um erro se algum dos argumentos eh invalido.
    """
    if not(eh_tabuleiro(tab) and eh_posicao(pos)):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    
    #Verificar em que linha estah a posicao e proceder de acordo
    if (1<= pos and pos <= 3):
        valor = tab[0][pos - 1]
    elif (4 <= pos and pos <= 6):
        valor = tab[1][pos - 4]
    else:
        valor = tab[2][pos - 7]
    return(valor == 0)
    
def obter_posicoes_livres(tab):
    """tabuleiro -> vetor

       Esta funcao recebe um tabuleiro e retorna um vetor com todas as posicoes
       livres do mesmo.
       Gera um erro se o tabuleiro nao for valido.
    """
    if not(eh_tabuleiro(tab)):
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    i = 1
    rslt = ()
    for linha in tab:
        for elem in linha:
            if elem == 0:
                rslt = rslt + (i,)
            i += 1
    return rslt


    
def jogador_ganhador(tab):
    """tabuleiro -> inteiro

    Esta funcao recebe um tabuleiro e devolve um inteiro que representa
    o jogador que ganhou o jogo (-1 para "O" e 1 para "X")

    Retorna 0 em caso de empate ou se o jogo ainda estiver a decorrer.

    Esta funcao gera um erro se o tabuleiro for invalido.   
    """

    if not(eh_tabuleiro(tab)):
        raise ValueError("jogador_ganhador: o argumento e invalido")

    i = 1
    while (i <= 3):
        col = obter_coluna(tab, i)
        if col[0] == col[1] == col[2]:
            return col[0]
        i += 1
    i = 1
    while (i <= 3):
        linha = obter_linha(tab, i)
        if linha[0] == linha[1] == linha[2]:
            return linha[0]
        i += 1
    i = 1
    while (i <= 2):
        diag = obter_diagonal(tab, i)
        if diag[0] == diag[1] == diag[2]:
            return diag[0]
        i += 1        
        
    return(0) 
    
def jogo_a_decorrer(tab):
    """tabuleiro -> booleano

    Esta funcao auxiliar recebe um tabuleiro e retorna True se o jogo ainda 
    estiver a decorrer, ou False caso contrario.
    
    Esta funcao gera erro caso o tabuleiro seja invalido.
    """
    if not (eh_tabuleiro(tab)):
        raise ValueError("jogo_a_decorrer: o argumento e invalido")

    #Se nao existirem mais posicoes livres, o jogo acabou
    if obter_posicoes_livres(tab) == ():
        return False
    #Se o resultado de jogador_ganhador(tab) nao for 0, alguem ganhou o jogo
    #logo, o jogo acabou
    elif jogador_ganhador(tab) != 0:
        return False
    #Caso contrario, ainda estah a decorrer
    else:
        return True
    
#Retorna um tuplo achatado com todos os valores de 1 a 9 dentro do tabuleiro
#Permite manipulacao em marcar_posicao() sem listas e sem partir tuplos


def obter_tab_achatado(tab):
    """tabuleiro -> vetor

    Esta funcao auxiliar recebe um tabuleiro e retorna um vetor com todos
    os valores de todas as posicoes do tabuleiro num unico vetor,o que simplifica
    alguma logica nas funcoes que se seguem.

    Esta funcao gera um erro caso o tabuleiro seja invalido.
    """
    if not(eh_tabuleiro(tab)):
        raise ValueError("obter_tab_achatado: o argumento e invalido")
    rslt = ()
    for linha in tab:
        for valor in linha:
            rslt += (valor,)
    return rslt        
    
def reconverter_tab_achatado(tab):
    """vetor -> tabuleiro
    
    Esta funcao auxiliar recebe um vetor de um tabuleiro anteriormente achatado
    (respeitando a formatacao obtida atraves da funcao obter_tab_achatado() )
    e retorna o para a sua formatacao original.

    Esta funcao gera um erro caso o tabuleiro seja invalido.
    """
    if len(tab) != 9:
        raise ValueError("reconverter_tab_achatado: o argumento e invalido")
    return (tab[:3], tab[3:6], tab[6:9])
        
def marcar_posicao(tab, jgdr, pos):    
    """tabuleiro x inteiro x posicao -> tabuleiro
    
    Esta funcao recebe um tabuleiro, um inteiro representando um jogador e
    uma posicao _livre_ e devolve um novo tabuleiro modificado com a marca
    do jogador na posicao dada.
    
    Se algum dos argumentos for invalido (posicao nao livre, posicao nao existente,
    jogador nao existente), eh retornado um erro.

    """
    if not(eh_tabuleiro(tab) and isinstance(jgdr, int) and eh_posicao(pos) and \
           (jgdr == -1 or jgdr == 1) \
            and not isinstance(jgdr, bool) and eh_posicao_livre(tab, pos)):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")    

    #Achatar o tabuleiro para facilitar a sua manipulacao   
    tab_achatado = obter_tab_achatado(tab)

    #Separar o tuplo em dois tuplos distintos, um com todas as posicoes ah esquerda
    #da posicao dada e outro com todas as posicoes ah direita da posicao dada
    #No meio deles eh inserido um tuplo com a marca do jogador, efetivamente marcando a
    #posicao
    rslt = tab_achatado[:pos-1] + (jgdr,) + tab_achatado[pos:]
    
    #Reconverter e devolver o tabuleiro alterado
    return(reconverter_tab_achatado(rslt))

def escolher_posicao_manual(tab):
    """
    tabuleiro -> posicao

    Esta funcao recebe um tabuleiro e realiza a leitura de uma posicao
    manualmente inserida por um jogador, e devolve-a se esta for valida.

    (A posicao eh valida se for uma posicao do tabuleiro e esta nao
    estiver ocupada. Caso nao seja verdade, gera um erro.)

    """
    if not eh_tabuleiro(tab):
        raise ValueError("escolher_posicao_manual: o argumento e invalido")
    #Pedir ao utilizador que insira a posicao
    pos = eval(input("Turno do jogador. Escolha uma posicao livre: "))
    
    #Validar a posicao
    if not eh_posicao(pos):
        raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
    if not eh_posicao_livre(tab, pos):
        raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
    return(pos)
        
def escolher_posicao_auto(tab, jgdr, modo):
    """tabuleiro x inteiro x cadeia de caracteres

    Esta recebe um tabuleiro, um inteiro identificado um jogador
    e uma cadeia de caracteres que identifica a estrategia a usar e
    devolve a posicao escolhida automaticamente de acordo com a 
    estrategia selecionada.

    Existem 3 modos definidos:
    
    Facil: Segue as estrategias 5,7 e 8, por ordem;
    Normal: Segue as estrategias 1, 2, 5, 6, 7 e 8 por ordem;
    Perfeito: Segue todas as estrategias (1 a 8), por ordem.
    
    Esta funcao gera um erro caso algum dos argumentos seja invalido.
    """
    if not(eh_tabuleiro(tab) and isinstance(jgdr, int) \
           and (jgdr == -1 or jgdr == 1) \
        and not isinstance(jgdr, bool)):
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")  
    
    if not (modo == "basico" or modo == "normal" or modo == "perfeito"):
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")
    
    #Definir previamente variaveis para 
    #poderem ser usadas repetidamente em varios criterios

    oponente = obter_oponente(jgdr) 
    livres = obter_posicoes_livres(tab)
    colunas = (obter_coluna(tab,1),obter_coluna(tab,2),obter_coluna(tab,3))
    diags = (obter_diagonal(tab,1), obter_diagonal(tab,2))
    
    def crit_1e2(tab, jgdr, colunas, diags):
        """tabuleiro x inteiro x vetor x vetor -> posicao ou None

        Esta funcao auxiliar recebe um tabuleiro, um inteiro representando um jogador,
        e dois vetores com as 3 colunas e 2 diagonais de um tabuleiro, respetivamente.

        Devolve um inteiro que representa a posicao de acordo com o criterio 1 e 2, se
        esta posicao existir.
        Os dois criterios foram combinados numa unica funcao, pois o resultado e o metodo a usar
        tem que ser o mesmo, independentemente de se tratar do jogador ou do seu oponente.
        
        Esta funcao nao gera erros.
        """
        diag1, diag2 = diags

        #Verificar os criterios linha a linha
        i = 1
        for linha in tab:
            if linha.count(jgdr) == 2:
                for valor in linha:
                    if valor == 0:
                        return i
                    i+=1
            else:
                i+=3      
        i = 1
        #Verificar os criterios coluna a coluna
        for col in colunas:
            if col.count(jgdr) == 2:
                for valor in col:
                    if valor == 0:
                        return i
                    i+=3
            else:
                i+=1                  
        i = 1
        #Verificar os criterios na diagonal 1
        if diag1.count(jgdr) == 2:
            for valor in diag1:
                if valor == 0:
                    return i
                i+=4
        #Verificar os criterios nas diagonal 2
        elif diag2.count(jgdr) == 2:
            i = 7
            for valor in diag2:
                if valor == 0:
                    return i
                i-=2
            
    def obter_bifurcacoes(tab, livres, jgdr, colunas, diags, oponente):
        """tabuleiro x vetor x inteiro x vetor x vetor x inteiro

        Esta funcao auxiliar recebe: 
        um tabuleiro,
        um vetor com todas as posicoes livres,
        um inteiro que representa o jogador,
        um vetor com as 3 colunas,
        um vetor com as 2 diagonais,
        um inteiro que representa o oponente.

        Esta bifurcacao retorna um vetor contendo o nr de bifurcacoes encontradas
        e a posicao da primeira bifurcacao.

        Esta funcao nao gera erros.
        """
        #Criar previamente copia do tabuleiro, achatada
        #Esta poderia ser passada como argumento ah funcao, mas
        #diminuiria a legibilidade do codigo por jah ter demasiados argumentos.
        taba = obter_tab_achatado(tab)

        #Definir previamente valores necessarios
        i = 1
        nr_bifurcacoes = 0
        primeira_bifurcacao = False

        #diags = diag1, diag2
        #Ver bifurcacoes das diagonais primeiro
        #1a diagonal
        
        #Verificar todas as bifurcacoes linha-coluna existentes
        for linha in tab:
            for col in colunas:
                if jgdr in linha:
                    if oponente not in linha:
                        #Se o jogador nao estiver na coluna nao ha bifurcacao
                        if jgdr in col:
                            #Se o oponente estiver na coluna nao ha bifurcacao
                            if oponente not in col:
                                #Verificar se a posicao de intersecao esta ocupada ou nao
                                if taba[i-1] == 0:
                                    #Incrementar o nr de bifurcacoes encontradas
                                    nr_bifurcacoes += 1
                                    if primeira_bifurcacao is False:
                                        primeira_bifurcacao = i
                i += 1
                                    
        return nr_bifurcacoes, primeira_bifurcacao
    

    def crit_3(tab, livres, jgdr, colunas, diags, oponente):
        """tabuleiro x vetor x inteiro x vetor x vetor x vetor x inteiro -> posicao ou None
        Esta funcao recebe exatamente os mesmos argumentos que a funcao obter_bifurcacoes.

        Devolve uma posicao obtida de acordo com o criterio 3, se esta existir.

        Esta funcao nao gera erros.
        """
        bifurcacoes = obter_bifurcacoes(tab,livres, jgdr, colunas, diags, oponente)
        if bifurcacoes[0] is not False:
            return bifurcacoes[1]
            

  
    def crit_4(tab, livres, jgdr, colunas, diags, oponente):
        """tabuleiro x vetor x inteiro x vetor x vetor x vetor x inteiro -> posicao ou None
        Esta funcao recebe exatamente os mesmos argumentos que a funcao obter_bifurcacoes.

        Devolve uma posicao obtida de acordo com o criterio 4, se esta existir.

        Esta funcao nao gera erros.
        """
        #A funcao obter_bifurcacoes eh chamada com os argumentos oponente e jgdr trocados
        #de modo a verificar se o oponente tem bifurcacoes.
        #Se a bifurcacao encontrada for unica, entao devolver a posicao de intersecao
        #de modo a bloqueah la.
        bifurcacoes = obter_bifurcacoes(tab, livres, oponente, colunas, diags, jgdr)
        if bifurcacoes[0] is not False:
            if bifurcacoes[0] == 1:
                return bifurcacoes[1]
            elif bifurcacoes[0] > 1:
                return

        

    
    def crit_5(livres): 
        """
        vetor -> posicao ou None

        Esta funcao recebe um vetor com todas as posicoes livres
        e retorna 5 se 5 for uma posicao dentro do vetor livres.
        (Criterio 5)
        Esta funcao nao gera erros.
        """
        if 5 in livres:
            return 5
    
    def crit_6(tab, livres, oponente):

        """
        tabuleiro x vetor x inteiro -> posicao ou None

        Esta funcao recebe um tabuleiro, um vetor com todas as posicoes
        livres e um inteiro que representa o oponente
        e retorna uma posicao de acordo com o criterio 6, se esta existir.

        Esta funcao nao gera erros.
        """
        tab = obter_tab_achatado(tab)
        #Cantos 1 e 9
        if tab[0] == oponente:
            if 9 in livres: 
                return 9
        elif tab[8] == oponente:
            if 1 in livres: 
                return 1

        #Cantos 3 e 7
        elif tab[2] == oponente:
            if 7 in livres:
                return 7
        elif tab[6] == oponente:
            if 3 in livres:
                return 3

    def crit_7(livres):
        """vetor -> posicao ou None
        Esta funcao recebe um vetor com todas as posicoes livres
        e retorna uma posicao de acordo com o criterio 7.

        Esta funcao nao gera erros.
        """
        if 1 in livres: 
            return 1
        elif 3 in livres: 
            return 3
        elif 7 in livres:
            return 7
        elif 9 in livres:
            return 9
        
    def crit_8(livres):
        """vetor -> posicao ou None
        Esta funcao recebe um vetor com todas as posicoes livres
        e retorna uma posicao de acordo com o criterio 8.

        Esta funcao nao gera erros.
        """
        return livres[0]
    
    #Basico: Por ordem, os criterios  5 7 e 8    
    if modo == "basico":
        return(crit_5(livres) or
         crit_7(livres) or crit_8(livres))

    #Normal: Por ordem, os criterios 1 2 5 6 7 e 8
    elif modo == "normal":
        return(crit_1e2(tab, jgdr, colunas, diags) or \
               crit_1e2(tab, oponente, colunas, diags) or \
               crit_5(livres) or \
               crit_6(tab, livres, oponente) or \
               crit_7(livres) or \
               crit_8(livres))
    
    #Perfeito: por ordem, todos os criterios
    elif modo == "perfeito":
        return(crit_1e2(tab, jgdr, colunas, diags) or \
               crit_1e2(tab, oponente, colunas, diags) or \
               crit_3(tab, livres, jgdr, colunas, diags, oponente) or \
               crit_4(tab, livres, jgdr, colunas, diags, oponente) or
               crit_5(livres) or \
               crit_6(tab, livres, oponente) or \
               crit_7(livres) or \
               crit_8(livres))

    
def jogo_do_galo(jgdr, modo):
    """ cadeia de caracteres x cadeia de caracteres -> cadeia de caracteres 
    
    Esta funcao corresponde ah funcao principal que permite jogar um
    jogo completo de Jogo do Galo de um jogador contra o computador.

    O jogo comeca sempre com o jogador "X" a marcar uma posicao livre e termina
    quando um dos jogadores vence, ou, se nao existirem posicoes livres no tabuleiro
    (empate).

    A funcao recebe duas cadeias de caracteres e devolve o identificador do 
    jogador ganhador ("X" ou "O", ou "EMPATE" caso contrario.)

    O primeiro argumento corresponde ao caracter que o jogador humano pretende
    usar, e o segundo corresponde ah estrategia a usar pelo computador.

    Esta funcao gera um erro caso algum dos argumentos for invalido,
    ou se for indicada uma posicao invalida durante o decorrer do jogo
    pelo jogador humano.
    """
    if not (modo == "basico" or modo == "normal" or modo == "perfeito"):
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")
    
    #rep_jgdr = Representacao interna da marca do jogador (X=1, O=-1)
    #rep_pc = Mesmo que rep_jgdr mas para o computador
    #Turno = Booleano, True se for a vez do jogador a jogar, False caso contrario
    
    #Identificar os jogadores de acordo com o 1o argumento e definir 
    #de quem eh o 1o turno
    if jgdr == "X":
        rep_jgdr = 1
        turno = 1
        rep_pc = -1
    elif jgdr == "O": 
        turno = 0
        rep_jgdr = -1
        rep_pc = 1
    else:
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")
    
    #Definir o estado inicial do tabuleiro 
    tab = ((0,0,0),(0,0,0),(0,0,0))
    print("Bem-vindo ao JOGO DO GALO.")
    print("O jogador joga com '{}'.".format(jgdr))
    
    #Iniciar o loop do jogo
    while jogo_a_decorrer(tab):
        #Caso seja o turno do jogador, pedir a posicao a jogar,
        #Marcar a posicao a jogar no tabuleiro e mostrar ao
        #jogador humano o novo tabuleiro
        if turno:
            pos = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, rep_jgdr, pos)
            print(tabuleiro_str(tab))
            #Alternar o turno
            turno = False
        #Caso contrario, deixar o computador escolher a posicao a jogar,
        #marcar essa posicao e mostrar ao jogador humano o novo tabuleiro
        else:   
            print("Turno do computador ({}):".format(modo))
            pos = escolher_posicao_auto(tab, rep_jgdr, modo)
            
            tab = marcar_posicao(tab, rep_pc, pos)
            print(tabuleiro_str(tab))
            #Alternar o turno
            turno = True
    #Apos o fim do jogo, verificar se alguem ganhou ou se houve empate
    vencedor = jogador_ganhador(tab)
    if vencedor == -1:
        return('O')
    elif vencedor == 1:
        return('X')
    else:
        return('EMPATE')