##Ahorcado

import random
import string

from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()

def ahorcado():
    
    print("=================================")
    print("Bienvenido al juego del ahorcado")
    print("=================================")

    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar = set(palabra) 
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra:").upper()

        #Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras adivinadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #Si la letra esta en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('¡Correcto!')
            else: 
                vidas -= 1
                print(f'¡Incorrecto! La letra {letra_usuario} no esta en la palabra')

        #Si la letra escogida por el usuario ya fue ingresada    
        elif letra_usuario in letras_adivinadas:
            print(f'¡Ya has ingresado la letra {letra_usuario}!')
        
        else:
            print('Esta letra no es valida')
    
    #El juego llega a esta linea cuadno se adivinan todas las letras de la palabra o cuando se agota las vidas del jugador
    if vidas == 0:
        print(f'¡Perdiste! La palabra era {palabra}')
    else:
        print(f'¡Ganaste! La palabra era {palabra}')
    
ahorcado()
            
            
            