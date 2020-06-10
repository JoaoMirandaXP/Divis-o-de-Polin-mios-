o_divisor = int(input("Ordem do divisor :"))
o_dividendo = int(input("Ordem do dividendo :"))
coef_divisor = []
coef_dividendo = []

for x in range(o_dividendo+1):
    coef_divisor.append(input("Insira o #{} coeficiente do dividendo : ".format(x+1)))

for x in range(o_divisor+1):
    coef_divisor.append(input("Insira o #{} coeficiente do divisor : ".format(x+1)))

for x in coef_divisor:
    coef_dividendo[x] = x * coef_dividendo 

#---------------------
#---Resultado Final---
#D(x) = 
#d(x) = 
#Q(x) =
#R(x) =
#---------------------