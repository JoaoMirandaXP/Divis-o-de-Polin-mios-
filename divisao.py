import numpy as np 

o_divisor = int(input("Ordem do divisor :"))
o_dividendo = int(input("Ordem do dividendo :"))
o_quociente = o_dividendo - o_divisor
o_resto = o_divisor -1
coef_divisor = []
coef_dividendo = []
coef_final = []

for x in range(o_divisor+1):
    coef_divisor.append(float(input("Insira o #{} coeficiente do divisor : ".format(x+1))))

for x in range(o_dividendo+1):
    coef_dividendo.append(float(input("Insira o #{} coeficiente do dividendo : ".format(x+1))))
for x in range(o_quociente+1):
    coef_final.append([])

#Distributiva da parte literal 
for y in range(1,o_quociente+1):
    for x in coef_divisor: 
            coef_final[y].append(x*y)
print(coef_final)
def resolveSistema():
    A = np.array(coef_final)
    B = np.array(coef_dividendo) 
    return np.linalg.inv(A).dot(B)

print(coef_dividendo)
print(coef_divisor)
print(coef_final)
#print(resolveSistema())

#print(---------------------)
#print(---Resultado Final---)
#D(x) = 
#d(x) = 
#Q(x) =
#R(x) =
#print(---------------------)