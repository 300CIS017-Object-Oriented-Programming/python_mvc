class CalculadoraView:
    def obtener_valor(self, mensaje):
        return int(input(mensaje))

    def mostrar_resultado(self, resultado):
        print("El resultado es: ", resultado)