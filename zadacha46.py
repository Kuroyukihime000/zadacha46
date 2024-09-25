from decimal import Decimal
number = Decimal("0.1")
input_data = open('input.txt', 'r')
data = input_data.read()
E = Decimal("2.7182818284590452353602875")
a = int(data)
result = round(E,a)
output_data = open('output.txt', 'w')
output_data.write(str(result)) 

input_data.close()
output_data.close()