 

#O intuito do projeto é criar um novo alfabeto com base no alfabeto em português
#O usário decide quantas e quais serão as letras presentes no seu novo alfabeto
#e dirá qual será o seu correspondente no alfabeto em português. 
#a partir disso da para desenvolver um sistema degerenciamento de senhas


import pandas as pd
import random 

Alfabeto = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N", 
            "O", "P", "Q", "R", "S", "T", "U", 
            "V", "W", "X", "Y", "Z"]

AlfabetoCP = ["A", "B", "C", "D", "E", "F", "G",
              "H", "I", "J", "K", "L", "M", "N",
              "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", ".", ",",
              "!", "?", ";", ":", "-", "'", "(",
              ")", "[", "]", "{", "}", "<", ">",
              "/", "|", "@", "#", "$", "%", "^",
              "&", "*", "_", "+", "="]

Pontuacao = ["!", "?", ";", ":", "-", "'", "(",
              ")", "[", "]", "{", "}", "<", ">",
              "/", "|", "@", "#", "$", "%", "^",
              "&", "*", "_", "+", "=",".", ","]

NovoAlfabeto = []
def Funcao1():
    i = 0
    while(i<len(Alfabeto)):
        print(f"Qual caractere deseja que represente a letra {Alfabeto[i]}\n")
        letra = input().upper()
        if (letra not in NovoAlfabeto):
            NovoAlfabeto.append(letra)
            print(f"Caracteres já utilizados {NovoAlfabeto}\n")
            i+=1
        else:
            print(f"O caractere {letra} já foi utilizado\n")
    return NovoAlfabeto

def Funcao2():
    NovoAlfabeto = Alfabeto[:]
    random.shuffle(NovoAlfabeto)
    return NovoAlfabeto

def Funcao3():
    i = 0
    while(i<len(AlfabetoCP)):
        print(f"Qual caractere deseja que represente o caractere {AlfabetoCP[i]}\n")
        letra = input().upper()
        if (letra not in NovoAlfabeto):
            NovoAlfabeto.append(letra)
            print(f"Caracteres já utilizados {NovoAlfabeto}\n")
            i+=1
        else:
            print(f"O caractere {letra} já foi utilizado\n")
    return NovoAlfabeto

def Funcao4():
    NovoAlfabeto = AlfabetoCP[:]
    random.shuffle(NovoAlfabeto)
    return NovoAlfabeto

def Funcao5():
    NovoAlfabeto = Pontuacao[:]
    random.shuffle(NovoAlfabeto)
    del NovoAlfabeto[0]
    del NovoAlfabeto[0]
    return NovoAlfabeto

y = 0
while(y == 0):
    print("Escolha uma opção:")
    print("(1) - Criar Alfabeto manulmente (Sem pontuação)")
    print("(2) - Criar Alfabeto automaticamente (Sem pontuação)")
    print("(3) - Criar Alfabeto manualmente (Com pontuação)")
    print("(4) - Criar Alfabeto automaticamente (Com pontuação)")
    print("(5) - Criar Alfabeto automaticamente apenas com simbolos de pontuação")
    opcao = int(input())

    if  (opcao == 1):
        NovoAlfabeto = Funcao1()
        y = 1
    elif  (opcao == 2):
        NovoAlfabeto = Funcao2()
        y = 1
    elif (opcao == 3):
        NovoAlfabeto = Funcao3()
        y = 1
    elif  (opcao == 4):
        NovoAlfabeto = Funcao4()
        y = 1
    elif  (opcao == 5):
        NovoAlfabeto = Funcao5()
        y = 1
    else:
        print("Opção Inválida")

if (opcao == 1 or opcao == 2 or opcao == 5):
    Dicionario = { 'Alfabeto': Alfabeto,
                   'Codificação': NovoAlfabeto
                 }     
else:
    Dicionario = { 'Alfabeto': AlfabetoCP,
                   'Codificação': NovoAlfabeto
                 }

Decode = pd.DataFrame(Dicionario)
print(Decode)

x = 1
while (x == 1):
    print("Escolha uma opção:")
    print("(1) - Importar Dataframe no formato Exel")
    print("(2) - Importar Dataframe no formato CSV")
    print("(3) - Importar Dataframe no formato JSON")
    print("(4) - Encerrar Programa")
    opcao2 = int(input())
    
    if (opcao2 == 1):
        Nome = input("Informe o nome do arquivo:\n")
        Nome += '.xlsx'
        Decode.to_excel(Nome)
        print('Operação finalizada com Sucesso')
        x=2
    elif (opcao2 == 2):
        Nome = input("Informe o nome do arquivo:\n")
        Nome += '.csv'
        Decode.to_csv(Nome)
        print('Operação finalizada com Sucesso')
        x=2
    elif (opcao2 == 3):
        Nome = input("Informe o nome do arquivo:\n")
        Nome += '.json'
        Decode.to_json(Nome)
        print('Operação finalizada com Sucesso')
        x=2
    elif  (opcao2 == 4):
        x=2
