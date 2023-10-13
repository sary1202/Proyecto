import unittest
import os,PIL

from src.Proyecto_python2.images import showImageFromURL, downloadImageFromUrl,grayScaleImage
from src.Proyecto_python2.myemail import sendQuickMail,sendAttachEmail

class TestProyecto(unittest.TestCase):


    def test_url(self):

        url = "https://images4.alphacoders.com/132/1327987.png"

        showImageFromURL(url)
        self.assertIsNotNone(url)


    def test_verificar_descarga_img(self):

        url = "https://images4.alphacoders.com/132/1327987.png"
        ruta = "imagen1.jpg"
        downloadImageFromUrl(url,ruta)
        self.assertTrue(os.path.exists(ruta))

    def test_imagen_blanco_y_negro(self):

        ruta = "e.jpg"
        grayScaleImage(ruta)
        self.assertTrue(os.path.exists(ruta))


    def test_SendQuikEmail(self):

        asunto = "Prueba Unitaria-QuikEmail"
        mensaje = "Esto es una prueba desde Python"
        destino = "s.ary02@hotmail.com"
        respuesta = sendQuickMail(asunto,mensaje,destino)
        respuesta_esperada = {}
        
        self.assertEqual(respuesta,respuesta_esperada)

    def test_SendAttachEmail(self):

        asunto = "Prueba Unitaria-AttachEmail"
        mensaje = "Esto es una prueba desde Python"
        destino = "s.ary02@hotmail.com"
        adjunto = "paisaje.jpg"
        respuesta = sendAttachEmail(asunto,mensaje,destino,adjunto)
        respuesta_esperada = {}
        
        self.assertEqual(respuesta,respuesta_esperada)
    


if __name__ == "__main__":
    unittest.main()