# conversão de m em cm 

#n1 = int(input('Digite um algum metro: '))
#convert = n1 * 100
#print(' {} metros equivalem a {} centimetros' .format(n1, convert))

#Resolução da aula

medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A distancia de {}m corresponde a {:.0f}cm e {:.0f}mm' .format(medida, cm, mm))