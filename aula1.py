# Aula 1 - Formatação de Strings

nome = "Otávio Cabral"
print(f"Meu nome é {nome}")

lucro= 3.14159
print(f"O lucro é de {lucro:.2f}")

porcnt = 0.12345
print(f"O percentual é de {porcnt:.1%}")

# 1.2 Evitando que o código quebre

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Por favor, digite um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# 1.3 Criando uma tabela justificada

print('-' * 50)
print("Ativos".ljust(20) + "Valor".rjust(30) + "\n")
print("Ação A".ljust(20) + "R$ 100,00".rjust(30))
print('-' * 50)
