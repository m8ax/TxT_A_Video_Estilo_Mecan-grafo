############################################################################################################################################################################
#
#  Programado Por Marcos Ochoa Diez - M8AX - MvIiIaX - 25-Ene-2023
#
#  Programa Para Generar Un Video Del Texto Que Queramos En Modo Mecanógrafo, Sin Exceder 14351x12470, Con Fondo Aleatorio Entre 2 O Fondo Negro Y Dentro, El Contenido Del
#  Fichero Texto.TxT, Cada Carácter Del Texto, De Un Color, Que Será Aleatorio.
#  Al Final Tendremos 1 Fichero, M8AX-Mecanografía.Mp4, Con El Contenido Del Fichero De Texto. Video A Los Fps, Que Le Digamos. FPS A 7 = Mecanógrafo Real.
#  Se Necesita Una Fuente TTF, tahoma.ttf, Incluida Y 4 Fondos De Audio, En MP3, También Incluidos Para Hacer El Video. El Audio Será Aleatorio Entre Los 4 Sonidos.
#  Se Necesitan 2 Fondos De Imágen, También Incluidos, El Fondo Será Aleatorio En Cada Video Generado, Como Los 4 Sonidos Anteriores, Si Así Lo Hemos Elegido.
#  Se Necesita Un Fichero Texto.TxT Con El Texto Que Queramos. Se Incluye Texto.TxT Con La Declaración De Independencia De EEUU De 1776.
#
#  --- NOTA ---
#
#  Al Comenzar El Programa, Podremos Elegir Entre Usar Los Fondos Aleatorios En PNG, Que Ya Están Incluidos O Que El Fondo Sea Negro.
#  Si Elegimos Los Fondos PNG Que Ya Tenemos, Hay Que Respetar Su Resolución, A La Hora De Hacer El Video, Sino... Podremos Elegir La Resolución Que Queramos.
#  Esta Versión Crea Varios Ficheros JPG, Hasta Que Texto.TxT Termine, Para Hacer El Video.
#  Los Saltos De Línea Serán Saltos De Línea...
#
#  --- NOTA IMPORTANTE ---
#
#  Ahora Se Puede Elegir El Color RGB De Los Caracteres, Entre Aleatorios O El Que Tu Elijas Y También El FrameRate Del Video...
#
#  Si Seleccionas Usar Los Fondos Aleatorios, Ya No Es Necesario Decirle La Resolución Que Tienen, La Averigua El Programa, Con Lo Que Si Quieres Añadir 2 Imágenes
#  Aleatorias En PNG, Solo Tendras Que Respetar Sus Nombres Ya Que El Programa Elegirá Una De Las 2 Y Averiguará El Tamaño Que Tiene.
#
#  Ejemplo - py m8ax_TxT_In_JpG_VidTxT_Mecano.py
#
############################################################################################################################################################################

import time
import math
import subprocess
import glob
import numpy as np
import sys
import os
from PIL import ImageFont, ImageDraw, Image
from subprocess import call
from os import remove

def segahms(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas * 60 * 60
    minutos = int(segundos / 60)
    segundos -= minutos * 60
    return f"{horas}h:{minutos}m:{int(segundos)}s"

def barra_progreso_vibrante(progreso, total, tiembarra):
    porcen = 100 * (progreso / float(total))
    segrestante = 0
    if porcen > 0:
        segrestante = (100 * (tiembarra - time.time()) / porcen) - (
            tiembarra - time.time()
        )
    barra = "█" * int(porcen) + "-" * (100 - int(porcen))
    print(
        (
            f"\r\033[38;2;{np.random.randint(0, 256)};{np.random.randint(0, 256)};{np.random.randint(0, 256)}m|{barra}|"
            f" - ETA - {segahms(segrestante*-1)} - {porcen:.2f}%      "
        ),
        end="\r\033[0m",
    )

os.system("cls")

with open("Texto.TxT", "r", encoding="utf-8") as file:
    ficherillo = file.read()
    caratot = len(ficherillo)
file.close()

print(
    f"... Comienzo Del Programa. Recuerda: Si Vas A Usar Los 2 Fondos PNG Aleatorios, El Video Se Hará, Respetando La Resolución\nDel Fondo Que Elija El Programa, Si Eliges Fondo Negro, Podrás Tu Decidir La Resolución Del Video. Así Que... Si Quieres\nUsar Los Fondos Aleatorios, Cerciórate Antes, De Que Tengan La Resolución Que Quieres, Para Hacer El Video ...\n"
)
negro = int(
    input(
        "\n... 1 - A Elegir Entre Los 2 Fondos Que Tenemos En PNG, 2 - Fondo Negro Y Resolución Que Se Nos Antoje ...\n\n"
    )
)

fondoele = np.random.randint(0, 101)
fondoso = np.random.randint(1, 6)

if fondoso == 1:
    fondiso = "M8AX-1.Mp3"
if fondoso == 2:
    fondiso = "M8AX-2.Mp3"
if fondoso == 3:
    fondiso = "M8AX-3.Mp3"
if fondoso == 4:
    fondiso = "M8AX-4.Mp3"
if fondoso == 5:
    fondiso = "M8AX-5.Mp3"

if negro == 1:
    if fondoele % 2 == 0:
        img = Image.open("mviiiax-fondo1.png")
    else:
        img = Image.open("mviiiax-fondo2.png")
    width = img.width
    height = img.height

if negro == 2:
    width = int(
        input(
            "\n... Dime Los Píxeles De Ancho, Que Quieres Para La Imágen Generada ...\n\n"
        )
    )
    height = int(
        input(
            "\n... Dime Los Píxeles De Alto, Que Quieres Para La Imágen Generada ...\n\n"
        )
    )

if negro == 2:
    img = Image.new("RGB", (width, height), color="black")
    img.save("m8ax.png")
    img = Image.open("m8ax.png")

framerate = int(
    input(
        "\n... Dime El FrameRate Que Quieres Para Hacer El Video 1 = 1 Carácter Por Segundo En Pantalla ...\n\n"
    )
)
colovario = int(
    input(
        "\n... 1 - Quiéres Cada Letra De Un Color Aleatorio O 2 - Prefieres Que Todas Las Letras Sean Del Mismo Color ...\n\n"
    )
)

if colovario == 2:
    print(
        f"\n... Ingresa Los Valores RGB Para Cada Color, Se Te Pedirán Los 3, Ya Sabes, El Formato RGB ...\n"
    )
    rojo = int(input(f"... Ingresa El Valor Para El Color Rojo ...\n\n"))
    verde = int(input(f"\n... Ingresa El Valor Para El Color Verde ...\n\n"))
    azul = int(input(f"\n... Ingresa El Valor Para El Color Azul ...\n\n"))

print(
    f"\n... Haciendo Ficheros Jpg De {width}x{height} Píxeles, Con Los Caracteres Del Texto ...\n"
)

font = ImageFont.truetype("tahoma.ttf", 48)

ubica1 = 5
ubica2 = 0
frase = ""
fiche = 0
cuenta = 0
draw = ImageDraw.Draw(img)
tiembarra = time.time()

with open("Texto.TxT", "r", encoding="utf-8") as file:

    for line in file:
        for char in line:
            if char == "\n":
                ubica2 += 60
                ubica1 = -20
            cuenta += 1
            if colovario == 1:
                colorle = (
                    np.random.randint(60, 256),
                    np.random.randint(60, 256),
                    np.random.randint(60, 256),
                )
            else:
                colorle = (rojo, verde, azul)
            if len(frase) < 81:
                frase = frase + char
            draw.text((ubica1, ubica2), char, font=font, fill=colorle)
            fiche += 1
            img.save(
                "M8AX-" + str(fiche) + ".JpG",
                "JPEG",
                quality=75,
            )
            ubica1 += 28
            if ubica1 > (width - 26):
                ubica1 = 5
                ubica2 += 60
            if ubica2 > (height - 60):
                fiche += 1
                ubica1 = 5
                ubica2 = 0
                img.save("M8AX-" + str(fiche) + ".JpG", "JPEG", quality=75)
                if negro == 1:
                    if fondoele % 2 == 0:
                        img = Image.open("mviiiax-fondo1.png")
                    else:
                        img = Image.open("mviiiax-fondo2.png")
                else:
                    img = Image.open("m8ax.png")
                draw = ImageDraw.Draw(img)
        barra_progreso_vibrante((cuenta * 100) / (caratot), 100, tiembarra)

barra_progreso_vibrante((caratot * 100) / (caratot), 100, tiembarra)
fiche += 1
file.close()
img.save("M8AX-" + str(fiche) + ".JpG", "JPEG", quality=75)
cucu = ""

for filename in sorted(glob.glob("*.jpg"), key=os.path.getmtime):
    cucu = cucu + "file '" + filename + "'\n"

with open("m8ax.txt", "w") as file:
    file.write(cucu)
file.close()

print(f"\n\n... Se Han Creado {fiche} Imágenes, Haciendo Video Con Todas Ellas ...\n")
call(
    [
        "ffmpeg",
        "-r",
        str(framerate),
        "-threads",
        "8",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        "m8ax.txt",
        "-c:v",
        "hevc_amf",
        "M8AX-Mecanografía-SA.Mp4",
    ]
)
print(
    f"\n... Video Creado, Metiendo Audio Al Video, Hasta Lo Que Dure El Propio Video, Repitiendo El Audio Y Añadiendo A Su Vez, MetaDatos ...\n"
)

os.remove("m8ax.txt")

if negro == 2:
    os.remove("m8ax.png")

files = glob.glob("m8ax*.jpg")

for f in files:
    os.remove(f)

call(
    [
        "ffmpeg",
        "-threads",
        "8",
        "-i",
        "M8AX-Mecanografía-SA.Mp4",
        "-stream_loop",
        "-1",
        "-i",
        fondiso,
        "-shortest",
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-metadata",
        "episode_id=M8AX - Fichero De Texto - " + frase,
        "-metadata",
        "copyright=-///\\\ --- MvIiIaX & M8AX 2020 - 2030 --- ///\\\-",
        "-metadata",
        "description=Mi Página En OnCyber - https://oncyber.io/m8ax",
        "-metadata",
        "genre=--- MarcoS OchoA DieZ ---",
        "-metadata",
        "grouping=--- MarcoS OchoA DieZ ---",
        "-metadata",
        "album_artist=MvIiIaX - M8AX - THE ALGORITHM MAN - M8AX - MvIiIaX",
        "-metadata",
        "author=--- MarcoS OchoA DieZ ---",
        "-metadata",
        "show=Mi Canal De Youtube - https://youtube.com/m8ax",
        "-metadata",
        "grouping=Mi Blog - https://mviiiaxm8ax.blogspot.com",
        "-metadata",
        (
            "comment=1 - Por Muchas Vueltas Que Demos, Siempre Tendremos El Culo Atrás... 2 - El"
            " Futuro... No Esta Establecido, Solo Existe... El Que Nosotros Hacemos... 3 - Fichero"
            " De Texto En Video, Tipo Mecanógrafo, Compilado En Honor A MDDD Por M8AX... 4 - El Miedo Es El Camino"
            " Hacia El Lado Oscuro, El Miedo Lleva A La Ira, La Ira Lleva Al Odio, El Odio Lleva Al"
            " Sufrimiento... 5 - Yo He Visto Cosas Que Vosotros No Creeriais. Atacar Naves En"
            " Llamas Mas Alla De Orion. He Visto Rayos-C Brillar En La Oscuridad Cerca De La Puerta"
            " De Tannhauser. Todos Esos Momentos Se Perderan En El Tiempo, Como Lagrimas En La"
            " Lluvia. Es Hora De Morir..."
        ),
        "-metadata",
        "title=M8AX - Fichero De Texto - " + frase,
        "-y",
        "-c:v",
        "hevc_amf",
        "-c:a",
        "aac",
        "M8AX-Mecanografía.Mp4",
    ]
)

os.remove("M8AX-Mecanografía-SA.Mp4")
pcentaj = round((cuenta * 100) / caratot, 3)
speed = round(cuenta / (time.time() - tiembarra), 3)
speed2 = round((fiche) / (time.time() - tiembarra), 3)

print(
    f"\n... Trabajo Realizado. Tiempo De Proceso - {segahms(time.time()-tiembarra)} ...\n\n... Imágenes Creadas - {fiche} Imágenes ...\n\n... Se Han Metido En Las Imágenes {cuenta} Caracteres, De Un Total De {caratot}, Un {pcentaj}% Del Texto ...\n\n... Velocidad De Proceso - {speed} Caracteres Por Segundo ...\n\n... Velocidad De Proceso - {speed2} Ficheros De Imágen Por Segundo ..."
)
print(
    f"\n... http://youtube.com/m8ax ...\n\n... By M8AX ...\n\n... Fin Del Programa ..."
)
print(f"\n... Reproduciendo El Video Resultante ...\n")
call(
    [
        "ffplay",
        "-stats",
        "-loop",
        "0",
        "M8AX-Mecanografía.Mp4",
    ]
)