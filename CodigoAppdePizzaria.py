valor = 0 #valor para somatoria

print ('Seja bem vindo a pizzaria do Danilo Cesar Delfino junior') #apresentação do identificador pessoal
print('-------------------------Cardapio----------------------------') #cardapio apresentado
print('| Código | Descrição  |  Pizza Média - M | Pizza Grande – G |')
print('|   21   | Napolitana |     R$ 20,00     |     R$ 26,00     |')
print('|   22   | Margherita |     R$ 20,00     |     R$ 26,00     |')
print('|   23   | Calabresa  |     R$ 25,00     |     R$ 32,50     |')
print('|   24   |  Toscana   |     R$ 30,00     |     R$ 39,00     |')
print('|   25   | Portuguesa |     R$ 30,00     |     R$ 39,00     |')
print('-------------------------------------------------------------')

while True:
    tamanho = input('Qual o tamanho da pizza que deseja? (M/G): ') #questionamento sobre o tamanho da pizza
    if tamanho == 'M': #primeiro If para identificar os tamanhos
      codigo = input('Qual o codigo da pizza que deseja? ') #primeira sequencia para as pizzas medias
      if codigo == '21': #segunda sequencia de IFs com os sabores e preços para cada tamanho
            valor = valor + 20 #valor das pizzas medias
            print('Você pediu uma pizza Media de Napolitano') #achei menos complicado colocar o nome e o tamanho individualmente para diminuir o tamanho do codigos
      elif codigo == '22':
            valor = valor + 20
            print('Você pediu uma pizza Media de Margherita')
      elif codigo == '23':
            valor = valor + 25
            print('Você pediu uma pizza Media de Calabresa')
      elif codigo == '24':
            valor = valor + 30
            print('Você pediu uma pizza Media de Toscana')
      elif codigo == '25':
            valor = valor + 30
            print('Você pediu uma pizza Media de Portuguesa')
      else:
            print('opção invalida!') #invalidação caso tente algo fora dos caracteres oferecidos
            continue
      print('O valor a ser pago está em: {:.2f}'.format(valor)) #uma previa para ver qual será o valor antes de fechar a conta
      resposta = input('Deseja comprar algo a mais? (Digite sim ou não) ') #questionamento simples se o cliente deseja aderir mais algum produto
      if resposta == 'sim':
          continue
      else:
          print('O valor total a ser pago é: {:.2f}'.format(valor)) #valor total a ser pago e logo em seguida a finalização da segunda sequencia de IFs para pizzas M
      break
    elif tamanho == 'G': #ainda na segunda sequencia de IFs com os sabores e preços para cada tamanho
      codigo = input('Qual o codigo da pizza que deseja? ') #mesmo input para questionar o codigo referente as pizzas grandes
      if codigo == '21': # codigo de cada pizza
           valor = valor + 26 #valor calculado referente a cada uma
           print('Você pediu uma pizza Grande de Napolitano')
      elif codigo == '22':
           valor = valor + 26
           print('Você pediu uma pizza Grande de Margherita')
      elif codigo == '23':
           valor = valor + 32.50
           print('Você pediu uma pizza Grande de Calabresa')
      elif codigo == '24':
           valor = valor + 39
           print('Você pediu uma pizza Grande de Toscana')
      elif codigo == '25':
           valor = valor + 39
           print('Você pediu uma pizza Grande de Portuguesa')
      else:
           print('opção invalida!') #invalidação caso tente algo fora dos caracteres oferecidos
           continue
      print('O valor a ser pago está em: {:.2f}'.format(valor)) #previa do valor, para o cliente acompanhar
      resposta = input('Deseja comprar algo a mais? (Digite sim ou não) ')
      if resposta == 'sim': 
          continue
      else:
          print('O valor total a ser pago é: {:.2f}'.format(valor)) #valor total a ser pago e logo em seguida a finalização da segunda sequencia de IFs para pizzas G
      break
    else:
         print('opção invalida!') #caso seja digitado um tamanho diferente, será pedido para refazer e escolher entre M ou G.
         continue