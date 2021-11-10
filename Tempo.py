N = int(input())

eventos = []
amigos = {}

# ler os eventos e inicializar todos os amigos
for i in range (N):
	aux = input()
	eventos.append(aux)
	codigo, x = aux.split()
		
	if codigo == 'R':
		#checar se o amigo ja existe
		if x in amigos:
			amigos[x]['respondido'] = False 
			#ja foi inicializado
		else:
			amigos[x] = {
				"contador": 0,
				"respondido": False,
				"inicializado": False
			}
	
for e in range(len(eventos)):
	codigo, x = eventos[e].split()
	for amigo in amigos:
		if codigo == 'E':
			if x == amigo:
				amigos[amigo]['respondido'] = True
				amigos[amigo]['inicializado'] = False
			else:
				if amigos[amigo]['inicializado'] == True:
					if e - 1 > 0:
						if eventos[e-1].split()[0] != 'T':
							amigos[amigo]['contador'] += 1

		elif codigo == 'R':
			if x == amigo:
				amigos[amigo]['respondido'] = False
				amigos[amigo]['inicializado'] = True
			else:
				if amigos[amigo]['inicializado'] == True:
					if e - 1 > 0:
						if eventos[e-1].split()[0] != 'T':
							amigos[amigo]['contador'] += 1

		else:
			if amigos[amigo]['inicializado'] == True:
					amigos[amigo]['contador'] += int(x)
		

print(amigos)