from Anagrama import Anagrama,AnagramaException
import random

class Partida:        
    __VogaisReveladasLista=[]
    __VogaisReveladasString=''
    
    __jogadasPossiveis=0
    palpite=''

    def __init__(self,palavraNormal:str, dicas=True):
        '''
        Para se iniciar uma partida o usuário deverá informar uma palavra.
        Depois é gerado um Anagrama.
        Em seguida, a quantidade de tentativas é medida com a seguinte fórmula:
        (X + 4)//2   onde X equivale ao tamanho da palavra
        '''
            
        self.__palavraNormal=palavraNormal
        self.__anagrama= Anagrama(self.__palavraNormal)
        self.__jogadasPossiveis= (len(self.__anagrama.palavraEmbaralhada)+4)//2
        self.__dicas=dicas
    #== == == == Propertys e setters
    @property
    def jogadasPossiveis(self):
        return self.__jogadasPossiveis
    
    @property
    def anagrama(self):
        return self.__anagrama.palavraEmbaralhada

    @property 
    def palavraNormal(self):
        return self.__palavraNormal
    
    @property 
    def dicas(self):
        return self.__dicas
    
    #== == == == Métodos relacionados no palpite

    def checarPalpite(self,palpite:str):
        '''Este é o método que verifica e resolve o resultado do palpite do usuário'''
        self.palpite=palpite
        return self.__checarVitoria(self.palpite)
             
        #elif not(self.__dicas): return  # caso o usuário não queira dicas

        #return self.__sortearDica() # se não, ele retornará uma dica
            
    def __checarVitoria(self,palpite:str)->bool:
        '''Checa se o usuário acertou a palavra embaralhada'''
        if palpite == self.__anagrama.palavraEmbaralhada: return True # o usuário adivinhou!
        else: return False # O usuário errou!
    
    #== == == == Dicas    
    def sortearDica(self):
        '''Retorna uma dica aleatória:
         1: Informa as primeiras letras do Anagrama
         2: Informa a posição de uma ou mais vogais
         3: Informa se o usuário acertou a posição das letras no seu palpite 
        '''
        
        Numero=random.randint(1,3) # método para escolher as dicas de maneira aletória
        dica=''
        if Numero==1:
            dica=f'Dica Nº{Numero}, as primeiras letras da palavra embaralhada são:\n'
            dica+=self.PrimeirasLetras()

        elif Numero==2:
            dica=f'Dica Nº{Numero}, há uma vogal na seguinte posição:\n'
            dica+=self.revelarVogalPosicao()
        
        elif Numero==3:
            dica=f'Dica Nº{Numero}, no seu palpite, você acertou as seguintes posições:\n'
            dica+=self.LetraPosicao()
        
        return dica
            

    #------Dica dada através das primeiras letras    
    def PrimeirasLetras(self):
        PrimeirasLetras= (self.__anagrama.__len__() +1 ) //3
        return f"{self.__anagrama.palavraEmbaralhada[:PrimeirasLetras]}"

    #------Dica dada através da posição da vogal   
    def revelarVogalPosicao(self)->str:
        '''função que irá mostrar a lista das vogais do anagrama desta partida. Detalhe: A lista de vogais do anagrama irá aumentar cada vez  que esta função for chamada e caso não haja mais vogais para revelar, ela retorna apenas a lista'''
        
        antigaQuantidadeVogaisReveladas=len(self.__VogaisReveladasLista)
        
        vogal=self.__anagrama.verificarVogalPosicao(len(self.__VogaisReveladasLista))
            
        if vogal[0]!=None: #Vê se foi retornado uma vogal e a sua posição 
            self.__VogaisReveladasLista.append(vogal)
        
        
        if (len(self.__VogaisReveladasLista) - antigaQuantidadeVogaisReveladas): #vê se ocorreu alguma alteração na lista de vogais
            self.__VogaisReveladasString= self.__revelarVogalPosicao(self.__VogaisReveladasLista) #caso tenha sido adicionado uma nova vogal
        
        return self.__VogaisReveladasString
                  
    
    def __revelarVogalPosicao(self,listaVogal:list)->str:
        '''Este método cria uma string contendo todas as posições '''
        string=''
        if len(listaVogal)==0:
            return string
        string+= f'|Vogal: {listaVogal[0][0]:^5} Posição: {listaVogal[0][1]:^5}| \n'
        
        return  string + self.__revelarVogalPosicao(listaVogal[1:])
    
    
    #------Dica Através da posiçao de uma letra
    def LetraPosicao(self)->str:
        '''Este método irá checar se a posição de algumas letras inseridas no palpite do usuário é semelhante ao que está no Anagrama.
        Detalhe: Uma posição pode ser checada mais de uma vez, ou seja, este método não garante a unicidade.
        '''
        
        verificacao=''
        verificarVezes=(len(self.palpite)+1) // 2 #Formúla para verificar de maneira justa as letras do palpite do usuário
        anagrama=self.__anagrama.palavraEmbaralhada
        
        for i in range(verificarVezes): #irá fazer o cheque N vezes
            
            posicao=random.randint(0,len(anagrama))
            
            if self.palpite[posicao]== anagrama[posicao]:
                verificacao+=f'[Certo] Letra: {self.palpite[posicao]}. Na posição: {posicao + 1} \n'
            else:
                verificacao+=f'[Errado] Letra: {self.palpite[posicao]}. Na posição: {posicao + 1} \n'
        
        return verificacao