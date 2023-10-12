
####-----------------------------------------------

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendQuickMail(subject:str, message:str, destination:str):
    """
    Envía un correo electrónico rápido al destino indicado.
    La función debe preguntar cual es el correo electrónico con el que se enviará así
    como su contraseña
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com
    """

    context = ssl.create_default_context()

    # Se genera mensaje preferible hacerlo antes del wtih
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject
#   mensaje["From"] = input("ingrese la cuenta con la que va a enviar el correo")
    mensaje["To"] = destination

    texto = message # se define cuerpo del correo

    cuerpo_texto = MIMEText(texto, "plain") # se llama al cuarpo del correo

    mensaje.attach(cuerpo_texto)

    cuenta_origen = input("Ingrese la cuenta con la que va a enviar el correo: ")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(cuenta_origen, input("Ingrese la contraseña para enviar el correo: "))

        return server.sendmail(cuenta_origen,
            destination,
            mensaje.as_string()
            )
        









# 2-----------------------------------------------------

import smtplib, ssl
from mimetypes import MimeTypes

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def sendAttachEmail(subject:str, message:str, destination:str, path:str):
    """
    Envía un correo electrónico rápido al destino indicado.
    La función debe preguntar cual es el correo electrónico con el que se enviará así
    como su contraseña
    Se utilizará el puerto 587 y se utilizará TLS
    Se utilizará el servidor de correo smtp.gmail.com
    """

    context = ssl.create_default_context()

    # Se genera mensaje preferible hacerlo antes del wtih
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject
#   mensaje["From"] = input("ingrese la cuenta con la que va a enviar el correo")
    mensaje["To"] = destination

    texto = message # se define cuerpo del correo
    cuerpo_texto = MIMEText(texto, "plain") # se llama al cuarpo del correo
    mensaje.attach(cuerpo_texto)

    ruta_archivo = path

    adjunto = MIMEBase("application", "octet-stream")
    with open(ruta_archivo, "rb") as attachment:
        adjunto.set_payload(attachment.read())
    
    encoders.encode_base64(adjunto)
    adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename={ruta_archivo}",
    )
    mensaje.attach(adjunto)

    cuenta_origen = input("Ingrese la cuenta con la que va a enviar el correo: ")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(cuenta_origen,input("Ingrese la contraseña para enviar el correo: "))
            
        return server.sendmail(cuenta_origen,
                destination,
                mensaje.as_string()
            )
