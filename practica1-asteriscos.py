class Asteriscos:

    numero = 0

    def __init__(self, a):
        self.numero = a

    def generacionPiramide(self):
        num = self.numero

        for i in range(1, num + 1):
            for j in range(i):
                print("*", end="")

            print()
    
def main():
    num = int(input("Ingresar cantidad de digitos de la piramide: "))
    
    obj = Asteriscos(num)
    obj.generacionPiramide()

if __name__ == "__main__":
    main()