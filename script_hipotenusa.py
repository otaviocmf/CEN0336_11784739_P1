# Importar o módulo sys para trabalhar com argumentos da linha de comando
import sys

# Verificar se o número correto de argumentos foi fornecido
if len(sys.argv) != 3:
    print("Erro: Forneça exatamente dois inteiros como argumentos.")
    sys.exit(1)

# Atribuir argumentos às variáveis a e b
a, b = sys.argv[1], sys.argv[2]

# Verificar se os argumentos são inteiros e seguem as restrições especificadas
if not (a.isdigit() and b.isdigit() and 0 < int(a) < 500 and 0 < int(b) < 500):
    print("Erro: Ambos os argumentos devem ser inteiros positivos menores que 500.")
    sys.exit(1)

# Converter argumentos para inteiros
a, b = int(a), int(b)

# Calcular o quadrado da hipotenusa
hipotenusa_quadrada = a**2 + b**2

# Imprimir o resultado
print(f"O quadrado da hipotenusa para o triângulo retângulo com lados a={a} e b={b}, é {hipotenusa_quadrada}")

