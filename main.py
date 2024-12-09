# Exemplo que causa TypeError
nome = "Lucas"

try:
    resultado = len(nome)
    print(resultado)
except TypeError as e:
    print(e)  
else:
        print("Deu bom")
finally:
     print("Nois tenta ate dar bom")