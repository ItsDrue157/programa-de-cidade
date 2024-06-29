import os
import time 

cidades = ['Belo Horizonte', 'Rio de Janeiro', 'Santa Catarina', 'Salvador']

def App():
    def Exibir_menu():
        Limpar_terminal()
        escolha = input('''
𝙷𝚎𝚕𝚕𝚘! 𝚂𝙴𝙹𝙰 - 𝙱𝙴𝙼𝚅𝙸𝙽𝙳𝙾

Digite 1 para visualizar a lista
Digite 2 para verificar se a sua cidade está na lista: ''')

        # Processamento da escolha
        if escolha == '1':
            print(f'A lista de cidades é: {cidades}')
        elif escolha == '2':
            Verificar_cidade_na_lista()
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            Exibir_menu()  # Retorna ao menu se a opção for inválida

    def Verificar_cidade_na_lista():
        cidade_digitada = input("Digite o nome da cidade: ")
        if cidade_digitada in cidades:
            print(f'A cidade {cidade_digitada} está na lista.')
        else:
            print(f'A cidade {cidade_digitada} não está na lista.')
        time.sleep(3)
        Voltar_ao_menu()

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