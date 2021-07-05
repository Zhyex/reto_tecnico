# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:17:44 2021

@author: Camilo
"""


from random import randint
from objetosjuego import *

class Carro:
    
    def __init__(self,jugador,f1):
        self.jugador=jugador
        self.f1=f1
        
# Dist_Pistas={'Monza':4.1,
#         'Bahrein':5.4,
#         'Portimao':4.6,
#         'Silverstone':5.8
#         }

Dist_Pistas={'Monza':4100,
        'Bahrein':5400,
        'Portimao':4600,
        'Silverstone':5800
        }


Pistas={'Monza':'4.1 km',
        'Bahrein':'5.4 km',
        'Portimao':'4.6 km',
        'Silverstone': '5.9 km'
        }
X=['Monza', 'Bahrein','Portimao','Silverstone']



#1. Configuración del juego

print('Bienvenido al Juego de Carros por consola!'+'\n' + 'Seleccione una de las siguientes pistas a continuación:\n' )
contador=1
for x, y in Pistas.items():
    print(str(contador)+'. ' + x, y)
    contador+=1
    

Seleccion=int(input("Seleccione una de las opciones anteriores. En caso de no querer jugar, ingrese el número 0 para finalizar el juego: "))
while True:
    if Seleccion==1:
        Seleccion=X[0]
        break
    elif Seleccion==2:
        Seleccion=X[1]
        break
    elif Seleccion==3:
        Seleccion=X[2]
        break
    elif Seleccion==4:
        Seleccion=X[3]
        break
    elif Seleccion==0:
        break
    print(Seleccion)
   

#!-------------------------------------especificar jugadores y crear los objetos con carros asignados

cantidad_jugadores=int(input("Por favor indique cuantas personas van a participar del juego: "))
carriles= []

distancia_pista=(Dist_Pistas.get(Seleccion))  

distancia_faltante=[]
for i in range(cantidad_jugadores):
    distancia_faltante.append(distancia_pista)  

for i in range (cantidad_jugadores):
    jugador=input("Ingrese su nombre: ")
    f1=input("Ingrese su vehiculo: ")
    formula=Carro(jugador,f1)
    carriles.append(formula)
    
def desplazamientos(lanzar):
    global desplazar
    dado=randint(1,6)
    desplazar=dado*100
    print(f"Distancia recorrida: {desplazar} metros.")
    return desplazar


#2. Inicio del juego
print("\nRecuerde que en el orden en el que se registraron los participantes, será el orden para avanzar en el juego.\n")



podio=[0,0,0]
while True:
    for i in range(len(carriles)):
        pulsa=input("Pulse . para lanzar dados: ")
        desplazamientos(pulsa)
        distancia_faltante[i]=distancia_faltante[i]-desplazar
        print(f"distancia para llegar a meta {distancia_faltante[i]} metros")
        if distancia_faltante[i]<=0:
            podio[0].append(carriles[i])
            carriles.pop(0)
    if podio[0]!=0:
        for i in range(len(carriles)):
            pulsa=input("Pulse . para lanzar dados: ")
            desplazamientos(pulsa)
            distancia_faltante[i]=distancia_faltante[i]-desplazar
            print(f"distancia para llegar a meta {distancia_faltante[i]} metros")
        
            
    
        





    






    

    
    