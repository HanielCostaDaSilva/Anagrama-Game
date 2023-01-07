import time
from Partida import Partida
import os 

#== == == == Métodos
def MostrarDicionario(dicionario:dict,dictionaryKeys):
    '''Recebe um dicionário e um array com chaves para poder mostrar na tela as chaves e os seus valores'''
    for i in range(len(dictionaryKeys)):
        print(f'\n[{dictionaryKeys[i]:^10}] => {dicionario.get(dictionaryKeys[i]):^10}')

def clearConsole():
    '''Método para Limpar o terminal'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#== == == == Variáveis
sep1='=-='*30
sep2='=-'*15
sep3='-='*15
sep4='<3'*30
sep5='</3'*30
cursor='=>'

flag=True
partidasJogadas=0
vitoriaFlag=False

#== == -- -- Introducao
print(f"{sep2} Bem vindo ao Anagrama {sep3} \n{sep1 :^5}\nO jogo consiste em você escrever uma palavra e em seguida tentar adivinhar qual o anagrama formado a partir dela!")
input(cursor)


#== == Inicio da Partida
while flag:
    #== O Usuário digitará uma palavra
    PalavraNormal=str.lower(input(f'digite uma palavra: (mínimo de 4 letras) \n{cursor} ')) #o programa recebe a palavra do Usuário
    print(sep1)

    while len(PalavraNormal)<4: #Caso possua menos que 4 letras, o programa irá exigir uma outra palava com uma quantidade maior 

        PalavraNormal=str.lower(input(f'Por favor digite uma outra palavra com no mínimo 4 letras \n{cursor} '))
        print(sep1)
        
    #== -- -- -- È feito algumas implementações antes do incio da Partida
    partidasJogadas+=1
    
    desejaDica=input(f'Deseja receber dicas nesta partida? (S/N) \n{cursor}') #Verifica se usuário gostaria de receber dicas
    
    partida=Partida(PalavraNormal, desejaDica.upper()=='S') # a partida é criada
    
    palpitesAnteriores=[]

    
    print('Digite "N" caso não queira iniciar a partida\n')
    jogar=input(f"{sep1}\nVAMOS COMEÇAR A {partidasJogadas}ª PARTIDA!\n {cursor}")
    if jogar.upper()=='N':
        break
    #== == -- -- É neste laço em que o jogo acontece
     
    for i in range(partida.jogadasPossiveis):
        
        palpite='' # O palpite é uma lista para ficar mais fácil para visualização e análise das letras informadas pelo usuário
        LetraPalpiteNum=0 # Para informar qual o número da letra que o usuário deve informar
        palavraMostrada=list(partida.palavraNormal)
        palavraDigitada=['_ ' for i in range(len(palavraMostrada))]
        
        #== == -- -- Recebendo o palpite do usuário    
        while len(palpite) < len(partida.anagrama): # Enquanto o palpite não tiver a mesma quantidade de levras que a palavra embaralhada
            clearConsole()
        
            print(f'{sep1 :^5}\n Você possui: {partida.jogadasPossiveis - i} tentativas! \n{sep1 :^5}\n {i+1}ª Rodada: ')
            
            print(f'{sep2} Digite 999 para apagar o seu palpite{sep3}')
            print(f'{sep1} \n a palavra original é: {partida.palavraNormal}\n{sep1}')
            
            print(f'{sep2} Palpites Anteriores: {" ".join(palpitesAnteriores):^5}{sep3}')
            
            print(f'{sep2}{" ".join(palavraDigitada):^5}{sep3}')
            print(f'você pode digitar as seguintes letras: {" ".join(palavraMostrada) }')
            
            letra= str.lower(input(f"\nDigite a {LetraPalpiteNum+1}ª letra do seu palpite: \n {cursor}")) #variável que armazena a letra dada pelo usuário 
            
            if letra=='999':
                palavraMostrada=list(partida.palavraNormal)
                palavraDigitada=['_ ' for i in range(len(palavraMostrada))]
                palpite=''
                LetraPalpiteNum=0
                time.sleep(1)
            
            elif len(letra)>1:
                time.sleep(1)
                print('Digite apenas um caracter.')
            
            elif letra not in palavraMostrada:
                print(f"{sep2:^5}Esta letra, ou já foi digitada ou não está presente na palavra embaralhada!{sep3:^5}")
                time.sleep(1)
                input(cursor)
                
        
            else:
                palpite+=letra
                palavraDigitada[LetraPalpiteNum]=letra
                palavraMostrada.remove(letra)
                LetraPalpiteNum+=1
            
        palpitesAnteriores.append(palpite)
        validacao= partida.checarPalpite(palpite) # verifica se o usuário acertou a palavra embaralhada
        
        if validacao:
            vitoriaFlag=not(vitoriaFlag)
            break
        else:
            clearConsole()
            print(f'{sep1}\n O seu palpite:{palpite}, está errado! \n{sep1} ')
            #time.sleep(2)
            
            if partida.dicas:
                print(f"{sep1}\n Lá vem uma dica.....\n{partida.sortearDica()}\n{sep1}")
                input(f'Aperte "Enter" para continuar...\n{cursor}')
    
    if vitoriaFlag:
        print(f"{sep4}\nParabéns! Você acertou! \n{sep4}")
    
    else:
        print(f"{sep5}\nSinto muito, não foi dessa vez...\nA palavra embaralhada era:{partida.anagrama}\n{sep5}")
    
    jogarDenovo=input(f'Deseja jogar de novo?(S/N) \n {cursor}')
    
    if jogarDenovo.upper()!='S':
        flag=False
    
    clearConsole()

print(f'{sep4}\nFim De Jogo! \n Obrigado por ter jogado :) \n{sep4}')