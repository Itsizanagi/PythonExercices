#n1 = int(input('Qual é o preço do produto? '))
#d = 5 / 100 
#s = d * n1
#vt = n1 - s
#print('Voce tem 5 por cento de de conto, e equivale a {:.2f} ' .format(vt))

#Resolução do ex na aula

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O protudo que custava {} reais, com o desconto 5%, agora custa {} reais !!!!!!!!!' .format(preço, novo))