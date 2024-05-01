# Calculadora de Segundos
print("Calculadora de Segundos")

# Solicita entrada do usuário para horas, minutos e segundos
horas = int(input("Quantas horas? \n"))
minutos = int(input("Quantos minutos? \n"))
segundos = int(input("Quantos segundos? \n"))

# Converte o tempo para segundos
total_segundos = horas * 60 * 60 + minutos * 60 + segundos

# Exibe o total de segundos
print(f"Nesse intervalo de tempo há {total_segundos} segundos!")

# Calculadora de Milhas
print("\nCalculadora de Milhas")

# Solicita entrada do usuário para quilômetros e metros
quilometros = float(input("Quantos quilometros? \n"))
metros = float(input("Quantos metros? \n"))

# Converte a distância para milhas
total_milhas = quilometros / 1.61 + metros / 1000 / 1.61

# Exibe o total de milhas
print(f"Essa distância são {total_milhas} milhas")

# Calculadora de Passo Médio
passo_medio = total_segundos / total_milhas

# Exibe o passo médio
print(f"Seu passo médio é: {passo_medio:.2f} segundos/milha")

# Calculadora de milha por hora
milha_por_hora = 60 * 60 / passo_medio

# Exibe a velocidade em milhas por hora
print(f"Sua velocidade é de {milha_por_hora:.2f} milhas/hora")
