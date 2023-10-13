.. Proyecto documentation master file, created by
   sphinx-quickstart on Thu Oct 12 06:41:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenidos a la documentacion de mi Proyecto
=============================================

***********
Instalación
***********

.. code-block:: python

   pyhon -m venv env
   env\Scripts\activate 
   pip install -r python venv venv 


Para importarlo debe importar las funciones al inicio de su modulo 

.. code-block:: python

   from src.Proyecto_python2.images import showImageFromURL, downloadImageFromUrl,grayScaleImage
   from src.Proyecto_python2.myemail import sendQuickMail,sendAttachEmail


****
Usos
****
Esta biblioteca tiene dos modulos:

1. Images 

    *  showImageFromURL(url)
    * downloadImageFromUrl(url, path)
    * grayScaleImage(path:str)

2. Myemail 

    * sendQuickMail(subject, message, destination)
    * sendAttachEmail(subject, message, destination, path)

***********
Referencias
***********

Para ve el código fuente vaya al epositorio de `Github`_.
.. _`Github`: https://github.com/sary1202/Proyecto


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   modules 



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
