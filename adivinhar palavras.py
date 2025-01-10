import random

palavra = ["cão", "gato", "pato", "vaca", "piriquito", "papagaio"]

palavra_random = (random.choice(palavra))

oculto = ['_'] * len(palavra_random)


tamanho = len(palavra_random)

print("Bem vindo ao jogo de advinhação!")

vidas = 6

while vidas > 0:
    print(f"a sua palavra tem {tamanho} letras: {oculto}")

    tentativa = input(f"escreva uma letra: ").lower()

    if tentativa in palavra_random:

        for i in range(len(palavra_random)):
                if palavra_random[i] == tentativa:
                    oculto[i] = tentativa
        if '_' not in oculto:
             print(f"Parabéns! Você adivinhou a palavra: {palavra_random}")
             break
    else:
        vidas -= 1
        print(f"perdeste uma vida, agora tens apenas {vidas}")

        if vidas == 0:
            print("fim de jogo")







