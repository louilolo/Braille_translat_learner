import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
def desenhar_centroides(centroids, shape):
    # Criar uma imagem em branco
    nova_imagem = np.ones(shape, dtype=np.uint8) * 0  # Fundo branco
    
    # Definir o raio do círculo
    raio = 3
    #chamar aqui a rotacionar!
    #salvar imagem!
    # Desenhar um círculo preto em cada centróide
    for centroide in centroids:
        cv2.circle(nova_imagem, tuple(centroide[::-1]), raio, (1, 1, 1), -1,)  # Inverte a ordem (y, x) para (x, y) 
        # verificar
    cv2.imshow("Nova Imagemp", nova_imagem)
    io.imsave('nova_imagemp.png', nova_imagem)
    
    print(type(nova_imagem))
    return nova_imagem
