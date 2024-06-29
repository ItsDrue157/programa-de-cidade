import os
import time
from dados import data

def App():
    #Transforma um dicionario em uma lista
    lista_de_cidades = [d["list"] for d in data]
    
    
    
    def Exibir_menu():
        Limpar_terminal()
        escolha = input('''
𝙷𝚎𝚕𝚕𝚘! 𝚂𝙴𝙹𝙰 - 𝙱𝙴𝙼𝚅𝙸𝙽𝙳𝙾

Digite 1 para visualizar a lista
Digite 2 para verificar se a sua cidade está na lista: ''')

        # Processamento da escolha
        if escolha == '1':
            Mostrar_cidades()
        elif escolha == '2':
            Verificar_cidade_na_lista()  # Passa data como argumento
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            Exibir_menu()  # Retorna ao menu se a opção for inválida
    
    def Mostrar_cidades():
        print("Lista de dados:")
        for cidades in data:
            print(cidades)
        
        time.sleep(5)
        voltar_ao_menu = input('Deseja voltar ao menu? s/n ')
        if voltar_ao_menu.lower() == 's':
            Voltar_ao_menu()
        elif voltar_ao_menu.lower() == 'n':
            exit()
        else:
            print("Opção inválida.")
            Mostrar_cidades()
    
    def Verificar_cidade_na_lista():    
        cidade_digitada = input("Digite o nome da cidade: ")
        if cidade_digitada in lista_de_cidades:
            print(f'A cidade {cidade_digitada} está na lista.')
        else:
            print(f'A cidade {cidade_digitada} não está na lista.')
        
                
                
                
    def Voltar_ao_menu():
        try:
        
            escolha_voltar_menu = input("Deseja voltar ao menu? s/n ")
            match escolha_voltar_menu:
                case 's':
                    print("Voltando ao menu...")
                    time.sleep(2)
                    Exibir_menu()
                case 'n':
                    exit()
        except KeyError:
            print("Opcao invalida")
            Voltar_ao_menu()
                
                
        

    def Limpar_terminal():
        os.system('cls')

    # Início do programa
    Exibir_menu()

# Executa o aplicativo
App()