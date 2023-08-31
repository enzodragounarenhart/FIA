ent1 = [0, 0, 1]
ent2 = [0, 1, 1]
ent3 = [1, 0, 1]
ent4 = [1, 1, 1]


entradas = [ent1, ent2, ent3, ent4]

s0 = 0
s1 = 1

def fun_ajuste(entrada, sd, so, pesos):

    
    p1_aj = pesos[0] + 1 * (sd - so) * entrada[0]
    p2_aj = pesos[1] + 1 * (sd - so) * entrada[1]
    p3_aj = pesos[2] + 1 * (sd - so) * entrada[2]
    
    return [p1_aj, p2_aj, p3_aj]

#FUNÇÃO QUE RETORNA O VALOR DA SOMA QUANDO É APLICADA A FUNÇÃO RÁPIDA
def fr_function(soma):
    if soma < 0:
        return 0
    elif 0 <= soma <= 1:
        return soma
    else:
        return 1
    
    #CALCULA E RETORNA A SOMA INICIAL
def calculate_sum(entrada: int, peso: int):
    #Realiza a soma dos inputs com os pesos
    return sum(x * y for x, y in zip(entrada, peso))

print("Digite os pesos: ")
entrada = input().split()

pesos = []

for num in entrada:
    number = int(num)
    pesos.append(number)

i = 0

print(calculate_sum(entradas[1], pesos))


soma = fr_function(calculate_sum(entradas[1], pesos))

entrada_x = entradas[1]
print(entrada_x)
print(fun_ajuste(entradas[1], s0, soma, pesos))

while soma != s1:
    soma = fr_function(calculate_sum(entradas[1], pesos))
    pesos = fun_ajuste(entradas[1], s0, soma, pesos)
    print(pesos)
    
        
    

if soma == s0:
    print("0")
    
elif soma == s1:
    print("1")