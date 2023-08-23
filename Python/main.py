inputs = []
sums = []
i = 0
y = 0.0

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
inputN = int(input(print("How many inputs?")))

while i<inputN:
    inputs.append(int(input(print("Write an input: "))))
    i+=1


i = 0
#pega os sums
sumN = int(input(print("How many sums?")))
while i<sumN:
    sums.append(int(input(print("Write a sum value: "))))
    i+=1
i = 0

summed = calculate_sum(inputs, sums)

print(f"Result of LR Function: {lr_function(summed)}")
print(f"Result of FR Function: {fr_function(summed)}")
print(f"Result of FS Function: {fs_function(summed)}")

#Caso necessitar, continua o programa para calcular mais expressões, só suporta uma soma
print("Continue?(Y/N)")
cont = input().capitalize()
if cont == 'Y':
    sumCont = []
    print("Write a sum value")
    sumCont.append(int(input()))
    #Um laço para printar todas as funções
    while True:
        
        print("Which function to use(1 for LR, 2 for FR, 3 for FS, 0 to exit): ")
        funct = int(input())

        if funct == 1:
            #Cria uma lista nova e insere o valor da função LR na mesma
            input_cont = []
            input_cont.append(lr_function(summed))
            #                                           \  / calcula uma nova soma com o peso provido
            #                                            \/  e com a lista criada no if 
            print(f"Result of LR function: {lr_function(sum(x * y for x, y in zip(input_cont, sumCont)))}")
        elif funct == 2:
            input_cont = []
            input_cont.append(fr_function(summed))
            #                                           \  / calcula uma nova soma com o peso provido
            #                                            \/  e com a lista criada no if 
            print(f"Result of FR function: {fr_function(sum(x * y for x, y in zip(input_cont, sumCont)))}")
        elif funct == 3:
            input_cont = []
            input_cont.append(fs_function(summed))
            #                                           \  / calcula uma nova soma com o peso provido
            #                                            \/  e com a lista criada no if 
            print(f"Result of FS function: {fs_function(sum(x * y for x, y in zip(input_cont, sumCont)))}")
        elif funct == 0:
            break
