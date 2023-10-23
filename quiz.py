# Importar as bibliotecas necessárias:

import pandas as pd
import numpy as np
import datetime 
from datetime import datetime as dt
from time import sleep as sl

#Contagem para definir quantas pessoas responderam o teste
contagem = 0

# Dicionários de perguntas e respostas:
# Perguntas


questoes =   {
    "Questão 1": "Constelação são os desenhos que conseguimos ver se imaginarmos uma linha ligando as estrelas",
    "Questão 2": "As estações do ano são definidas por conta da inclinação da Terra com relação ao Sol",
    "Questão 3": "Existe lugares no planeta Terra que ficam 6 meses sem luz Solar",
    "Questão 4": "Buracos negros não são estrelas"
}

# Opções de resposta
respostas = {
    "1": "Sim/Verdadeiro",
    "2": "Não/Falso",
    "3": "Não sei responder"
}

# Gêneros
genero_alternativas = { 
    "1" : "Homem Cis",
    "2" : "Mulher Cis",
    "3" : "Homem Trans",
    "4" : "Mulher Trans",
    "5" : "Não Binário",
}


# Dados dos testers

tester = {

}

#classes para organizar as partes do código:
class Menu:

    # Para iniciar o questionário, será solicitado ao usuário que informe a sua idade e gênero.
    def __init__(self, idade, genero):
        pass
        #self.idade = idade
        #self.genero = genero
    

    # Menu inicial

 
    while True:

        dadosTester = [] 

        idade = input("Sua idade: ")
                
        print("\n")
        sl(1)

        if idade == "00":
            print ("\nObrigado por participar do teste!\n")
            break
        try:
            idade = int(idade)

            if idade < 1 or idade > 99:
                print('\nIdade inválida. A idade deve estar entre 1 e 99.\n')
                continue  # Volta ao início do loop para pedir a idade novamente

            else:
                dadosTester.append(idade) # adiciona a idade já convertida para inteiro
                contagem += 1

                #Imprimir opções de gênero
                
                for gk, gv in genero_alternativas.items():
                    print(f'{gk}: {gv}')
                genero = int(input("\nCom qual gênero você se identifica? \n"))
                dadosTester.append(genero)

                        # Anotar a hora do começo das respostas para que seja registrada
                horaResposta = dt.now()
                        # horaResposta.strftime('%d/%m/%Y')
                dadosTester.append(horaResposta)


                for pk, pv in questoes.items():
                    while True:
                        print(f'\n{pk}: {pv}\n')
                        sl(1)

                        for rk, rv in respostas.items():
                            print(f"{rk}: {rv}\n")
                            sl(1)

                        respostaUsuario = input("Sua resposta: ")
                        if not respostaUsuario in respostas:
                            print("\n")
                            print("*"*50)
                            print(f'\nOpção inválida. Tente novamente.\n')
                            print("*"*50)
                        else:
                            dadosTester.append(respostaUsuario)
                            print("\n")
                            print("*"*50)
                            break
                        
        except ValueError:
            print('\nResposta inválida! Digite apenas números inteiros.')

            dadosTester.append(idade)
            print(dadosTester)

            # Atribuir os dados ao dicionário de dados dos testers
        tester[contagem] = dadosTester

        print(tester)

    print(pd.DataFrame(tester.values(), index=tester.keys(), columns=['idade', 'gênero', 'data', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4']))
