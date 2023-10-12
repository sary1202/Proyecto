# 1 -------------------------------------------------

from PIL import Image
import requests

def showImageFromURL(url:str):
    """
    Descarga una imagen desde una URL y la muestra
    """
    with Image.open(requests.get(url, stream=True).raw) as img:
        img.show()
    print("Se ha descargado mostrado la imagen correctamente")




# 2 -------------------------------------------------

import requests
from PIL import Image

def downloadImageFromUrl(url:str, path:str):
    """
    Descarga una imagen y la guarda en la ruta indicada
    """
    respuesta = requests.get(url)
    
    with open(path, mode="wb") as imagen: # Se abre la ruta en modo escritura y binario para definir el nombre
        imagen.write(respuesta.content)
    print("Se ha descargado la imagen correctamente")



# 3 -------------------------------------------------

from PIL import Image


def grayScaleImage(path:str):
    """
    Convierte una imagen a blanco y negro
    """
    with Image.open(path) as p:
        s = p.convert("L")
        s.save(path)
    print("Se guardo la imagen a blanco y negro")


