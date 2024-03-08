class CalculadoraModel:
    def calcular(self, num1, num2, operacao):
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Divisão por zero não é permitida"

# Visão (View)
class CalculadoraView:
    def mostrar_resultado(self, resultado):
        print("Resultado:", resultado)

    def pedir_entrada(self):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        return num1, num2, operacao

# Apresentador (Presenter)
class CalculadoraPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calcular(self):
        num1, num2, operacao = self.view.pedir_entrada()
        resultado = self.model.calcular(num1, num2, operacao)
        self.view.mostrar_resultado(resultado)

# Código principal
if __name__ == "__main__":
    # Cria instâncias do modelo, visão e apresentador
    model = CalculadoraModel()
    view = CalculadoraView()
    presenter = CalculadoraPresenter(model, view)

    # Inicia o cálculo
    presenter.calcular()