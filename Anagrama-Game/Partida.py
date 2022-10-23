from Anagrama import Anagrama
import random

class Partida:        
    __VogalPosicao=[]
    palpiteAnterior=''
    __Jogadas=0
    
    def __init__(self,palavraNormal:str):
        self.__palavraNormal=palavraNormal
        self.__anagrama= Anagrama(self.__palavraNormal)
        self.__Jogadas= (len(self.__anagrama.palavraEmbaralhada)+4)//2
    #== == == == Propertys e setters
    @property
    def Jogadas(self):
        return self.__Jogadas
    
    
    @property
    def anagrama(self):
        return self.__anagrama.palavraEmbaralhada
    
    #== == == == Métodos relacionados no palpite
    
    def ChecarPalpite(self,palpite:str)-> bool:
        self.palpiteAnterior=palpite
        if palpite == self.__anagrama: return True # o usuário adivinhou!
        else: return False # O usuário errou!
    
    #== == == == Dicas    
    def Dicas(self): 

        Numero=random.randint(1,3) # método para escolher as dicas de maneira aletória

        if Numero==1:
            self.PrimeirasLetras()

        if Numero==2:
            self.VogalPosicao()
        
        if Numero==3:
            self.LetraPosicao()

        
    def PrimeirasLetras(self):
        PrimeirasLetras= (self.__anagrama.__len__() +1 ) //3
        return f"Dica 1 : A palavra começa com a(s) letra(s): { self.__anagrama.palavraEmbaralhada[:PrimeirasLetras] }"

'''
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

'''