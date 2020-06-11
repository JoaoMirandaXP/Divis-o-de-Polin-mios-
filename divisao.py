import numpy as np 

o_divisor = int(input("Ordem do divisor :"))
o_dividendo = int(input("Ordem do dividendo :"))
o_quociente = o_dividendo - o_divisor
o_resto = o_divisor -1
coef_divisor = []
coef_dividendo = []
coef_final = []
sistema = []
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for x in range(o_divisor+1):
    coef_divisor.append(float(input("Insira o #{} coeficiente do divisor : ".format(x+1))))

for x in range(o_dividendo+1):
    coef_dividendo.append(float(input("Insira o #{} coeficiente do dividendo : ".format(x+1))))
    sistema.append([])
for x in range(o_quociente+1):
    coef_final.append([])

#Distributiva da parte literal 
for y in range(o_quociente+1):
    for x in coef_divisor: 
        coef_final[y].append(x)

for x in range(o_dividendo+1):
    for y in range(len(coef_dividendo)):
        sistema[x].append(0) 
print(sistema)

def organizaSistema(coefs):
    i=0
    z=0
    for x in range(len(sistema)):
        if(x<len(coef_final)):
            
            for y in range(len(coef_final[0])):    
                sistema[x][y+i] = coef_final[x][y]
            i=i+1
        else:
            
            while(z<=o_resto):
                print(z)
                sistema[-o_resto - z][-o_resto - z] = 1 
                z=z+1
            
    print(sistema)



def resolveSistema():
    a = np.array(sistema)
    A = a.transpose()
    B = np.array(coef_dividendo)
    i = 0
    solucao = np.linalg.inv(A).dot(B)
    print('Os coeficientes são :')
    print('----------------')  
    for x in solucao:
        print("{} = {}".format(alfabeto[i],x)) 
        i=i+1
    print('----------------')
    return solucao

print(coef_dividendo)
print(coef_divisor)
print(coef_final)
organizaSistema(coef_final)
print(resolveSistema())

#print(resolveSistema())

#print(---------------------)
#print(---Resultado Final---)
#D(x) = 
#d(x) = 
#Q(x) =
#R(x) =
#print(---------------------)