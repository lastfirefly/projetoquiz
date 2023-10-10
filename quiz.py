# Importar as bibliotecas necessárias:
import pandas as pd
import numpy as np
import datetime as dt
from time import sleep as sl
# Dicionários de perguntas e respostas:
# Perguntas
questoes =   {"Questão 1": "Constelação são os desenhos que conseguimos ver se imaginarmos uma linha ligando as estrelas",
            "Questão 2": "As estações do ano são definidas por conta da inclinação da Terra com relação ao Sol",
            "Questão 3": "Existe lugares no planeta Terra que ficam 6 meses sem luz Solar",
            "Questão 4": "Buracos negros não são estrelas"
}
# Opções de resposta
respostas = {    "1": "Sim/Verdadeiro",
                "2": "Não/Falso",
                "3": "Não sei responder"
}
#classes para organizar as partes do código:
class Menu:
    # Definir as variáveis a serem utilizadas
    idade = int(input("Sua idade: "))
    genero = int(input("Com qual gênero você se identifica?\n[1] - Homem Cis\n[2] - Mulher Cis\n[3] - Homem Trans\n[4] - Mulher Trans\n[5] - Não-Binário\n"))
    contagem = 0
    
    # Para iniciar o questionário, será solicitado ao usuário que informe a sua idade e gênero.
    def __init__(self, idade, genero):
        self.idade = idade
        self.genero = genero
    
    # Menu inicial
    def start(self, idade, genero):
    #apresentar o questioário
        print("Olá!\nHoje vamos testar seu conhecimento básico sobre Astronomia com quatro perguntinhas!")
        sl(2)
    #pedir informações da pessoa
        print("Para que possamos começar, vou te explicar as regras.\nI) Responda as perguntas apenas com o teclado numérico.\
              \nII) Caso não queira mais fazer o questionário, responda com '00' quando a idade for perguntada!")
        sl(1)
    
    # Loop para percorrer pergutas e oferecer opções de respostas
    for pk, pv in questoes.items():
        print(f'\n{pk}: {pv}\n')
        for rk, rv in respostas.items():
            print(f"{rk}: {rv}\n")
        respostaUsuario = input("Sua resposta: ")
        print("*"*50)




contagem = 0



# class Questionario:
#     pass


# class Respostas:
#     pass
