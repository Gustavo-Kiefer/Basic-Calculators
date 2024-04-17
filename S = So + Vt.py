import math

# S = So + vot

#para conversao
km = 3.6


So = float(input('Posição inicial: '))

vo = float(input('Velocidade: '))

m = (input('Em que unidade esta o valor? m/s ou km/h?: '))
if m == "km":
        vdc = (float(vo/km))
        print ('Sua unidade foi convertida')
else: vdc = vo

t = float(input('Tempo: '))

#formula final
S = float(So + vdc * t)

print (S)