inputs = []
sums = []
i = 0

#Calcula a função LR
def lr_function(soma):
    if soma <= 0:
        y = -1
        LRSum = y
        return LRSum
    elif soma > 0:
        y = 1
        LRSum = y
        return LRSum
    
#Calcula a função FR
def fr_function(soma):
    if soma < 0:
        y = 0
        FRSum = y
        return FRSum
    elif soma >=0 and soma <=1:
        y = soma
        FRSum = y
        return FRSum
    elif soma > 1:
        y = 1
        FRSum = y
        return FRSum

#Calcula a função FS      
def fs_function(soma):
    if soma >= 0:  
        y = 1 - (1/(1+soma))
        FSSum = y
        return FSSum
    elif soma < 0:
        y = -1 + (1/(1-soma))
        FSSum = y
        return FSSum

def calculate_sum(inputs, sums):
    #Realiza a soma dos inputs com os pesos
    return sum(x * y for x, y in zip(inputs, sums))

#Pega os inputs
print("Escreva duas entradas: ")

while i<2:
    inputs.append(int(input()))
    i+=1
i = 0

print("Escreva os pesos na mesma ordem das entradas: ")
while i<2:
    sums.append(int(input()))
    i+=1
i = 0  

summed = calculate_sum(inputs, sums)

print(f"Soma: {summed}")

while True:
    print("Escolha a funcao a ser utilizada(1 para LR, 2 para FR e 3 para FS, 0 para sair): ")
    func = int(input())
    
    if func == 1:
        print(f"Resultado da funcao LR: {lr_function(summed)}")
    elif func == 2:
        print(f"Resultado da funcao LR: {fr_function(summed)}")
    elif func == 3:
        print(f"Resultado da funcao LR: {fs_function(summed)}")
    elif func == 0:
        break