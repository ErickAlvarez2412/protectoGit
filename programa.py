def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def calcular_area_rectangulo(base, altura):
    return base * altura


temperatura = 30
resultado_temp = celsius_a_fahrenheit(temperatura)

print(f"{temperatura}°C equivalen a {resultado_temp}°F")


base = 5
altura = 10
resultado_area = calcular_area_rectangulo(base, altura)

print(f"El área del rectángulo es: {resultado_area}")