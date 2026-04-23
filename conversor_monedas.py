
#Valor de monedas: Pesos chilenos (CLP), Dólar (USD), Euro (EUR), Yen (JPY)

#Tasas de cambio en relación al dolar
USD = 1
CLP = 891.45
EUR = 0.85
JPY = 159.48

def a_usd(monto, moneda_origen):
    if moneda_origen == "USD":
        return monto
    elif moneda_origen == "CLP":
        return monto / CLP
    elif moneda_origen == "EUR":
        return monto / EUR
    elif moneda_origen == "JPY":
        return monto / JPY
    else:
        return None


def desde_usd(monto_usd, moneda_destino):
    if moneda_destino == "USD":
        return monto_usd
    elif moneda_destino == "CLP":
        return monto_usd * CLP
    elif moneda_destino == "EUR":
        return monto_usd * EUR
    elif moneda_destino == "JPY":
        return monto_usd * JPY
    else:
        return None


moneda_origen = input("Ingrese la moneda origen (CLP, USD, EUR, JPY): ").strip().upper()
monto = float(input("Ingrese el monto a convertir: ").strip())
moneda_destino = input("Ingrese la moneda a la que quiere convertir (CLP, USD, EUR, JPY): ").strip().upper()

paso_1 = a_usd(monto, moneda_origen)
paso_2 = desde_usd(paso_1, moneda_destino)


print("Usted ingresó: $"+str(monto)+" "+moneda_origen)
print("Su conversión total es de: $"+str(round(paso_2,2))+" "+moneda_destino)

