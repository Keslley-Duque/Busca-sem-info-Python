class No(object):
    def __init__(self, pai=None, estado = None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1
        self.valor2    = valor2
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, v1, v2, p):
        novo_no = No(p, st, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, v1, v2, p):

        novo_no = No(p, st, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head
    
    # RETORNA O ULTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE A LISTA ESTA VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    # EXIBE O CONTEUDO DA LISTA    
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho
    
    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.estado != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

class busca(object):

    # BUSCA EM AMPLITUDE
    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor1+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor1+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                    l2.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho
                    
        return "Caminho não encontrado!"        
    
    # BUSCA EM PROFUNDIDADE                
    def profundidade(self, inicio, fim):
    
        # manipular a FILA para a busca
        l1 = lista()
    
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
    
        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
    
        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
    
            ind = nos.index(atual.estado)
    
            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):
    
                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True
    
                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor1+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor1+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor1 + 1, 0 , atual)
                    l2.insereUltimo(novo, atual.valor1 + 1, 0 , atual)
    
                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor1+1)
                    visitado.append(linha)
    
                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"
    
    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self, inicio, fim, limite):
    
        # manipular a FILA para a busca
        l1 = lista()
    
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
    
        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
    
        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            
            if atual.valor1!=limite:
    
                ind = nos.index(atual.estado)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])):
        
                    novo = grafo[ind][i]
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor1+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor1+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                        l2.insereUltimo(novo, atual.valor1 + 1, 0, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor1+1)
                        visitado.append(linha)
        
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho

        return "caminho não encontrado"

    # BUSCA EM APROFUNDAMENTO ITERATIVO
    def aprof_iterativo(self, inicio, fim, max_lim):

        for limite in range(max_lim):
            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while l1.vazio() == False:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                
                if atual.valor1 != limite:
    
                    ind = nos.index(atual.estado)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])):
        
                        novo = grafo[ind][i]
                        # pressuponho que não foi visitado
                        flag = True
        
                        # controle de nós repetidos
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor1+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor1+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.valor1 + 1, 0,atual)
                            l2.insereUltimo(novo, atual.valor1 + 1, 0,atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor1+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("Fila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho
                            
        return "caminho não encontrado"
    
    # BUSCA EM AMPLITUDE
    def bidirecional(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()
        l3 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        l4 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        l3.insereUltimo(fim,0,0,None)
        l4.insereUltimo(fim,0,0,None)


        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        primeiro=True

        while l1.vazio() == False and primeiro==True:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado1)):
                    if visitado1[j][0]==novo:
                        if visitado1[j][1]<=(atual.valor1+1):
                            flag = False
                        else:
                            visitado1[j][1]=atual.valor1+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                    l2.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor1+1)
                    visitado1.append(linha)

                    # verifica se é o objetivo
                    flag = False
                    for j in range(len(visitado2)):
                        if visitado2[j][0]==novo:
                            flag = True
                            break
                    
                    if flag:
                        caminho = []
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        #print("\nÁrvore de busca:\n",l4.exibeLista())
                        caminho += l2.exibeCaminho()
                        caminho += l4.exibeCaminho1(novo)
                        return caminho
                    
            primeiro=False
            
        while l3.vazio() == False and primeiro==False:
            # remove o primeiro da fila
            atual = l3.deletaPrimeiro()

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado2)):
                    if visitado2[j][0]==novo:
                        if visitado2[j][1]<=(atual.valor1+1):
                            flag = False
                        else:
                            visitado2[j][1]=atual.valor1+1
                        break
                    
                # se não foi visitado inclui na fila
                if flag:
                    l3.insereUltimo(novo, atual.valor1 + 1, 0, atual)
                    l4.insereUltimo(novo, atual.valor1 + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado2.append(linha)

                    # verifica se é o objetivo
                    flag = False
                    for j in range(len(visitado1)):
                        if visitado1[j][0]==novo:
                            flag = True
                            break
                        
                    if flag:
                        caminho = []
                        #print("Fila:\n",l3.exibeLista())
                        #print("\nÁrvore de busca:\n",l4.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        caminho += l4.exibeCaminho()
                        caminho += l2.exibeCaminho1(novo)
                        return caminho[::-1]
                        
                primeiro=True

        return "caminho não encontrado"

nos = ["Altair", "Berlin", "Caçapava", "Detroit", "Eldorado", "Franca", 
       "Goiânia", "Herval", "Ilhéus", "Jacareí", "Kiev", "Lisboa", "Los Angeles", "Manaus",
       "Namur", "Nova York", "Oiapoque", "Paris", "Quadra", "Roseira","Seul", "São Paulo", "Tijuana",
       "Tokyo", "Uberlandia", "Viena", "Washington", "Xangai", "Yakutsk", "Zurich"]

# ORDEM DECRESCENTE

grafo = [
            ["Berlin", "Herval", "São Paulo"],#Altair
            ["Altair", "Caçapava", "Ilhéus"],#Berlin
            ["Berlin", "Detroit"],#Caçapava
            ["Caçapava", "Ilhéus", "Jacareí", "Eldorado"],#Detroit
            ["Detroit", "Jacareí", "Franca"],#Eldorado
            ["Eldorado", "Kiev", "Goiânia"],#Franca 
            ["Franca", "Oiapoque", "Tokyo"],#Goiânia
            ["Altair", "Washington", "Paris"],#Herval
            ["Berlin", "Detroit", "Lisboa"],#Ilhéus
            ["Detroit", "Eldorado", "Kiev", "Manaus"],#Jacarei
            ["Franca", "Jacareí", "Roseira", "Namur"],#Kiev
            ["Ilhéus", "Paris", "Quadra"],#Lisboa
            ["Xangai", "Zurich"], #Los Angeles
            ["Jacareí", "Quadra", "Roseira"],#Manaus
            ["Kiev", "Oiapoque"],#Namur
            ["Paris", "Washington"], #Nova York
            ["Namur", "Goiânia", "Xangai", "Viena"],#Oiapoque
            ["Herval", "Seul", "Yakutsk", "Lisboa", "Nova York"],#Paris
            ["Lisboa", "Manaus", "Seul"],#Quadra
            ["Manaus", "Kiev", "Tijuana", "Uberlandia"],#Roseira
            ["Paris", "Quadra"],#Seul
            ["Altair", "Washington"], #São Paulo
            ["Roseira"],#Tijuana
            ["Goiânia", "Xangai"], #Tokyo
            ["Roseira", "Oiapoque"],#Uberlandia
            ["Oiapoque", "Zurich"],#Viena
            ["Herval", "Nova York", "São Paulo"],#Washington
            ["Oiapoque","Tokyo", "Los Angeles"],#Xangai
            ["Paris"],#Yakutsk
            ["Viena", "Los Angeles"]#Zurich
       ]
"""
nos = ["Al","Be","Ca","De","El","Fr","Go","He","Il","Ja","Ki",
       "Li", "La","Ma","Na","Ny","Oi","Pa","Qu","Ro","Se","Sp","Ti","Tk","Ub","Vi",
       "Wa", "Xa", "Ya", "Zu"]

grafo = [["Be","He","Sp"],["Al","Ca","Il"],["Be","De"],
         ["Ca", "Il","Ja", "El"],["De","Ja", "Fr"],["El","Ki", "Go"],["Fr","Oi", "Tk"],
         ["Al","Wa","Pa"],["Be","De","Li"],
         ["De","El","Ki","Ma"],["Fr","Ja","Ro", "Na"],["Il","Pa","Qu"],
         ["Xa", "Zu"],["Ja","Qu","Ro"],["Ki","Oi"],["Pa", "Wa"],
         ["Na","Go","Xa", "Vi"],["He","Se","Ya", "Li", "Ny"],["Li","Ma","Se"],
         ["Ma","Ki", "Ti", "Ub"],["Pa","Qu"],["Al", "Wa"],
         ["Ro"],["Go", "Xa"],["Ro","Oi"],["Oi","Zu"],["He", "Ny", "Sp"],["Oi","Tk", "La"],
         ["Pa"],["Vi", "La"]
        ]

"""
# PROGRAMA PRINCIPAL
sol = busca()
caminho = []

origem  = "Berlin"
destino = "São Paulo"

caminho = sol.amplitude(origem,destino)
print("\nAmplitude...........: ",caminho)

caminho = sol.profundidade(origem,destino)
print("\nProfundidade........: ",caminho)

lim = 2
caminho = sol.prof_limitada(origem, destino, lim)
print("\n***** PROFUNDIDADE LIMITADA ( L =",lim-1,")*****\n",caminho)

lim = len(nos)
caminho = sol.aprof_iterativo(origem, destino, lim)
print("\n*****APROFUNDAMENTO ITERATIVO*****\n",caminho)

caminho = sol.bidirecional(origem,destino)
print("\n*****BDIRECIONAL*****\n",caminho)
