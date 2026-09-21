try:
    saldo = float(input("Informe o saldo da conta: "))
    saque = float(input("Informe o valor do saque: "))

    if saque <= 0:
        raise ValueError("O valor do saque deve ser maior que zero.")

    if saque > saldo:
        raise ValueError("O valor solicitado é maior que o saldo disponível.")

except ValueError as erro:
    print(f"Erro: {erro}")

else:
    saldo_restante = saldo - saque
    print("Saque realizado com sucesso!")
    print(f"Saldo restante: R$ {saldo_restante:.2f}")

finally:
    print("Operação bancária finalizada.")
