class AnalizadorArreglo:
    def __init__(self):
        self.arreglo = []

    def ingreso_datos(self):

        try:
            cantidad = int(input("Cuántos números quieres agregar a tu arreglo : "))
            
            entrada = input("Ingresa los números separados por espacio : ")
            
            self.arreglo = [int(num) for num in entrada.split()][:cantidad]

        except ValueError as e:
            print("Pes - ta - ñas - tE :", e)

    def proceso(self):
        
        ordenados = sorted(self.arreglo)
    
        unicos = set(self.arreglo)
        
        pares = []
        for num in unicos:
            if num % 2 == 0:
                pares.append(num)
        
        impares = []
        for num in unicos:
            if num % 2 != 0:
                impares.append(num)
        
        repetidos = {}
        for num in unicos:
            if self.arreglo.count(num) > 1:
                repetidos[num] = self.arreglo.count(num)

        return ordenados, pares, impares, repetidos

if __name__ == "__main__":
    
    analizador = AnalizadorArreglo()
    
    analizador.ingreso_datos()

    ordenado, pares, impares, repetidos = analizador.proceso()

    print("Arreglo ordenado : ", ordenado)
    print("Arreglo de números pares : ", pares)
    print("Arreglo de números impares : ", impares)
    print("Números repetidos y su cantidad de repeticiones : ", repetidos)
