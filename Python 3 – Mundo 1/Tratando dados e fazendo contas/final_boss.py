aluguel = 60
valor_km = 0.15

dias = int(input("Dias: "))
km = float(input("Km: "))

valor_km_total = km * valor_km
valor_dias_total = dias * aluguel
valor_total = valor_km_total + valor_dias_total

print(f"Você alugou por {dias} dias e percorreu {km}km.")
print(f"➡️ R${valor_km_total:.2f} por KM")
print(f"➡️ R${valor_dias_total:.2f} por dias de aluguel")
print(f"💰 Total a pagar: R${valor_total:.2f}")
