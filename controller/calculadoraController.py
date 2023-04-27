class CalculadoraController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def sumar(self):
        self.modelo.valor1 = self.vista.obtener_valor("Ingrese el valor #1: ")
        self.modelo.valor2 = self.vista.obtener_valor("Ingrese el valor #2: ")
        self.modelo.sumar()
        self.vista.mostrar_resultado(self.modelo.resultado)

    def restar(self):
        self.modelo.valor1 = self.vista.obtener_valor("Ingrese el valor #1: ")
        self.modelo.valor2 = self.vista.obtener_valor("Ingrese el valor #2: ")
        self.modelo.restar()
        self.vista.mostrar_resultado(self.modelo.resultado)