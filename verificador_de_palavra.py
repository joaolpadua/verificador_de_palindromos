palavra = input("Qual palavra deseja verificar? ").lower()
lista_palavra = list(palavra)
tamanho = int(len(lista_palavra))
palavra_contrario = []
while tamanho:
    letra = lista_palavra[tamanho-1]
    palavra_contrario.append(letra)
    tamanho -= 1
if  lista_palavra == palavra_contrario:
    print(f"Sim! {palavra} é um palíndromo! ")

else:
    print(f"Não! {palavra} não é um palíndromo! ")




