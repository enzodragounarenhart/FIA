x0 = 0
y0 = 0
x1 = 0
y1 = 1
x2 = 1
y2 = 0
x3 = 1
y3 = 1

s0 = 0
s1 = 1

def fun_ajuste(_x, _y, sd, so, p1, p2):

    
    p1_aj = p1 + 1 * (sd - so) * _x
    p2_aj = p2 + 1 * (sd - so) * _y
    
    return [p1_aj, p2_aj]

#FUNÇÃO QUE RETORNA O VALOR DA SOMA QUANDO É APLICADA A FUNÇÃO RÁPIDA
def fr_function(soma):
    if soma < 0:
        return 0
    elif 0 <= soma <= 1:
        return soma
    else:
        return 1
    
    #CALCULA E RETORNA A SOMA INICIAL
def calculate_sum(_x, _y, p1, p2):
    #Realiza a soma dos inputs com os pesos
    return (_x * p1 ) + (_y * p2)

print("Digite os pesos: ")
entrada = input().split()

pesos = []

for num in entrada:
    number = int(num)
    pesos.append(number)

i = 0

print(calculate_sum(x0,y0, pesos[0], pesos[1]))


soma = fr_function(calculate_sum(x0, y0, pesos[0], pesos[1]))

if soma == s0:
    print("0")
    
elif soma == s1:
    print("1")