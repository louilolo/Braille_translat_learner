import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte
def centroid_vect(escala_de_cinza_processada3):
        # Encontrar contornos na imagem limiarizada
    contornos, _ = cv2.findContours(escala_de_cinza_processada3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("rodou contornos")

    centroids = []
    cx = []
    cy =[]
    for contorno in contornos:
        M = cv2.moments(contorno)
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        cx.append(x)
        cy.append(y)
        print("ta infinita essa prr")
        centroids.append([y,x]) #linha, coluna
    print("rodou vect_centroid")
    return centroids , cx, cy, contornos