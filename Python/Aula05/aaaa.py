"""ent1 = [0, 0]
ent2 = [0, 1]
ent3 = [1, 0]
ent4 = [1, 1]

entradas = [ent1, ent2, ent3, ent4]

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

print(calculate_sum(ent1, pesos))


soma = fr_function(calculate_sum(ent1, pesos))


saida = fr_function(calculate_sum(entradas[2], pesos))
if saida != s1:
    entX = entradas[2]
    print(fun_ajuste(entX[0], entX[1], s0, saida, pesos[0], pesos[1]))
i+=1

if soma == s0:
    print("0")
    
elif soma == s1:
    print("1")
    
print(entradas)"""

#FUNÇÃO QUE RETORNA O VALOR DA SOMA QUANDO É APLICADA A FUNÇÃO RÁPIDA
def fr_function(soma):
    if soma < 0:
        return 0
    elif 0 <= soma <= 1:
        return soma
    else:
        return 1

#CALCULA E RETORNA A SOMA INICIAL
def calculate_sum(inputs, weights):
    #Realiza a soma dos inputs com os pesos
    return sum(x * y for x, y in zip(inputs, weights))

#FUNÇÃO DE AJUSTE UTILIZANDO A REGRA DELTA:
def fun_ajuste(inputs, weights, so, sd):
    w1, w2 = weights
    y = 0
    
    w1_adj = w1 + 1 * (sd - so) * inputs[0]
    w2_adj = w2 + 1 * (sd - so) * inputs[1]
    
    #RETORNA UMA LISTA COM OS VALORES 
    return [w1_adj, w2_adj]

    #CODIGO PARA ACEITAR N ITERAÇÕES
    #while y < qtd:
    #   return weights[y] + 1 * (sd - so) * inputs[y]
    #   y += 1
    
    
    
weights = []
inputs = []

print("Digite os pesos iniciais(separados por espaço): ")
ent = input().split()

for num in ent:
    number = int(num)
    weights.append(number)

print("Insira os inputs (separados por espaço)(0 para sair):")
entrada = input().split()

for num in entrada:
    number = int(num)
    inputs.append(number)

i = 0

print("Digite a saída desejada: ")
sd = int(input())

while True:
    

        
    saida = fr_function(calculate_sum(inputs, weights))

    print(saida)
    
    
    if saida != sd:
        weights = fun_ajuste(inputs, weights, saida, sd)
    else: 
        print("Treinamento completo!")
        break
    inputs.clear()
    i += 1
            
    