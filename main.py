import os
import time
import pandas as pd

lista_arquivo = [] 
caminho_da_lista = 'dados.csv'


def App():
    def Exibir_menu():
        
        Limpar_terminal()
        escolha = input('''
𝙷𝚎𝚕𝚕𝚘! 𝚂𝙴𝙹𝙰 - 𝙱𝙴𝙼𝚅𝙸𝙽𝙳𝙾

Digite 1 para visualizar a lista
Digite 2 para verificar se a sua cidade está na lista: ''')



        # Processamento da escolha
        if escolha == '1':
            Mostrar_cidades()
            time.sleep(10)
            Exibir_menu()
           
        elif escolha == '2':
            Verificar_cidade_na_lista()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            Exibir_menu()  # Retorna ao menu se a opção for inválida
    
    
    def Mostrar_cidades():
        #pd.read_csv = vai ser como o arquivo esta salvo o r'' eh para ler caminos
        lista = pd.set_option('display.max_rows', 350)
        lista = pd.read_csv("dados.csv")
#             transforma a tabela em uma tring q pode ser mostrada.
        print(lista)
        time.sleep(5)
        voltar_ao_menu = input('Deseja voltar ao menu? s/n ')
        match voltar_ao_menu:
            case 's':
                Voltar_ao_menu()
            case 'n':
                exit()
    

    def Verificar_cidade_na_lista():
        cidade_digitada = input("Digite o nome da cidade: ")
        if cidade_digitada in lista_arquivo:
            print(f'A cidade {cidade_digitada} está na lista.')
        else:
            print(f'A cidade {cidade_digitada} não está na lista.')
        time.sleep(3)
        voltar_ao_menu = input('Deseja voltar ao menu? s/n ')
        match voltar_ao_menu:
            case 's':
                Voltar_ao_menu()
            case 'n':
                exit()

    def Voltar_ao_menu():
        print("Voltando ao menu...")
        time.sleep(2)
        Exibir_menu()

    def Limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa terminal dependendo do sistema

    # Início do programa
    Exibir_menu()

# Executa o aplicativo
App()