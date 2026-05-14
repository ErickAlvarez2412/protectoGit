def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatura = 30
resultado = celsius_a_fahrenheit(temperatura)

print(f"{temperatura}°C equivalen a {resultado}°F")