#plano
N = int(input())
vagas = {}
clientes = {}
for x in range(N):
    vagas[x+1] = 'n'

M = int(input())
for i in range(M):
    clientes[i+1] = int(input())

contador_vagas_ocupadas = 0    
for cliente in clientes.keys():
    if clientes[cliente] > 0:
        for j in range(clientes[cliente]):                    
            if vagas[clientes[cliente] - j] == 'n':
                vagas[clientes[cliente] - j] = 'o'
                contador_vagas_ocupadas += 1
                clientes[cliente] = 0
                break
        if clientes[cliente] > 0:
            break




print(contador_vagas_ocupadas)