#n1 = int(input('Qual é seu salário? '))
#d = 15 / 100
#s = d * n1
#vt = n1 + s
#print('Voce tem um novo salário!, seu salário atual é de {:.0f}! ' .format(vt))

n1 = float(input('Qual é o seu salário atual ? R$ '))
n = n1 + (n1 * 15 / 100)
print('Parabens, voce conseguiu um aumento de 15%, seu antigo salário era {} reais, o seu novo é {:.2f} reais!!!!!!' .format(n1, n))