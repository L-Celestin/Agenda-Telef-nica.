# Campo Principal:
#Gefferson Resende Santos
#George Sergio Soares De Oliveira
#Leonardo Antonio Celestino Meneses Sobral
#Lorena De Jesus Almeida
#Thalita Dantas Araújo
lc = {'Gefferson Resende Santos': {'NOME': 'Gefferson Resende Santos', 'TELEFONE': '', 'EMAIL': '', 'ENDEREÇO': '', 'CPF': '', 'MATRÍCULA': '202002004428', 'NACIONALIDADE': ''}, 'Geise Kelly Conceição Santos': {'NOME': 'Geise Kelly Conceição Santos', 'TELEFONE': '', 'EMAIL': '', 'ENDEREÇO': '', 'CPF': '', 'MATRÍCULA': '202002520361', 'NACIONALIDADE': ''}, 'George Sergio Soares De Oliveira': {'NOME': 'George Sergio Soares De Oliveira', 'TELEFONE': '', 'EMAIL': '', 'ENDEREÇO': '', 'CPF': '', 'MATRÍCULA': '202008199468', 'NACIONALIDADE': ''}, 'Leonardo Antonio Celestino Meneses Sobral': {'NOME': 'Leonardo Antonio Celestino Meneses Sobral', 'TELEFONE': '', 'EMAIL': '', 'ENDEREÇO': '', 'CPF': '', 'MATRÍCULA': '202001338391', 'NACIONALIDADE': ''}, 'Lorena De Jesus Almeida': {'NOME': 'Lorena De Jesus Almeida', 'TELEFONE': '', 'EMAIL': '', 'ENDEREÇO': '', 'CPF': '', 'MATRÍCULA': '202003045012', 'NACIONALIDADE': ''}, 'Thalita Dantas Araújo': {'NOME': 'Thalita Dantas Araújo', 'TELEFONE': '', 'EMAIL': '', 'ENDEREÇO': '', 'CPF': '', 'MATRÍCULA': '202003045012', 'NACIONALIDADE': ''}}
# 'lc' foi escolhida como dicionário que vai guardar todos os contatos, a lógica da sua nomeação segue o nome "lista de contatos".
# Definição de funções:

def Incluir(campo, inc):
  contato = lc[nome]
  contato[campo] = inc
def Continuar_Voltar(s = 1):
  print('(1) Continuar. \n(2) Voltar. \n')
  s = int(input("Selecione uma opção: "))
  return s
  # A Letra 's' foi escolhida pra representar a palavra 'seleção'.
def Bordas():
  print()
  print("}----------/ ----------/ ----------/ ----------/ ----------{")
  print()
# Definição de Variáveis:
lista_p_alterar = ['EMAIL', 'ENDEREÇO', 'CPF', 'MATRÍCULA', 'NACIONALIDADE', 'TELEFONE']
# 'le' foi criada como 'lista de escolha', com o intuito de separar os procedimentos de alteração de nome de usuário e alteração de outros campos, ela serve pra escolher uma chave do dicionário 'lc' (menos 'NOME') que possua os mesmos caracteres de uma das strings da lista.
n = 0
# Algorítimo:
print('\nOlá, bem vindo a sua agenda .PY \n')
while n != 6:
    Bordas()
    print("(1) novo contato. \n(2) buscar contato. \n(3) alterar contato. \n(4) copiar. \n(5) deletar. \n(6) sair. \n")
    n = int(input("Escolha uma das opções acima: "))
    Bordas()
    if n == 1:
       s1 = Continuar_Voltar()
       if s1 == 1:
         Bordas()
         nome = input(">> Insira o nome do contato: ").strip().lower().title()
         fone = input(">> Insira o telefone do contato: ").strip()
         lc[nome] = {"NOME": nome, "TELEFONE": fone}
         Bordas()
         print("Desejas adicionar mais informações? \n \n(1) Sim. \n(2) Não. \n")
         c1 = int(input("Selecione uma das opções: "))
         # 'c1' foi escolhida como 'condicional 1', mesma lógica para os enesimos 'c's
         Bordas()
         if c1 == 1:
           print('< Caso não queira adicionar informações apenas aperte enter > \n')
           email = input(">> Insira o endereço de email: ") .strip().lower()
           Incluir('EMAIL', email)
           end = input(">> Insira o endereço residencial: ").strip().lower().title()
           Incluir('ENDEREÇO', end)
           cpf = input(">> Insira o cpf: ").strip()
           Incluir('CPF', cpf)
           matr = input(">> Insira a matrícula: ").strip()
           Incluir('MATRÍCULA', matr)
           naci = input(">> Insira sua nacionalidade: ").strip().lower()
           Incluir('NACIONALIDADE', naci)
           print(lc)
         else:
           print("OK!")
       else:
         Bordas()
         print("OK!") 
    if n == 2:
       s2 = Continuar_Voltar()
       if s2 == 1: 
         Bordas()
         nome_do_contato = input("Por qual contato deseja buscar?: ").lower().title().strip()
         if nome_do_contato in lc:
           contato = lc[nome_do_contato]
           Bordas()
           print('< Aqui estão as informações do contato buscado: > \n')
           for key, value in contato.items():
             print('{}: {}'.format(key, value))
         else:
             print("< Contato", nome_do_contato,"não localizado, tente novamente >")
       else:
         Bordas()
         print("OK!")      
    if n == 3:
     s4 = Continuar_Voltar()
     Bordas()
     if s4 == 1: 
       contato_para_alterar = input(">> Qual contato deseja alterar?: ").lower().title().strip()
       if contato_para_alterar in lc:
         camp = input(">> Que campo deseja alterar?: ").upper()
         if camp in lc[contato_para_alterar]: 
           if camp == 'NOME':
             import copy
             alterar = copy.deepcopy(lc[contato_para_alterar])
             mud = input(">> Insira as mudanças a serem feitas: ").strip().lower().title()
             alterar[camp] = mud
             del lc[contato_para_alterar]
             lc[mud] = alterar
             print("\n< Contato {} teve seu nome alterado para: {}>".format(contato_para_alterar, mud))
             Bordas()
             print("Dejesa visualizar as alterações? \n(1) Sim. \n(2) Não. \n")
             c4 = int(input("Escolha uma das opções a cima: "))
             if c4 == 1:
               print(lc[mud])
             else:
               print("Ok!")
           if camp in lista_p_alterar:
             import copy
             alterar = copy.deepcopy(lc[contato_para_alterar])
             mud = input(">> Insira as mudanças a serem feitas: ")
             alterar[camp] = mud
             lc[contato_para_alterar] = alterar
             print("\n< O contato foi alterado com sucesso >")
             Bordas()
             print("Dejesa visualizar as alterações? \n(1) Sim. \n(2) Não. \n")
             c4 = int(input("Escolha uma das opções a cima: "))
             if c4 == 1: 
               print(lc[contato_para_alterar])
             else:
                 print("Ok!")
         else:
           print("< Campo não localizado, tente novamente >")
           print("Os campos que você pode alterar (caso os tenha inseridos antes) são: NOME, TELEFONE, EMAIL, ENDEREÇO, CPF, MATRICULA e NACIONALIDADE ")
       else:
         print("Contato não localizado, tente novamente.")
     else:
       print("OK!")

    if n == 4:
      s3 = Continuar_Voltar()
      if s3 == 1: 
         Bordas()
         print("< Sua agenda foi copiada para a variável: backup >")
         import copy
         from operator import itemgetter
         lc = sorted(lc.items(), key=itemgetter(0))
         backup = copy.deepcopy(lc)
         Bordas()
         print("Deseja visualizar o Backup da Lista de contatos? \n \n(1) Sim. \n(2) Não. \n")
         view = int(input("Selecione uma opção: "))
         if view == 1:
           Bordas()
           print("< Aqui está a cópia > \n")
           print("backup =", backup) 
         else:
           Bordas()
           print("OK!")
      else:
       Bordas()
       print("OK!")  
    if n == 5:
       print("Desejas apagar? \n \n(1) Um contato específico. \n(2) Todos os contatos. \n(3) voltar. \n")
       c2 = int(input("Escolha uma das opções acima: "))
       Bordas()
       if c2 == 1:
          lixo = input(">> Qual contato desejas remover?: ").lower().title().strip()
          del lc[lixo]
          Bordas()
          print("< Contato", lixo, "foi excluído da lista de contatos >")
       if c2 == 2:
         print("Tem certeza que deseja apagar todos os contatos da lista sem um backup? \n \n(1) Sim. \n(2) Não. \n")
         c3 = int(input("Escolha uma das opções acima: "))
         if c3 == 1:
           lc.clear()
           Bordas()
           print("< Lista de contatos excluída >")
         else: 
           Bordas()
           print("OK!")
       else:
         print()
    if n == 6:
       print("Programa finalizado.")