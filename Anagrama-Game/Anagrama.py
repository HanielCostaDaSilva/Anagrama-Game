import random
import time

#====== Métodos
def embaralhar(palavra): # Método ultilizado para embaralhar a palavra

  lista = list(palavra) 
  random.shuffle(lista)
  minhaString = ''.join(lista)
  return minhaString

#------ Dicas
def Dicas(palpite): 

    Tipo=random.randint(1,3) # método para escolher as dicas de maneira aletória

    if Tipo==1:
        PrimeirasLetras()

    if Tipo==2:
        VogalPosicao()
    
    if Tipo==3:
        LetraPosicao(palpite)
    

#Dica dada atráves da demonstração das primeiras letras
def PrimeirasLetras():
    PrimeirasLetras= ( len(PalavraEmbaralhada)+1 ) //3   #para ficar um jogo mais balanceado, a quantidade de letra será dada de acordo com a quantidade de letras da palavra embaralhada
    
    print(f"Dica 1 : A palavra começa com a(s) letra(s): { PalavraEmbaralhada[:PrimeirasLetras] }")

#------Dica dada através da posição da vogal
def VogalPosicao():
    Teste=True #A varíavel Teste serve para verificar se há alguma vogal na palavra embaralhada e para o funcionamento
    print("Dica 2: há uma vogal na posição... ")    
    
    for i in range(len(PalavraEmbaralhada)): # a varíavel i vai pecorrer toda a palavra embaralhada
    
        if str.lower(PalavraEmbaralhada[i]) in VogaisListas: #Caso seja encontrada alguma vogal na palavra embaralhada
            Teste=True
            break #Não vai continuar a repetição, a fim de que a váriavél Teste continue True
        
        else: 
            Teste=False # Não foi achada qualquer vogal.
    
    if Teste!=True: # caso nenhuma vogal foi encontrada
        print("Não há vogais!")

    for i in range(len(PalavraVogaisCuringa)): # A palavra curinga irá ser pecorrida a fim de procurar por vogais
    
        if Teste !=True: # Ora a palavra embaralhada não possui vogais, ora foi achada uma vogal
            break
              
        for j in range (len(VogaisListas)): #A variável j irá pecorrer a lista de vogais
            
            if PalavraVogaisCuringa[i]==VogaisListas[j]: # Caso uma vogal seja encontrada

                print (f"A vogal '{VogaisListas[j] }', se encontra na { i +1 }ª posiçao  ") # O programa vai dizer qual é a vogal e em qual posição ela se encontra
                PosicacaoVogais.append([VogaisListas[j],[i+1]])# A lista Posicao Vogais irá receber qual a vogal e a posição dela, a fim de usá-la
                PalavraVogaisCuringa[i]=0 # Para que quando o método seja usado novamente a mesma letra seja mostrada para o usuário, ou ocorra alterações no indíces da lista, a vogal da palavra curinga será trocada por um outro caractér
                Teste= False 
                break
        
     

    if len(PosicacaoVogais)>=1:# Essa condição irá mostrar as vogais e suas posições que foram inclúidas na lista Posicao vogais 
        print('+='*30)
        print("Essas são as vogais encontradas até agora: \n")
        
        for i in range (len(PosicacaoVogais)):
            print(f" Vogal {PosicacaoVogais[i][0]}, posição {PosicacaoVogais[i][1]} ")
    
    return None



#------Dica Através da posiçao de uma letra
def LetraPosicao(palpiteLista):
    print("Dica 3: Conferindo as posições das letras: ")
    VerificarVezes=(len(palpiteLista)+1) // 2 #Formúla para verificar de maneira justa as letras do palpite do usuário
    VerificarPalavraEmbaralhada=list(PalavraEmbaralhada) #variável usada para verificar a posição da letra na palavra embaralhada
    while VerificarVezes>0:
        
        VerificarIndice=random.randint(0,len(palpiteLista)-1) # o mesmo índice da lista do palpite e o da palavrava embaralhada é escolhido aleatoriamente, devido a isso, possa ser que o mesmo índice pode ser usado novamente
    
        if palpiteLista[VerificarIndice] == VerificarPalavraEmbaralhada[VerificarIndice]: # caso forem iguais a letra do palpite e o da palavra Embaralhada 
            print(f"a letra '{palpiteLista[VerificarIndice]}' está no local correta!! posição colocada no palpite: {VerificarIndice+1}")
                    
        else: #caso não forem iguais a letra do palpite e o da palavra
            print(f"a letra '{palpiteLista[VerificarIndice]}' está na posição Errada!! posição colocada no palpite: {VerificarIndice+1 }")
        
        VerificarVezes-=1    
    return True

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

VogaisListas=["a","e","i","o","u","â","á",'ã',"é","ê","í","î","ô",'ó','õ','ú','û']

PalavraVogaisCuringa=list(PalavraEmbaralhada)

PosicacaoVogais=[]

#Variáveis para o número de tentativas
TentativaLimite= (len(PalavraEmbaralhada)+4)//2

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