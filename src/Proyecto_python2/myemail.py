
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mimetypes import MimeTypes
from email.mime.base import MIMEBase
from email import encoders


def sendQuickMail(subject:str, message:str, destination:str):
    """
    Envía un correo electrónico rápido al destino indicado.

    Arguments:
    ^^^^^^^^^^
    :subject argumento 1: Sirve para indicar el asunto del correo

    :type argumento 1: str

    :message argumento 2: Sirve para indicar el mensaje del correo

    :type argumento 2: str

    :destination argumento 3: Sirve para indicar la dirección a la que se va a enviar el correo 
    
    :type argumento 3: str

    Uso
    ^^^

    .. code-block:: python
    
        sendQuickMail(subject, message, destination)
        
    
    """

    context = ssl.create_default_context()

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
        


def sendAttachEmail(subject:str, message:str, destination:str, path:str):
    """
    Envía un correo electrónico con un archivo adjunto a la dirección indicada.

    Arguments:
    ^^^^^^^^^^
    :subject argumento 1: Sirve para indicar el asunto del correo

    :type argumento 1: str

    :message argumento 2: Sirve para indicar el mensaje del correo

    :type argumento 2: str

    :destination argumento 3: Sirve para indicar la dirección a la que se va a enviar el correo

    :type argumento 3: str

    :path argumento 4: Sirve para indicar la ruta del archivo que desea adjuntar al correo
    
    :type argumento 4: str  

    Uso
    ^^^

    .. code-block:: python
    
        sendAttachEmail(subject, message, destination, path)

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
