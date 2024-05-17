listaProdutos = []

def cadastrarProduto(codigo): #cadastro geral de produtos da mercearia
  print('Você selecionou a opção de Cadastrar Produto')
  print('O código do Produto é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome do Produto:')
  fabricante = input('Entre com o fabricante da Produto:')
  valor = float(input('Entre com o valor R$ do Produto:'))
  dicionarioProdutos = {'codigo'   : codigo, #Dicionario que abrange as informações para os produtos
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  listaProdutos.append(dicionarioProdutos.copy()) #codigo para copia

def consultarProduto(): #consulta geral de produtos da mercearia
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Produtos') #nova pesquisa para a consulta de produtos especificos, conforme pedido.
      Consultar = int(input('Entre com a opção desejada\n1- Consultar Todos os Produtos\n2- Consultar Produtos por Código\n3- Consultar Produtos por Fabricante\n4- Retornar\n>>'))
      if Consultar == 1:
        print('-' * 20)
        for Produtos in listaProdutos:
            for key, value in Produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif Consultar == 2:
        print('Você Selecionou a Opção Produtos por Código')
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        for Produtos in listaProdutos:
          if(Produtos['codigo'] == entrada):
            for key, value in Produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif Consultar == 3:
        print('Você Selecionou a Opção Produtos por Fabricante')
        entrada = input('Digite o Fabricante: ')
        print('-' * 20)
        for Produtos in listaProdutos:
          if(Produtos['fabricante'] == entrada):
            for key, value in Produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif Consultar == 4:
        break
      else:
        print('Por favor digite somente o que é pedido')
        continue
    except ValueError:
      print('Digite apenas valores existentes!')
      continue
def removerProduto(): #remoção geral de produtos da mercearia
    print('Você Selecionou o Remover Produto')
    entrada = int(input('Digite o Código do Produto que irá remover: '))
    for Produtos in listaProdutos:
      if(Produtos['codigo'] == entrada):
        listaProdutos.remove(Produtos)
    else:
      print('Você removeu o código do Produto.')

print('Seja bem vindo ao controle de estoque da fabrica de alimentos do Danilo') #identificação do codigo

registroProdutos = 0
while True:
    try:
      opcao = int(input('Digite a opção desejada:\n1- Cadastrar Produtos\n2- Consultar Produtos\n3- Remover Produtos\n4- Sair\n>>'))
      if opcao == 1:
        registroProdutos = registroProdutos + 1
        cadastrarProduto(registroProdutos)
      elif opcao == 2:
        consultarProduto()
      elif opcao == 3:
        removerProduto()
      elif opcao == 4:
        print('Programa terminado!')
        break
      else:
        print('Digite apenas as opções do MENU')
        continue
    except ValueError:
        print('Digite apenas valores existentes!') #finalização do codigo.