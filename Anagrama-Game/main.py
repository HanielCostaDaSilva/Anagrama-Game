import time
from Anagrama import Anagrama
import random

#====== Métodos
def embaralhar(palavra): # Método ultilizado para embaralhar a palavra

  lista = list(palavra) 
  random.shuffle(lista)
  minhaString = ''.join(lista)
  return minhaString

#------ Dicas
    

#Dica dada atráves da demonstração das primeiras letras

#====== Começo do jogo
PalavraNormal=str.lower(input('Antes de começar o jogo, digite uma palavra: (mínimo de 4 letras): \n')) #o programa recebe a palavra do Usuário
print("_-=-_"*30)

while len(PalavraNormal)<4: #Caso possua menos que 4 letras, o programa irá exigir uma outra palava com uma quantidade maior 

    PalavraNormal=str.lower(input('Por favor digite uma outra palavra com no mínimo 4 letras \n'))
    print("_-=-_"*30)

PalavraEmbaralhada=embaralhar(PalavraNormal) # A palavra é então embaralhada
print("VAMOS COMEÇAR O JOGO!") # E começa o jogo

#-------- Variáveis importantes

PalavrasTentadasLista=[]# Lista para armazenadas as palavras utilizidas pelo usuário

#---Variáveis Para a dica de vogais



PalavraVogaisCuringa=list(PalavraEmbaralhada)

PosicacaoVogais=[]
VogaisListas=["a","e","i","o","u","â","á",'ã',"é","ê","í","î","ô",'ó','õ','ú','û']

#Variáveis para o número de tentativas

cont=0
#====== Funcionamento do programa

while cont < TentativaLimite: # O programa funciona até o contador chegar ao limite
    
    print("_-=-_"*30)
    print(f"Você tem {TentativaLimite-cont} tentativas!")        
#------ Variáveis para o palpite
    palpite=[] # O palpite é uma lista para ficar mais fácil para visualização e análise das letras informadas pelo usuário
    LetraPalpiteNum=0 # Para informar qual o número da letra que o usuário deve informar
    palavraCuringa=list(PalavraNormal) # Ela funciona como um curinga para a palavra embaralhada. Vai ser usada para receber e excluir letras da palavra normal no processo do programa
    palavraFormada=[] # Recebe as letras que o usuário está digitando e no final as tranforma em uma palavra
    letrasRestantes=len(PalavraEmbaralhada)# 

#======= Recebendo o palpite do usuário    
    while len(palpite)!= len(PalavraEmbaralhada): # Enquanto o palpite não tiver a mesma quantidade de levras que a palavra embaralhada
        
        letra= str.lower(input(f"\nDigite a {LetraPalpiteNum+1}ª letra do seu palpite: \n")) #variável que armazena a letra dada pelo usuário 
        while letra not in palavraCuringa: #Caso a letra não esteja presente na palavra dada pelo usuário ou ela já tenha sido informada 
            
            letra= str.lower(input(f"A letra digitada ou já foi digitada ou não está presente na palavra embaralhada, por favor \n Digite a {LetraPalpiteNum+1}ª letra do seu palpite: \n")) # O usuário é forçado a informar uma letra até que seja informada uma dentro da palavra embaralhada
        
        print("+=+"*30)    
        palavraCuringa.remove(letra) #A letra informada é removida da Palavra Curinga, a fim de evitar repetições indesejadas
        palavraFormada.append(letra)# A letra é adicionada à lista, a fim de informá-lo quais letras que ele já informou
        
        print(f" palavra formada até agora: {''.join(palavraFormada)}", "_ "*(letrasRestantes-1),f"letras que ainda faltam: {', '.join(palavraCuringa)}" )
        letrasRestantes-=1
            
        palpite.append(letra)# o palpite vai receber a letra, depois que todas as exigências foram conclúidas
        LetraPalpiteNum+=1    
    
    cont+=1
#======= Analisando se a a palavra escrita é igual a palavra embaralhada

#------ Caso o palpite esteja errado e a quantidade de tentativas possíveis ainda é menor que o limite    
    if ''.join(palpite) != PalavraEmbaralhada and cont<TentativaLimite:
    
        print("Essa não foi a palavra que foi formada!")
        PalavrasTentadasLista.append(''.join(palpite)) #adiciona o palpite que o usuário deu na lista de palavras tentas
        print(f"você ainda tem {TentativaLimite-cont} tentativa(s) \n")# informa a quantidade de tentativas
        print("As palavras que você criou até agora foram: ", PalavrasTentadasLista)#informa a lista
        print(f"\n Só para lembrar... A palavra antes de ser embaralhada era: {PalavraNormal}")# Apressenta a palavra antes de ser embaralhada
        print("_-=-_"*30)
        print("Lá vem uma dica escolhida aleatoriamente: ")
                
        Dicas(palpite) #O programa chama a função dica a função  Dicas que irá gerar uma dica aleatória
        
#------ Caso o palpite esteja certo e o contador não utlrapassou o limite 
    elif ''.join(palpite) == PalavraEmbaralhada:
        print("Parabéns! Você acertou!")
        print(f"Você ainda tinha {TentativaLimite-cont} tentativa(s) \n") # Mostra a quantidade de tentativas que o usuário ainda tinha
        print("<3 "*30)
        cont= TentativaLimite #o cont recebe a quantidade de tentativas para que o programa encerre 

#------ Caso o palpite esteja errado e o contador ultrapassou o limite 
    else:
        print("Que pena, não foi dessa vez! Boa sorte na próxima!\n")
        print ("</3 "*30)   

    time.sleep(3)

print("A palavra embaralhada era: "+ PalavraEmbaralhada) # o usuário é informado qual a palavra embaralhada
input("GAME OVER \npressione a tecla 'Enter' para sair...")