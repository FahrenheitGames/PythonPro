import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("Que longitud de contraseña deseas?: "))
password = ""

for i in range(long):
    password += random.choice(caracteres)

print("Se ha generado la contraseña: ", password)