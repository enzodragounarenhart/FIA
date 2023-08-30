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
def fun_ajuste(inputs, weights, so, sd, qtd):
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

i = 0

while True:
    print(weights)
    print("Insira os inputs (separados por espaço)(0 para sair):")
    entrada = input().split()
    
    if entrada == ['0']:
        break
    
    for num in entrada:
        number = int(num)
        inputs.append(number)
        
    saida = fr_function(calculate_sum(inputs, weights))

    print(saida)
    
    print("Digite a saída desejada: ")
    sd = int(input())
    if saida != sd:
        weights = fun_ajuste(inputs, weights, saida, sd)
    else: 
        print("Treinamento completo!")
        break
    inputs.clear()
    i += 1
            
    