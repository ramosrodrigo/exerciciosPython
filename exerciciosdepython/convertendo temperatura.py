t_fahrenheit = float(input())
t_celsius = float((t_fahrenheit - 32)) * 5/9
t_kelvin = float(t_celsius + 273.15)

print("Convertendo",t_fahrenheit,"graus Fahrenheit temos:")
print(t_celsius,"graus Celsius e",t_kelvin,"Kelvin")

