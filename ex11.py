#calculo

#n1 = float(input('Qual é o valor do comprimento? '))
#n2 = float(input('Qual é o valor da largura? '))
#r = (n1 * n2) / 2
#print('Sua Área equivalem a {}' .format(n1 * n2))
#print('Para pintar área de 2m, precisa-se de {:.0f} litros' .format(r)) 

#Rosolução da aula

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem  dimensão de {}x{} e sua área é de {}m quadrados ' .format(larg, alt, área))
tinta = área / 2
print('Para pintar a parede, voce precisara de {} litros de tinta ' . format(tinta))