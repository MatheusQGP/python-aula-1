letra=str(input("digite uma letra: ")) .lower().strip()

if letra in "aeiou":
    print(f"{letra} é uma vogal")
elif letra in "bcdfghjklmnpqrstvxywz":
    print(f"{letra} e uma consoante")
else:
    print("meu fi, digite uma letraaaaaaaaaaaaa, conhece o alfabeto tu?")