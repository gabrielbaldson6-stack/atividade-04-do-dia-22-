try:
    primeiro = float(input("Digite o primeiro número: "))
    segundo = float(input("Digite o segundo número: "))

    resultado = primeiro / segundo

except ValueError:
    print("Erro: digite apenas números válidos.")

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

else:
    print(f"Resultado: {resultado}")

finally:
    print("Operação finalizada.")
    