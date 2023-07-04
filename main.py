import qrcode
import random
import string

def generar_nombre():
    texto = ''.join(random.choices(string.ascii_letters, k=5))
    num = random.randint(0, 999)
    nombre_generado = f"{texto}-{num}.jpg"
    return nombre_generado

file = input("Ingresa un texto o link para convertirlo en un Código QR: ")
img = qrcode.make(file)
filename = generar_nombre()
img.save(filename)
print(f"Imagen guardada con el nombre: {filename}")
