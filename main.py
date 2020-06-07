print('Empresa com Fretes e Peças.\n')

nomev = str(input('QUal o nome do vendedor?.\n'))
nomec = str(input('Qual o nome do cliente?\n'))

def frete(cod, pecas, custo_total):
	if cod == 1 and pecas < 1000:
		frete = pecas
	elif cod == 1 and pecas > 1000:
		frete = custo_total*0.1
	elif cod == 2 and pecas < 1000:
		frete = pecas * 1.1
	elif cod == 2 and pecas > 1000:
		frete = custo_total * 0.08
	elif cod == 3 and pecas < 1000:
		frete = pecas * 1.15
	elif cod == 3 and pecas > 1000:
		frete = custo_total * 0.07
	elif cod == 4 and pecas < 1000:
		frete = pecas * 1.2
	elif cod == 4 and pecas > 1000:
		frete = custo_total * 0.11
	elif cod == 5 and pecas < 1000:
		frete =  pecas * 1.25
	elif cod == 5 and pecas > 1000:
		frete = custo_total * 0.15
	elif cod == 6 and pecas < 1000:
		frete = pecas * 1.3
	elif cod == 6 and pecas > 1000:
		frete = custo_total * 0.12
	elif cod == 7 and pecas < 1000:
		frete = pecas * 1.4
	elif cod  == 7 and pecas > 1000:
		frete = custo_total * 0.18
	elif cod == 8 and pecas < 1000:
		frete = pecas * 1.35
	elif cod == 8 and pecas > 1000:
		frete = custo_total * 0.15
	return frete
def comissao(valor_venda):
	comissao = valor_venda * 0.065
	return comissao
def regiao(cod):
	if cod == 1:
		regiao = 'Sul'
	elif cod == 2:
		regiao = 'Norte'
	elif cod ==3:
		regiao = 'Leste'
	elif cod == 4:
		regiao = 'Oeste'
	elif cod == 5:
		regiao = 'Noroeste'
	elif cod == 6:
		regiao = 'Sudeste'
	elif cod == 7:
		regiao = 'Centro-Oeste'
	elif cod == 8:
		regiao = 'Nordeste'
	return regiao

while True:

	cod = int(input('Qual a região de localização do cliente? \n 1. Sul \n 2. Norte \n 3. Leste \n 4. Oeste \n 5. Noroeste \n 6. Sudeste \n 7. Centro-Oeste \n 8. Nordeste. \n 9. Sair\n'))

	if cod == 9:
		break

	pecas = int(input('Quantas peças foram adquiridas?\n'))
	custo_total = pecas * 7
	valor_venda = custo_total + (custo_total*0.5)
	lucro = valor_venda - comissao(valor_venda) - custo_total

	print('\n FATURA DE TRANSPOTE E AQUISIÇÃO DE PEÇAS \n Nome do Cliente:..........', nomec,'\n',
	'Nome do vendedor:..........',nomev,'\n'
	'Região:..........',regiao(cod),'\n',
	'-------------------------------\n',
	'Quantidade de peças adquiridas:..........',pecas,'\n',
	'Custo total das peças:..........R$%.2f'%custo_total,'\n',
	'Comissão do vendedor:..........R$%.2f'%comissao(valor_venda),'\n',
	'Valor total da venda:..........R$%.2f'%valor_venda,'\n',
	'Frete:..........R$%.2f'%frete(cod, pecas, custo_total),'\n',
	'-----------------------------------------------','\n',
	'Lucro:..........R$%.2f'%lucro)


