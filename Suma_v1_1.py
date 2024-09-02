def calcularSuma(sumando1, sumando2):
    return sumando1 + sumando2
def leerSumandos():
    sumando1 = int(input("Primer Sumando: "))
    sumando2 = int(input("Segundo Sumando: "))
    return sumando1, sumando2

if  __name__== '__main__':
    sumando1, sumando2 = leerSumandos()
    print(f"{sumando1} + {sumando2} = {calcularSuma(sumando1,sumando2)}")
