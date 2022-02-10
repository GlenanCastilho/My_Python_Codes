from forex_python.converter import CurrencyRates

c = CurrencyRates()

vl = float(input("\nValor em dólar: "))

r = round(c.convert("USD", "BRL", vl), 2)

print(f"${vl} = R$ {r}")