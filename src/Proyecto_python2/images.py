from PIL import Image
import requests

def showImageFromURL(url:str):
    """
    Descarga una imagen desde una URL y la muestra

    Arguments:
    ^^^^^^^^^^
    :url argumento 1: Sirve para ingresar la imagen de la url a mostar

    :type argumento 1: str

    Uso
    ^^^

    .. code-block:: python

        showImageFromURL(url)


    
    """
    with Image.open(requests.get(url, stream=True).raw) as img:
        img.show()
    print("Se ha descargado mostrado la imagen correctamente")



def downloadImageFromUrl(url:str, path:str):
    """
    Descarga una imagen y la guarda en la ruta indicada

    Arguments:
    ^^^^^^^^^^
    :url argumento 1: Sirve para ingresar la imagen de la url a mostar

    :type argumento 1: str

    :path argumento 2: Sirve para indicar la ruta donde se va a descargar la imagen

    :type argumento 2: str

    Uso
    ^^^

    .. code-block:: python

        downloadImageFromUrl(url, path)

    """
    respuesta = requests.get(url)
    
    with open(path, mode="wb") as imagen: # Se abre la ruta en modo escritura y binario para definir el nombre
        imagen.write(respuesta.content)
    print("Se ha descargado la imagen correctamente")



def grayScaleImage(path:str):
    """
    Convierte una imagen a blanco y negro

    Arguments:
    ^^^^^^^^^^
    :path argumento 1: Reconoce la ruta de la imagen a editar
    
    :type argumento 1: str

    Uso
    ^^^

    .. code-block:: python
    
        grayScaleImage(path:str)

         

    """
    with Image.open(path) as p:
        s = p.convert("L")
        s.save(path)
    print("Se guardo la imagen a blanco y negro")


