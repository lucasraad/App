import os #biblioteca OS

restaurantes = [{'nome':'Mr.House', 'categoria':'hambugueria', 'ativo':False},
               {'nome':'Yoshin', 'categoria':'sushi', 'ativo':True}, 
               {'nome':'Bar da tita', 'categoria':'bar', 'ativo':True}] # lista[], biblioteca{}

def exibir_nome_do_programa():
     print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def exibir_opcoes():
     print('1. Cadastrar restaurante')
     print('2. Listar restaurante')
     print('3. Ativar restaurante')
     print('4. Sair\n')

def finalizar_app():
     exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menur_principal():
     input('\nDigite uma tecla para voltar ao menur principal ')
     main()

def opcao_invalida():
     print('Opção inválida!\n')
     voltar_ao_menur_principal()

def exibir_subtitulo(texto):
     os.system('cls')
     print(texto)
     print()


def cadastrar_novo_restaurante():
     exibir_subtitulo('Cadasto de novos restaurantes\n')
     nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
     
     voltar_ao_menur_principal()

def listar_restaurantes():
     exibir_subtitulo('Listando os restaurantes\n')

     # para cada restaurante na lista restaurantesss:
     for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = restaurante['ativo']
          print(f'- {nome_restaurante} | {categoria} | {ativo}')

     voltar_ao_menur_principal()



def escolher_opcao():
     try:
         opcao_escolhida = int(input('Escolhe uma opção: '))
          # opcao_escolhida = int(opcao_escolhida)
          
     #se  opcao_escolhida for igual a 1
         if opcao_escolhida == 1: 
              cadastrar_novo_restaurante()
         elif opcao_escolhida == 2:
              listar_restaurantes()
         elif opcao_escolhida == 3:
             print('Ativar restaurantes')
         elif opcao_escolhida == 4:
            finalizar_app()
         else:
              opcao_invalida()                       
     except:
          opcao_invalida()


def main():
     os.system('cls') #limpa tela
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()

if __name__== '__main__':
     main()