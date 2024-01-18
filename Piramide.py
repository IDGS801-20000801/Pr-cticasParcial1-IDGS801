class Piramide:
    def __init__(self, numero):
        self.numero = numero

    def generar(self):
        i = 0
        while i <= self.numero:
            asteriscos = "* " * i
            print(asteriscos)
            i += 1


def main():
    try:
        numero_piramide = int(input("Cuanto quieres que mida tu piramide : "))
        if numero_piramide <= 0:
            print("No puede ser CERO ")
        else:
            piramide = Piramide(numero_piramide)
            piramide.generar()
    except ValueError:
        print("solo hace pirámides ENTERAS no uses flotantes u algún otro carácter")

if __name__ == "__main__":
    main()
