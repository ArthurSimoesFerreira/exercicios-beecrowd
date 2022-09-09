cardapiozinho = [4.00, 4.50, 5.00, 2.00, 1.50]
cod, quant = map(int, input().split())
total = (cardapiozinho[cod - 1] * quant)
print(f"Total: R$ {total:.2f}")