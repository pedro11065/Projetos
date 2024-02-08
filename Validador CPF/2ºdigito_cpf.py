CPF= "50774811803"
print(f'CPF = {CPF}')

i = 0
m = 11
cont = 9
c = 0
l = []

while i <= cont:

    i_int = CPF[i]
    num = (int(i_int))

    r = num*m

    l.append(r)

    i = i + 1
    m = m - 1

    continue

soma_num = 0

for num_1 in l:
    soma_num += num_1

r_full = soma_num * 10

r_final = r_full % 11
print(f"Esse CPF gera o primeiro dígito como {r_final}")
        
