#exercicio Fase 3 OBI nivel 1 "Sapo"
N, M = [int(i) for i in input().split()] #lendo entrada
lago = []
#criando o lago
for j in range(M):
    lago.append([])
    for i in range(N):
        lago[j].append(0)

# grafo nao direcionado
# exemplo: {1: [4], 2: [6], 3: [], 4: [1, 5], 5: [4, 6], 6: [2, 5]}
# 6 vertices e suas listas de adjacencias
grafo = {}
pedras = []
P = int(input()) #numero de pedras(vertices do grafo)
#adicionando pedras no lago que sao os vertices do grafo
for x in range(P):
    C, L = [int(i) for i in input().split()]
    lago[L-1][C-1] = x+1
    grafo[x+1] = []  #inicializa a lista de adjacencias do grafo
    pedras.append([L-1, C-1])

Col, Linha = [int(i) for i in input().split()] # lendo posicao  do sapo
Vert_sapo = lago[Linha-1][Col-1] #salvando o vertice em que o sapo esta em vert_sapo
x, y = [int(i) for i in input().split()] # lendo posicao da namorada
Vert_Namorada = lago[y-1][x-1]  #salvando o vertice em que a namorada esta na variavel Vert_Namorada

#esta funcao adiciona uma aresta ao grafo
def adiciona_aresta(origem, destino):
    global grafo
    grafo[origem].append(destino)

#esta funcao olha para os pontos vizinhos de dada posicao e verifica se tem uma pedra em 1 ou mais vizinhos e adiciona uma aresta entre os dois
def verifica_posicoes(L, C):
    if L+1 < M:
        if lago[L+1][C] > 0:
            adiciona_aresta(lago[L+1][C], lago[L][C])
    if L-1 >= 0:
        if lago[L-1][C] > 0:
            adiciona_aresta(lago[L-1][C], lago[L][C])
    if C+1 < N:
        if lago[L][C+1] > 0:
            adiciona_aresta(lago[L][C+1], lago[L][C])
    if C-1 >= 0:
        if lago[L][C-1] > 0:
            adiciona_aresta(lago[L][C-1], lago[L][C])
    if L+2 < M:
        if lago[L+2][C] > 0:
            adiciona_aresta(lago[L+2][C], lago[L][C])
    if L-2  >= 0:
        if lago[L-2][C] > 0:
            adiciona_aresta(lago[L-2][C], lago[L][C])
    if C+2 < N:
        if lago[L][C+2] > 0:
            adiciona_aresta(lago[L][C+2], lago[L][C])
    if C-2 >= 0:
        if lago[L][C-2] > 0:
            adiciona_aresta(lago[L][C-2], lago[L][C])
    if C-3 >= 0:
        if lago[L][C-3] > 0:
            adiciona_aresta(lago[L][C-3], lago[L][C])
    if C+3 < N:
        if lago[L][C+3] > 0:
            adiciona_aresta(lago[L][C+3], lago[L][C])
    if L+3 < M:
        if lago[L+3][C] > 0:
            adiciona_aresta(lago[L+3][C], lago[L][C])
    if L-3 >= 0:
        if lago[L-3][C] > 0:
            adiciona_aresta(lago[L-3][C], lago[L][C])
#para cada pedra no lago, verifico seus vizinhos
for i in pedras:
    verifica_posicoes(i[0], i[1])

# variaveis auxiliares do DFS
color = {}
parent = {}
achou_Namorada = False
#inicializando as variaveis auxiliares do DFS em base do grafo pronto
for u in grafo.keys():
    color[u] = 'W'
    parent[u] = None


#defino o destino do meu DFS(que eh a namorada)
color[Vert_Namorada] = 'N'


def dfs(u, color, parent):
    global achou_Namorada
    color[u] = 'V'
    aux = 0
    for v in grafo[u]:
        if color[v] == 'N':
            achou_Namorada = True
            return
        elif color[v] == 'W':
            parent[v] = u
            dfs(v, color, parent)

#executa o DFS partindo da posicao do Sapo em busca da namorada
dfs(Vert_sapo, color, parent)

#saida, achou ou nao
if achou_Namorada == True:
    print('S')
else:
    print('N')