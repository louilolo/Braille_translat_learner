
import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
def transformarImagem(img):
    # Ler a imagem
    imagem = cv2.imread(img)
    if not os.path.exists(img):
        print(f"Arquivo não encontrado: {img}")
        return 1
    else:
    # altura, largura, canais = imagem.shape
    
    # Converter para escala de cinza
        escala_de_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        
        #Implementar correção geometrica
        #geoCorrigida = correcao_geometrica(escala_de_cinza)
                
        # Aplicar limiarização binária
        cv2.adaptiveThreshold(escala_de_cinza , 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 2)
        ret, imagem_limiarizada = cv2.threshold(escala_de_cinza, 220, 255, cv2.THRESH_BINARY)
        cv2.imshow("limiarizada", imagem_limiarizada)

        
        #Filtro media
        #media = cv2.blur(imagem_limiarizada, (3, 3))
        mediana = cv2.medianBlur(imagem_limiarizada, 3)

        # Aplicar erosão e dilatação para remover pequenos ruídos e preencher lacunas
        kernel = np.ones((3, 3), np.uint8)
        escala_de_cinza_processada = cv2.erode(mediana, kernel, iterations=1)
        escala_de_cinza_processada2 = cv2.dilate(escala_de_cinza_processada, kernel, iterations=1)

        escala_de_cinza_processada3 = cv2.medianBlur(escala_de_cinza_processada2, 3)
        cv2.imshow("escala de cinza", escala_de_cinza_processada3)
    return escala_de_cinza_processada3, imagem_limiarizada