# 1
num_in = int(input("Inserir um numero inteiro: "))
num_in_2 = int(input("Inserir um denominador: "))
resultado = num_in // num_in_2
print(resultado) 

# 2
import math 
raio_circulo = float(input("Insira o raio: "))
area_circ = math.pi *raio_circulo** 2
# area_format = "{:.2f}".format(area_circ)
print(f"{area_circ:.2f}")

# 3 
data_do_user = input("Insira uma data no formato dd/mm/aaaa: ")
data_separada = data_do_user.split("/")
print(data_separada)