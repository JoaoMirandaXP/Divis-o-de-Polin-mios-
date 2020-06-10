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

#Distributiva da parte literal 
for x in coef_divisor: 
    

print(coef_dividendo)
print(coef_divisor)
print(coef_final)
#print(---------------------)
#print(---Resultado Final---)
#D(x) = 
#d(x) = 
#Q(x) =
#R(x) =
#print(---------------------)