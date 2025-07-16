class CalculadoraBasica:
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        return a + b
# Uso del objeto
calculadora = CalculadoraBasica()
print(calculadora.sumar(3, 7))



calc = CalculadoraBasica()
print(calc.sumar(5, 3))
numero = int(input ("Ingrese numero"))