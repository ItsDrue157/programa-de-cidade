import os
import time 
global pergunta
global cidades
global escolha

cidades = [ 'Belo Horizonte', 'Rio de Janeiro', 'Santa Catarina', "Salvador"]


def App():
    def Exibir_menu():
            Limpar_terminal()
            pergunta = input('''
            𝙷𝚎𝚕𝚕𝚘! 𝚂𝙴𝙹𝙰 -𝙱𝙴𝙼𝚅𝙸𝙽𝙳𝙾
            
            Digite 1 para visualizar a lista
            
            Digite 2 para verificar se a sua cidade esta na lista: ''')
            pergunta == escolha
        
        
    match escolha:
        case '1':
                print(f' A lista de cidades eh: {cidades} ')
        case '2':
                Verificar_cidade_na_lista()
            

                
    def Verificar_cidade_na_lista():
            cidade_digitada = input("Digite o nome da cidade ")
            if cidade_digitada in cidades == True:
                print(f'A Sua {cidade_digitada}, esta na lista ')
                time.sleep(5)
                Voltar_ao_menu()

    def Voltar_ao_menu():
            print("Voltando ao menu...")
            Exibir_menu()
                
    def Limpar_terminal():
            os.system('cls')
    
App()

        


