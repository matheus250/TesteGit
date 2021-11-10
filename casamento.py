#casamento
entrada_A = input()
entrada_B = input()

A = []
B = []


for a in entrada_A:
    A.append(a)
for b in entrada_B:
    B.append(b)

t_A = len(A)
t_B = len(B)

if t_A > t_B:
    for i in range(t_A - t_B):
        B.insert(0, 0)
elif t_B > t_A:
    for i in range(t_B - t_A):
        A.insert(0, 0)

for x in range(len(A)):
    if int(A[x]) > int(B[x]):
        B[x] = ''
    elif int(B[x]) > int(A[x]):
        A[x] = ''



saida_A = ''.join([str(i) for i in A])
saida_B = ''.join([str(l) for l in B])
if saida_A != '':
    saida_A = int(saida_A)
else:
    saida_A = -1

if saida_B != '':
    saida_B = int(saida_B)
else:
    saida_B = -1

if saida_A > saida_B:
    print(f'{saida_B} {saida_A}')
else:
    print(f'{saida_A} {saida_B}')