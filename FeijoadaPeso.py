acompanhamentos = {
   0: ["Não quero mais acompanhamentos (encerrar pedido)", 0],
   1: ["200g de arroz", 5],
   2: ["150g de farofa especial", 6],
   3: ["100g de couve cozida", 7],
   4: ["1 laranja descascada", 3]}

# Função para a quantidade de feijoada
def quantidadeF(): #para a quantidade de feijoada
   valor = 0
   print('\nVolume de feijoada')
   while True:
        try:
            quantidade = float(input('\nDigite a quatidade da Feijoada em ml: '))
            if quantidade <= 299 or quantidade >= 5001:
                print('Apenas aceitamos quantidades de 300ml á 5L, por valor digite novamente')
            else:
                valor = quantidade * 0.08
                break
        except ValueError:
            print('Digite um valor valido!')
   return valor

 # Função Opções da feijoada
def opcaoF(): #para as opções disponiveis de feijoada que temos
   multiplicador = 0
   print('Opção de feijoada')
   while True:
       try:
           opcao = input('Entre com a opção de Feijoada:\nb - Básica (Feijão + Paiol + Costelinha)\np - Premium (Feijão + Paiol + Costelinha + Partes de porco)\ns - Suprema (Feijão + Paiol + Costelinha + Partes do porco + Charque + Calabresa + Bacon\n>>')
           if opcao == 'b':
              return 1.00
           elif opcao == 'p':
              return 1.25
           elif opcao == 's':
              return 1.50
           else:
               print('Digite um valor valido')
               continue
       except ValueError:
           print('Digite um valor valido')
   return multiplicador

#Função Acompanhamento de feijoada
def acompanhamentoF(): # e para finalizar os acompanhamentos de feijoada
   totaldeacompanhamento = 0
   print('Acompanhamentos para a feijoada')
   while True:
       try:
           print("\nDeseja mais algum acompanhamento:")
           for key, values in acompanhamentos.items():
               print(f"{key} - {values[0]}")
           opcao = int(input())
           if opcao not in acompanhamentos.keys():
               print("\nOpção inválida\n")
           elif opcao == 0:
               break
           else:
               totaldeacompanhamento += acompanhamentos[opcao][1]
       except ValueError:
           print("\nDigite um acompanhamento válido.\n")
   return totaldeacompanhamento

#programa principal
print ('Seja bem vindo ao Programa de fechamento de pedido da feijoada do Danilo') #apresentação do identificador pessoal
mililitros = quantidadeF() #representação da quantidade
Escolha = opcaoF() #representação das opções
Complemento = acompanhamentoF() #representação daos complementos
total = (mililitros * Escolha) + Complemento
print(f"\nO valor total a ser pago pelo seu pedido é de (R$): {total:.2f} (Volume = {mililitros:.2f} * opcao = {Escolha:.2f} + Acompanhamento = {Complemento:.2f})")