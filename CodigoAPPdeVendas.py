print('Seja muito bem-vindo a loja do Danilo') #Adicionei o meu nome como identificação da "loja".

valordeproduto = float (input('insira o valor unitario dos produtos: ')) #para o valor determinado de cada produto

qntdproduto = float (input('insira a determinada quantidade de produtos adquiridos: ')) #para quantos produtos serão adquiridos

totalproduto = valordeproduto * qntdproduto #calculo para determinar o valor do produto x sua quantidade

if 0<= qntdproduto <= 4: #Conforme as aulas dos professores,o adicionado um 0<= para melhora do sistema.
    valorFinal = totalproduto
elif 5 <= qntdproduto <= 19:
    valorFinal = totalproduto - totalproduto * 0.03 #Desconto de 3% para essa determinada quantidade de produtos
elif 20 <= qntdproduto <= 99:
    valorFinal = totalproduto - totalproduto * 0.06 #Desconto de 6% para essa determinada quantidade de produtos
else:
    valorFinal = totalproduto - totalproduto * 0.10 #Desconto de 10% para essa determinada quantidade de produtos

print('valor sem desconto do produto é: R$ {:.2f}'. format(totalproduto))
print('valor com desconto do produto é: R$ {:.2f}'. format(valorFinal))

#Após a finalização do calculo com desconto e sem o desconto, verifiquei diversos valores e derão todos certos para a finalização desta questão.