import cv2
import os
import numpy as np
from sklearn.metrics import DistanceMetric
from builtins import len
import bdLetra
from skimage import io, filters, img_as_ubyte

from skimage import img_as_ubyte



# Carregar imagem
image = io.imread('tratamento_imagem-main/tratamento_imagem-main/imagesTratadas/im 0.jpg', as_gray=True)
# Supondo que filtered_image seja a imagem que você quer salvar

# Aplicar filtro de contraste e remoção de ruído
filtered_image = filters.gaussian(image, sigma=1)
filtered_image_uint8 = img_as_ubyte(filtered_image)  # Converte para uint8
io.imsave('filtered_image.png', filtered_image_uint8)
# Salvar imagem processada para aplicar OCR
def correcao_geometrica(imagem):
    # Obter as dimensões da imagem original
    altura, largura = imagem.shape[:2]
    
    # Definir pontos de referência na imagem original e na imagem de destino
    pontos_origem = np.float32([[0, 0], [largura, 0], [0, altura], [largura, altura]])
    pontos_destino = np.float32([[0, 0], [largura, 0], [0, altura], [largura, altura]])
    
    # Calcular a matriz de transformação
    matriz_transformacao = cv2.getPerspectiveTransform(pontos_origem, pontos_destino)
    
    # Aplicar a transformação de perspectiva
    imagem_corrigida = cv2.warpPerspective(imagem, matriz_transformacao, (largura, altura))
    
    return imagem_corrigida

def verificao(VLine, VCol, centroids):
    for _ in range(1):  #Coluna
        remCol = [0]   
        for i in range(0,len(VLine)-3,3):  #linha                         
            vLetras = [0,0,0,0,0,0]
            vCent = [0,0,0,0,0,0]
            cnt = 0
                
            for n in range(2): #Coluna
                for m in range(3): #linha
                    for k in range(len(centroids)):
                        if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[n] 
                           and centroids[k][1] <= VCol[n+1]):                    
                            vLetras[cnt] = 1
                            vCent[cnt] = k
                    cnt = cnt+1                

            dist = DistanceMetric.get_metric('euclidean')
            if(vLetras[0] == vLetras[2] and vLetras[0] != vLetras[1]):
                r1=0 
                r2=0 
                r3=0 
                r4=0 
                if(vLetras[0] == vLetras[3]):    
                    X = [ centroids[vCent[0]], centroids[vCent[3]] ]
                    r1 = dist.pairwise(X)[0][1]
                    
                if(vLetras[2] == vLetras[5]):    
                    X = [ centroids[vCent[2]], centroids[vCent[5]] ]
                    r2 = dist.pairwise(X)[0][1]
                    
                if(vLetras[0] == vLetras[4]):    
                    X = [ centroids[vCent[0]], centroids[vCent[4]] ]
                    r3 = dist.pairwise(X)[0][1]

                if(vLetras[2] == vLetras[4]):    
                    X = [ centroids[vCent[2]], centroids[vCent[4]] ]
                    r4 = dist.pairwise(X)[0][1]
                    
                if(r1 >= 12 or r2 >= 12 or r3 >= 14 or r4 >=14 ):#parametrizar
                    remCol.append(1)
                else:
                    remCol.append(0)
    
    if(np.max(remCol) == 1):
        VCol.remove(VCol[0])

    return VCol

def processGrid(centroids,VLine,VCol,imagem):
    # Buscar Cela
    flag = 0
    text = ''
    
    for i in range(0,len(VLine)-3,3):  # Linha
        for j in range(0,len(VCol)-2,2):  # Coluna
            vLetras = [0,0,0,0,0,0]
            cnt = 0      
            
            # Retira a sub_imagem        
            sub_img = imagem[VLine[i]:VLine[i+3], VCol[j]:VCol[j+2]]
            # Verifica se a sub_imagem é válida
            if sub_img.size == 0:
                cv2.imshow("sub imagem", sub_img)
                continue
                    
            for n in range(2): # Coluna
                for m in range(3): # Linha
                    for k in range(len(centroids)):
                            if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[j+n] and centroids[k][1] <= VCol[(j+n)+1]):                    
                                vLetras[cnt] = 1
                    cnt = cnt + 1
                
            [carac, flag] = bdLetra.bdLetra(vLetras, flag)
            text += carac
    
    return text

def desenhar_centroides(centroids, shape):
    # Criar uma imagem em branco
    nova_imagem = np.ones(shape, dtype=np.uint8) * 255  # Fundo branco
    
    # Definir o raio do círculo
    raio = 3
    
    # Desenhar um círculo preto em cada centróide
    for centroide in centroids:
        cv2.circle(nova_imagem, tuple(centroide[::-1]), raio, (0, 0, 0), -1)  # Inverte a ordem (y, x) para (x, y)
    
    return nova_imagem

def transformarImagem(img):
    # Ler a imagem
    imagem = cv2.imread(img)
    if not os.path.exists(img):
        print(f"Arquivo não encontrado: {img}")
        return

    # altura, largura, canais = imagem.shape
    
    # Converter para escala de cinza
    escala_de_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    #Implementar correção geometrica
    geoCorrigida = correcao_geometrica(escala_de_cinza)
            
    # Aplicar limiarização binária
    # limiarizada = cv2.adaptiveThreshold(escala_de_cinza_suavizada1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 2)
    ret, imagem_limiarizada = cv2.threshold(geoCorrigida, 215, 255, cv2.THRESH_BINARY)
    cv2.imshow("Rotated", imagem_limiarizada)

    
    #Filtro media
    #media = cv2.blur(imagem_limiarizada, (3, 3))
    mediana = cv2.medianBlur(imagem_limiarizada, 3)

    # Aplicar erosão e dilatação para remover pequenos ruídos e preencher lacunas
    kernel = np.ones((3, 3), np.uint8)
    escala_de_cinza_processada = cv2.erode(mediana, kernel, iterations=1)
    escala_de_cinza_processada = cv2.dilate(escala_de_cinza_processada, kernel, iterations=1)

    escala_de_cinza_processada = cv2.medianBlur(escala_de_cinza_processada, 3)
    cv2.imshow("escala de cinza", escala_de_cinza_processada)
    
    # Encontrar contornos na imagem limiarizada
    contornos, _ = cv2.findContours(escala_de_cinza_processada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    

    centroids = []
    cx = []
    cy =[]
    for contorno in contornos:
        M = cv2.moments(contorno)
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        cx.append(x)
        cy.append(y)

        centroids.append([y,x]) #linha, coluna
    

    #criar nova imagem com os centroides achados
    nova_imagem_centroides = desenhar_centroides(centroids, escala_de_cinza.shape)

    escala_de_cinza_processada = nova_imagem_centroides

    #remove a primeira linha pois ele retorna o centroid da imagem.
    cx.remove(cx[0])
    cy.remove(cy[0])
    centroids.remove(centroids[0])

    #ordenar as listas com os valores de X e Y (crescente)
    cx.sort(reverse=False)
    cy.sort(reverse=False)
    
    limiar_gride = 25
    cor = 200
    
    # Inserir grade coluna na imagem original
    imagem_com_grade = imagem.copy()
    VCol = []
    cv2.line(imagem_com_grade, (cx[0] - limiar_gride, 0), (cx[0] - limiar_gride, escala_de_cinza_processada.shape[0]), (0, 0, 255), 2)
    VCol.append(cx[0] - limiar_gride)
    p_aux = 0
    for i in range(len(cx)):
        if(cx[i] >= (p_aux + limiar_gride)): 
            cv2.line(imagem_com_grade, (cx[i] + limiar_gride, 0), (cx[i] + limiar_gride, escala_de_cinza_processada.shape[0]), (0, 0, 255), 2)
            p_aux = cx[i]
            VCol.append(cx[i] + limiar_gride)

    # Inserir grade linha na imagem original
    VLine = []
    cv2.line(imagem_com_grade, (0, cy[0] - limiar_gride), (escala_de_cinza_processada.shape[1], cy[0] - limiar_gride), (0, 0, 255), 2)
    VLine.append(cy[0] - limiar_gride)
    p_aux = 0
    for i in range(len(cy)):
        if(cy[i] >= (p_aux + limiar_gride)): 
            cv2.line(imagem_com_grade, (0, cy[i] + limiar_gride), (escala_de_cinza_processada.shape[1], cy[i] + limiar_gride), (0, 0, 255), 2)
            p_aux = cy[i]
            VLine.append(cy[i] + limiar_gride)
    
           
    # Desenhar os contornos na imagem original
    imagem_contornos = imagem.copy()
    cv2.drawContours(imagem_contornos, contornos, -1, (0, 255, 0), 2)
    VCol = verificao(VLine, VCol, centroids)
    texto = processGrid(VCol=VCol, VLine=VLine, centroids=centroids, imagem=escala_de_cinza_processada)
    print(texto)
    # Aplicar filtro de contraste e remoção de ruído
    
    # Exibir a imagem original, a imagem processada e a imagem com contornos
    cv2.imshow("Imagem Original", image)
    cv2.imshow("Filtros", filtered_image)
    cv2.imshow("Correção Geométrica", geoCorrigida)
    cv2.imshow("Nova Imagem", escala_de_cinza_processada)
    cv2.imshow("Contornos", imagem_contornos)
    cv2.imshow("Rotated", imagem_limiarizada)
    cv2.imshow("Grade", imagem_com_grade)
    

    # cv2.imshow("Imagem Processada", imagem_limiarizada)
    # cv2.imshow("Imagem com Centroides", nova_imagem_centroides)
    # cv2.imshow("Imagem com Contornos", imagem_contornos)
    cv2.waitKey(0)
   

transformarImagem("C:\\Users\\louis\\OneDrive\\Documentos\\GitHub\\Braille_translat_learner\\tratamento_imagem-main\\tratamento_imagem-main\\imagesTratadas\\im 1.jpg") #imagens braille/WhatsApp Image 2022-11-03 at 14.43.13 (6).jpeg 