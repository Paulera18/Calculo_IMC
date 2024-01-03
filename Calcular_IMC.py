def calcular_imc(peso, altura):

    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def main():
    try:
        
        peso = float(input("Digite seu peso em quilogramas: "))
        altura = float(input("Digite sua altura em metros: "))

        imc = calcular_imc(peso, altura)

        interpretacao = interpretar_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Interpretação: {interpretacao}")

    except ValueError:
        print("Erro: Certifique-se de inserir números válidos para peso e altura.")

if __name__ == "__main__":
    main()
