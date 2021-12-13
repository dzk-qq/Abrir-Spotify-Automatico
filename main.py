import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import time

pyautogui.FAILSAFE = False

iconoSpotify = './referencias/abrir.png'
iconoSpotifyA = './referencias/abierto.png'
comprobarSpotify = './referencias/comp1.png'
comprobarSpotify2 = './referencias/comp2.png'


def abrirSpotifyLoop():
    while True:
        pos = imagesearch(iconoSpotify, 0.5)
        if not pos[0] == -1:
            time.sleep(1)
            pyautogui.doubleClick(pos[0], pos[1])
            print('Icono encontrado!')
            break
            time.sleep(1)

def comprobarApertura():
    busqueda = imagesearch(comprobarSpotify)
    sonido = imagesearch(comprobarSpotify2)

    if not busqueda[0] == -1 or not sonido[0] == -1:
        return True
    else:
        return False


def main():
    abierto = True
    abrirSpotifyLoop()
    time.sleep(3)

    while abierto is True:
        comprobarApertura()
        time.sleep(1)

        while True:
            error = abrirSpotifyLoop()
            if error is True:
                print("Hubo un error")
                break

        seAbrio = comprobarApertura()
        if seAbrio is True:
            print("Se abrió correctamente!")
            time.sleep(1)
            break

if __name__ == '__main__':
    print("Buscando...")
    main()



