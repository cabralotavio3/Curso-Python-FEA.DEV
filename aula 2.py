# Aula 2 - Estruturas Condicionais

#2.1 Listas
 
lista = ["Cruzeiro", "Flamengo", "São Paulo"]
lista2 = lista[0:1]

lista2.append(lista[2])
lista2.remove(lista[2])

# 2.2 Condicionais

#if, else e elif

i = 0
while i< 100:
    print("Cruzeiro é gigante")
    i+=1
    if i == 99:
        break


palavra = "tudobem?"
for letra in palavra:
    print(letra)


for i in range(4):
    print(i)


#Exercício: Fatorial

numero = int(input("Qual número voce deseja calcular o fatorial?  "))
i = 1
fatorial = 1
while i < numero:
    fatorial *= numero-i
    i+=1
print(f"O seu fatorial é {numero * fatorial}")