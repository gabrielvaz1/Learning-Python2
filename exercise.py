qtd = 0
sum = 0
average = 0
value = float(input("Write a value: "))

while (value> 0.0):
    sum = sum + value
    qtd = qtd +1

    #Value Inputs
    value = float(input("write a value: "))

#If you write a negative value the while end

average = sum / qtd
print("\n Totaly sum: ",sum)
print("\n quantity of wrotes values: ",qtd)
print("\n Average Values: ",average)
