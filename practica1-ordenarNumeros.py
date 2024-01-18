class OrdenarNumeros:

    nums = []
    
    def __init__(self, a):
        self.nums = a

    def ordenar(self):
        self.nums.sort()
        print("Lista de números ordenados: {}".format(self.nums))

    def mostrar_pares(self):
        pares = []

        for num in self.nums:
            if num % 2 == 0:
                pares.append(num)

        print("Lista de números pares: {}".format(pares))

    def mostrar_impares(self):
        impares = []

        for num in self.nums:
            if num % 2 == 1:
                impares.append(num)

        print("Lista de números impares: {}".format(impares))

    def mostrar_repetidos(self):
        repeticiones = {}

        for num in self.nums:
            if num in repeticiones:
                repeticiones[num] += 1
            else:
                repeticiones[num] = 1

        print("Números y sus repeticiones:")

        for num, cantidad in repeticiones.items():
            if cantidad > 1:
                print("{} se repite {} veces".format(num, cantidad))

def main():
    cantidad = int(input("¿Cuantos números deseas ingresar?: "))
    print()
    numeros = []

    for i in range(1, cantidad + 1):
        numero = int(input("Ingresa el número {}: ".format(i) ))
        numeros.append(numero)
    print()
    
    print("--- Lista de números original: {} ----".format(numeros))
    print()

    obj = OrdenarNumeros(numeros)

    obj.ordenar()
    print()

    obj.mostrar_pares()
    print()

    obj.mostrar_impares()
    print()

    obj.mostrar_repetidos()
    print()

if __name__ == "__main__":
    main()