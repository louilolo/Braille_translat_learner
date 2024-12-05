import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte
from alinhar import alinhar_pontos_braille
from deenhar_centroids import desenhar_centroides
from grade import grid_appl
from process_grid import processGrid
from transformar import transformarImagem
from vcol import verificao
from vect_centroid import centroid_vect

from skimage import img_as_ubyte
def main():

    # Carregar imagem
    image = io.imread('tratamento_imagem-main/tratamento_imagem-main/imagesTratadas/im 0.jpg', as_gray=True)
    # Supondo que filtered_image seja a imagem que você quer salvar

    # Aplicar filtro de contraste e remoção de ruído
    filtered_image = filters.gaussian(image, sigma=1)
    filtered_image_uint8 = img_as_ubyte(filtered_image)  # Converte para uint8
    io.imsave('filtered_image.png', filtered_image_uint8)
# Salvar imagem processada para aplicar OCR
    escala_de_cinza_processada3, imagem_limiarizada= transformarImagem(filtered_image_uint8)
    centroids, cx , cy, contornos = centroid_vect(escala_de_cinza_processada3)
    print(type(escala_de_cinza_processada3))
    
    nova_imagem_centroides = desenhar_centroides(centroids, escala_de_cinza_processada3.shape)
    print(type(nova_imagem_centroides))
    
    correcao_geometrica = alinhar_pontos_braille(centroids, nova_imagem_centroides)
    cv2.imshow("passou?", nova_imagem_centroides)
    #remove a primeira linha pois ele retorna o centroid da imagem.
    cx.remove(cx[0])
    cy.remove(cy[0])
    centroids.remove(centroids[0])

    #ordenar as listas com os valores de X e Y (crescente)
    cx.sort(reverse=False)
    cy.sort(reverse=False)
    VLine, VCol, imagem_com_grade = grid_appl(image, cy, cx, nova_imagem_centroides)    
    # Desenhar os contornos na imagem original
    imagem_contornos = image.copy()
    cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2)
    
    VCol = verificao(VLine, VCol, centroids)
    texto = processGrid(VCol=VCol, VLine=VLine, centroids=centroids, imagem=imagem_com_grade)
    print(texto)
    # Aplicar filtro de contraste e remoção de ruído
    
    # Exibir a imagem original, a imagem processada e a imagem com contornos
    cv2.imshow("Imagem Original", image)
    cv2.imshow("Filtros", filtered_image)
    cv2.imshow("Correcão Geometrica", correcao_geometrica)
    cv2.imshow("Contornos", imagem_contornos)
    cv2.imshow("Rotated", imagem_limiarizada)
    cv2.imshow("Grade", imagem_com_grade)
    

    # cv2.imshow("Imagem Processada", imagem_limiarizada)
    # cv2.imshow("Imagem com Centroides", nova_imagem_centroides)
    # cv2.imshow("Imagem com Contornos", imagem_contornos)
    cv2.waitKey(0)


transformarImagem("C:\\Users\\louis\\OneDrive\\Documentos\\GitHub\\Braille_translat_learner\\tratamento_imagem-main\\tratamento_imagem-main\\imagesTratadas\\im 1.jpg") #imagens braille/WhatsApp Image 2022-11-03 at 14.43.13 (6).jpeg