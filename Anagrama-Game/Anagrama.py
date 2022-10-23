import random

class AnagramaException(Exception):
    #== == == == Errors codes: 
    #== == == 2: User inseted a Number
    def __init__(self, msg:str, ErrorCode:int) -> None:
        super().__init__(f'{ErrorCode}: '+ msg.upper())
        

class Anagrama:
    
    def __init__(self,palavraNormal:str) -> None:
        self.__palavraEmbaralhada=self.__gerarAnagrama(palavraNormal.lower())
        
    
    def gerarAnagrama(self,palavra)->str: # Método ultilizado para embaralhar a palavra
        palavraLista= list(palavra) 
        random.shuffle(palavraLista)
        for i in range( len(palavraLista)):
            
            if palavraLista[i] in ' -,':
                palavraLista[i]== ''
            elif palavraLista[i] in [0-9]:
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