import random
from unicodedata import normalize

class AnagramaException(Exception):

    def __init__(self, msg:str, ErrorCode:int) -> None:
        '''
        1: User inserted a blank string
        2: User inseted a Number
        3: Invalid Vogal Position
        '''
        super().__init__(f'{ErrorCode}: '+ msg.upper())
        

class Anagrama:
    
    __vogalPosicao=[]

    def __init__(self,palavraNormal:str) -> None:
        ''' recebe uma palavra normal e em seguida a embaralha.'''
        if len(palavraNormal)==0:
            raise AnagramaException('Erro! Não foi inserido uma palavra!')
        
        palavraSemAcento = normalize('NFKD', palavraNormal).encode('ASCII','ignore').decode('ASCII')
        
        self.__palavraEmbaralhada=self.__gerarAnagrama(palavraSemAcento.lower())
        
        self.criarListaVogais()
    
    def __gerarAnagrama(self,palavra)->str: # Método ultilizado para embaralhar a palavra
        '''Este método cria um Anagrama. Ele remove os seguintes caracteres: " ", "-" e ",". 
        Caso encontre um número, retorna um erro.  '''
        
        palavraLista= list(palavra)
        random.shuffle(palavraLista)
        
        for i in range( len(palavraLista)):
            
            if palavraLista[i] in ' -,':
                palavraLista[i]== ''
            elif palavraLista[i] in [0,1,2,3,4,5,6,7,8,9]:
                raise AnagramaException('Erro! não é permitido Números! ',2)
            
        anagrama = ''.join(palavraLista)
        
        return anagrama

    @property
    def palavraEmbaralhada(self):
        return self.__palavraEmbaralhada
    
    def __str__(self) -> str:
        return self.__palavraEmbaralhada
    
    def __len__(self):
        return len(self.palavraEmbaralhada)
    
    def criarListaVogais(self):
        '''Este método adiciona a vogal e a sua posição na lista de ocorrencias'''
        self.__criarListaVogais(self.__vogalPosicao, self.__palavraEmbaralhada, 0)
        random.shuffle(self.__vogalPosicao)
    
    
    def __criarListaVogais(self,listaVogal:list, palavra:str, posicao:int):

        if len(palavra) == posicao: #caso a posição ultrapasse o tamanho da palavra
            return
        
        if palavra[posicao] in 'aeiou': #caso naquela posicão haja uma vogal
            listaVogal.append([ palavra[posicao], posicao + 1]) #adiciona a vogal e a sua posicao. Ex:Avestruz, [[a, 1],[e, 3], [u, 7]]

        self.__criarListaVogais(listaVogal, palavra, posicao+1)
    
    def verificarVogalPosicao(self,posicao:int)->list:
        '''Retorna uma lista contendo a vogal e a sua atual posição, caso não encontre, retorna uma lista contendo None'''
        try:
            return self.__vogalPosicao[posicao]
        except IndexError:
            return [None]