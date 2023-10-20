frase = str(input("digite uma frase: ")).lower().strip()

contador = 0 
for letra in frase: 
    if letra in "aeiou":
        contador = contador + 1 

print(f"a frase digitada tem {contador} vogais")