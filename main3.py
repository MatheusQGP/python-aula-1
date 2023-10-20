sexo = str(input("""digite seu sexo :
F ou f = feminino
M ou m = masculino""")).upper().strip()

if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("masculino")
else:
    print ("invalido")
