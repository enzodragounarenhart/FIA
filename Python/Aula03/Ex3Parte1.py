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
print("Escreva uma entrada: ")

while i<1:
    inputs.append(int(input()))
    i+=1
i = 0

print("Escreva o peso: ")
while i<1:
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
    
sumCont = []
print("Write a sum value")
sumCont.append(int(input()))

while True:
        
        print("Escolha a funcao a ser utilizada(1 para LR, 2 para FR e 3 para FS, 0 para sair): ")
        funct = int(input())

        if funct == 1:
            #Cria uma lista nova e insere o valor da função LR na mesma
            input_cont = []
            input_cont.append(lr_function(summed))
            #                                           \  / calcula uma nova soma com o peso provido
            #                                            \/  e com a lista criada no if 
            print(f"Resultado da funcao LR: {lr_function(sum(x * y for x, y in zip(input_cont, sumCont)))}")
        elif funct == 2:
            input_cont = []
            input_cont.append(fr_function(summed))
            #                                           \  / calcula uma nova soma com o peso provido
            #                                            \/  e com a lista criada no if 
            print(f"Resultado da funcao FR: {fr_function(sum(x * y for x, y in zip(input_cont, sumCont)))}")
        elif funct == 3:
            input_cont = []
            input_cont.append(fs_function(summed))
            #                                           \  / calcula uma nova soma com o peso provido
            #                                            \/  e com a lista criada no if 
            print(f"Resultado da funcao FS: {fs_function(sum(x * y for x, y in zip(input_cont, sumCont)))}")
        elif funct == 0:
            break
