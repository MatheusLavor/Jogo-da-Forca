lista_palavras= ["abacaxi","melao","bolsonaro","lula","morango"]
letras_acertadas=""
tentativas=0
letras_tentadas=""
ativo=True

import os
import random
palavra_aleatoria= random.choice(lista_palavras)
vidas= len(palavra_aleatoria)

def fim_jogo(palavra_completa,tentativas):
        while True:
            os.system("cls")
            print(f"Voce ganhou o jogo, a palavra era {palavra_completa}")
            print(f"Voce teve um total de {tentativas} tentativas")
            jogar= input("deseja jogar novamente? ").upper()
            if jogar =="S":
                letras_acertadas=""
                tentativas=0
                palavra_aleatoria= random.choice(lista_palavras)
                letras_tentadas=""
                vidas=len(palavra_aleatoria)
                return(letras_acertadas,tentativas,vidas,palavra_aleatoria,letras_tentadas)
            elif jogar== "N":
                return None
            else:
                print("Voce não digitou algo compativel, tente novamente!")
                continue
            
        

def obter_letra():
    letra_vez=input("digite uma letra para a tentativa atual: ")
    return(letra_vez)
def montar_palavra(palavra_aleatoria,letras_acertadas):
    palavra_completa=""
    for palavra_montada in palavra_aleatoria:
        if palavra_montada in letras_acertadas:
            palavra_completa+=palavra_montada
        else:
            palavra_completa+="*"
    print(palavra_completa)
    return(palavra_completa)

while ativo:
    letra_vez=obter_letra()
    if len(letra_vez) >1:
        print("voce digitou mais de uma letra, tente novamente")
        continue    
    
    tentativas+=1
    if letra_vez in letras_tentadas:
        print("Voce ja tentou essa letra!")
        continue
    letras_tentadas+=letra_vez
    if letra_vez in palavra_aleatoria:
        letras_acertadas+= letra_vez
     
    if letra_vez not in palavra_aleatoria:
        vidas -=1
        print("voce errou tente novamente")
        print(f"Vidas:{vidas}")
        if vidas == 0:
            print("Voce perdeu o jogo ")  
            
            while True:
                jogar= input("Deseja Tentar Novamente?: ").lower()
                if jogar == "s":
                    os.system("cls")
                    letras_acertadas=""
                    tentativas=0
                    palavra_aleatoria= random.choice(lista_palavras)
                    letras_tentadas=""
                    vidas= len(palavra_aleatoria)
                    break
                if jogar == "n":
                    os.system("cls")
                    print("Voce saiu do jogo!")
                    ativo=False
                    break
                    
                else:print("Voce nao digitou algo compativel!")
        continue
    palavra_completa=montar_palavra(palavra_aleatoria,letras_acertadas)
    
    if palavra_completa==palavra_aleatoria:
        resultado = fim_jogo(palavra_completa, tentativas)

        if resultado is None:
            ativo = False
        else:
            letras_acertadas, tentativas, vidas, palavra_aleatoria, letras_tentadas = resultado