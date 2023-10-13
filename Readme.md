# Proyecto del curso

## Instalación

Para instalar el paquete es necesario crear un entorno virtual:

```
python -m venv env
env\Scripts\Activate
pip install -r python venv venv 
```

Para poder utilizarlo solo debe importar las funciones al inicio del módulo:

```python
from src.Proyecto_python2.images import showImageFromURL, downloadImageFromUrl,grayScaleImage
from src.Proyecto_python2.myemail import sendQuickMail,sendAttachEmail
```


## Usos

Esta biblioteca cuenta con dos módulos:

* Images
    
    1. showImageFromURL(url)
    2. downloadImageFromUrl(url, path)
    3. grayScaleImage(path:str)

* Myemail

    1. sendQuickMail(subject, message, destination)
    2. sendAttachEmail(subject, message, destination, path)

## Referencias

Para ver el código fuente debe seleccionar el siguiente enlace [Github](https://github.com/sary1202/Proyecto)

