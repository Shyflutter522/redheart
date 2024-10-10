import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Configuración inicial
speed(0)  # Máxima velocidad
bgcolor("black")  # Fondo negro
penup()  # Levanta el lápiz

# Muestra la imagen como fondo
image_path = r"C:\Users\Pc\Desktop\nurse.gif"  # Asegúrate de que sea un archivo GIF
bgpic(image_path)  # Establece la imagen de fondo

# Dibuja el corazón sin rellenar
penup()
goto(hearta(0) * 20, heartb(0) * 20)
pendown()
color("red")
# Dibuja el contorno del corazón
for i in range(0, 628):
    x = hearta(i / 100) * 20
    y = heartb(i / 100) * 20
    goto(x, y)

# Detiene el lápiz y finaliza
penup()
goto(0, 0)  # Regresa al centro
hideturtle()
done()  # Finaliza
