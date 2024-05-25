file = open('arqText.txt', 'w')


file.write('curso Python \n')
file.write('Aula Prática')
file.close()

#Reading file text

reading = open('arqText.txt', 'r')
print(reading.read())
reading.close()