# importa a função sleep
from time import sleep as sl
# início da execução do código
if __name__ == "__main__":
    # imprime uma apresentação para o usuário
    print("\nOlá! Gostaria de participar de uma pesquisa sobre o uso das redes sociais?\n")
    # print("\nOlá!\nHoje vamos testar seu conhecimento básico sobre Astronomia com quatro perguntinhas!")
    sl(2)
    # exibe uma explicação sobre o funcionamento da pesquisa
    print("\nPara que possamos começar, vou te explicar as regras.\nI) Responda as perguntas apenas com o teclado numérico.\
              \nII) Caso não queira mais fazer o questionário, responda com '00' quando a idade for perguntada!\n")
    sl(1)
# chama o módulo quiz, onde está a pesquisa em si
import quiz as qz