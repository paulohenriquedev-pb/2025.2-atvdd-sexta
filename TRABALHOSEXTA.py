
alturas = []
generos = []

for i in range(1, 16):
    print(f"\nPessoa {i}:")
    
    altura = float(input("Digite a altura (em metros, ex: 1.75): "))
    alturas.append(altura)
    
    while True:
        genero = input("Digite o gênero (M para Masculino / F para Feminino): ").strip().upper()
        if genero in ['M', 'F']:
            generos.append(genero)
            break
        else:
            print("Entrada inválida! Digite apenas M ou F.")

maior_altura = max(alturas)
menor_altura = min(alturas)

soma_altura_homens = 0
qtd_homens = 0
for i in range(len(alturas)):
    if generos[i] == 'M':
        soma_altura_homens += alturas[i]
        qtd_homens += 1

if qtd_homens > 0:
    media_altura_homens = soma_altura_homens / qtd_homens
else:
    media_altura_homens = 0

qtd_mulheres = generos.count('F')

print("\n=== RESULTADOS ===")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
if qtd_homens > 0:
    print(f"Média de altura dos homens: {media_altura_homens:.2f} m")
else:
    print("Não há homens no grupo para calcular a média.")
print(f"Número de mulheres: {qtd_mulheres}")
