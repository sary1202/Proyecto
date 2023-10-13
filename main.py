import sys
import PIL
from src.Proyecto_python2.images import showImageFromURL, downloadImageFromUrl,grayScaleImage
from src.Proyecto_python2.myemail import sendQuickMail,sendAttachEmail

def main(args):
    """
    Esta función es para hacer pruebas de la biblioteca
    """

    print("función: showImageFromURL")
    url = input("Ingrese ruta: ")
    showImageFromURL(url)

    input("Pulse enter para continuar:")
    print("función: downloadImageFromUrl")
    url = input("url: ")
    ruta = input("ruta: ")
    downloadImageFromUrl(url,ruta)

    input("Pulse enter para continuar:")
    print("función: grayScaleImage")
    ruta = input("Ingrese la ruta de la imagen: ")
    grayScaleImage(ruta)


    input("Pulse enter para continuar:")
    print("función: sendQuickMail")
    asunto = input("Digite el asunto del correo: ")
    mensaje = input("Digite el mensaje del correo: ")
    destino = input("Digite la cuenta de destino a la que va a enviar correo: ")
    sendQuickMail(asunto,mensaje,destino)

    input("Pulse enter para continuar:")
    print("función: sendQuickMail")
    asunto = input("Digite el asunto del correo: ")
    mensaje = input("Digite el mensaje del correo: ")
    destino = input("Digite la cuenta de destino a la que va a enviar correo: ")
    ruta_archivo = input("Digite la ruta del archivo que va a enviar por correo: ")
    sendAttachEmail(asunto,mensaje,destino,ruta_archivo)



if __name__ == "__main__":    
    main(sys.argv)