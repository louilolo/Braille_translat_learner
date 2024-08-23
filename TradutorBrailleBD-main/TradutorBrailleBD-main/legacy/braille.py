# -*- coding: utf-8 -*-

import cv2 as cv

# import numpy as np;
# from builtins import len
# import bdLetra
# from sklearn.metrics import DistanceMetric

# def verificao(VLine, VCol, centroids):
#     for j in range(1):  #Coluna
#         #print(VCol[j:j+3])
#         remCol = [0];
#         for i in range(0,len(VLine)-3,3):  #linha
#             #print(VLine[i:i+4])

#             vLetras = [0,0,0,0,0,0]
#             vCent = [0,0,0,0,0,0]
#             cnt = 0

#                 #retira a sub_imagem
#             img = thresh[VLine[i]:VLine[i+3],VCol[j]:VCol[j+2]] #não precisa

#             for n in range(2): #Coluna
#                 '''print(VCol[n])
#                 print(VCol[n+1])
#                 print("")'''
#                 for m in range(3): #linha
#                     '''print(VLine[i+m])
#                     print(VLine[(i+m)+1])'''

#                     for k in range(len(centroids)):
#                         if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[n]
#                            and centroids[k][1] <= VCol[n+1]):
#                             vLetras[cnt] = 1
#                             vCent[cnt] = k
#                             #print(VCol[m],VLine[n])
#                             #print("")
#                     cnt = cnt+1

#             #[carac, flag] = bdLetra.bdLetra(vLetras, flag)
#             print(vLetras)
#             dist = DistanceMetric.get_metric('euclidean')
#             if(vLetras[0] == vLetras[2] and vLetras[0] != vLetras[1]):
#                 r1=0
#                 r2=0
#                 r3=0
#                 r4=0
#                 if(vLetras[0] == vLetras[3]):
#                     X = [ centroids[vCent[0]], centroids[vCent[3]] ]
#                     r1 = dist.pairwise(X)[0][1]
#                     print(r1)

#                 if(vLetras[2] == vLetras[5]):
#                     X = [ centroids[vCent[2]], centroids[vCent[5]] ]
#                     r2 = dist.pairwise(X)[0][1]
#                     print(r2)

#                 if(vLetras[0] == vLetras[4]):
#                     X = [ centroids[vCent[0]], centroids[vCent[4]] ]
#                     r3 = dist.pairwise(X)[0][1]
#                     print(r3)

#                 if(vLetras[2] == vLetras[4]):
#                     X = [ centroids[vCent[2]], centroids[vCent[4]] ]
#                     r4 = dist.pairwise(X)[0][1]
#                     print(r4)

#                 if(r1 >= 12 or r2 >= 12 or r3 >= 14 or r4 >=14 ):
#                     remCol.append(1)
#                 else:
#                     remCol.append(0)

#     if(np.max(remCol) == 1):
#         VCol.remove(VCol[0])

#     return VCol


# #principal
# VCol = [17, 25, 38, 46, 58, 66, 79, 86, 99, 107, 120, 128, 141, 148, 161, 169, 182, 189, 202, 210, 222, 231, 243, 251, 264, 272, 285, 292, 305, 313, 325, 333, 346, 354, 366, 375, 387, 395, 408, 416, 428, 436, 449, 457, 469, 478]
# VLine = [12, 20, 28, 36, 68, 76, 84, 115, 122, 130]
# centroids = []
# cx = [96, 21, 322, 261, 240, 219, 207, 165, 157, 137, 301, 268, 165, 137, 117, 83, 63, 42, 321, 260, 248, 103, 34, 22, 330, 309, 281, 260, 240, 227, 219, 207, 158, 137, 124, 104, 96, 75, 62, 55, 54, 329, 199, 178, 157, 137, 75, 34, 21, 445, 425, 363, 137, 96, 62, 55, 34, 404, 371, 363, 343, 288, 268, 206, 198, 186, 157, 124, 83, 474, 445, 425, 0, 178, 145, 116, 103, 96, 75, 54, 42, 34, 21, 466, 425, 384, 363, 342, 281, 268, 260, 219, 198, 165, 446, 412, 247, 116, 95, 82, 75, 54, 21, 445, 425, 383, 363, 309, 239, 186, 453, 371, 350, 329, 322, 260, 240, 206, 144, 137, 124, 103, 54, 474, 433, 425, 404, 391, 383, 185, 116, 103, 96, 75, 54, 34, 21, 383, 362, 342, 322, 309, 268, 239, 218, 206, 198, 465, 445, 432, 424, 412, 371]
# cy = [127, 127, 126, 126, 126, 127, 126, 126, 126, 126, 119, 119, 119, 119, 119, 119, 119, 119, 118, 119, 118, 119, 112, 112, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 112, 82, 81, 81, 81, 81, 81, 81, 81, 81, 80, 80, 81, 74, 74, 74, 74, 74, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 72, 72, 73, 0, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 65, 65, 65, 65, 65, 66, 66, 65, 65, 65, 66, 65, 64, 33, 33, 33, 33, 33, 33, 33, 32, 32, 32, 32, 32, 32, 33, 32, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 24, 24, 24, 18, 18, 18, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 16, 16, 16, 16, 17]
# for ts in range(len(cx)):
#     centroids.append([cy[ts],cx[ts]]) #linha, coluna

# Leitura da imagem
image = cv.imread('src/sample/2.jpg')

# Filtro: Tom de Cinza
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# Filtro: Binarização
ret, thresh = cv.threshold(imgray, 230, 255, cv.THRESH_BINARY)
# Filtro: Contorno de cada ponto baille
im2, contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

"""
centroids = []
cx = []
cy =[]
for contour in contours:
    M = cv.moments(contour)
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])
    cx.append(x)
    cy.append(y)

    centroids.append([y,x]) #linha, coluna

#remove a primeira linha pois ele retorna o centroid da imagem.
cx.remove(cx[0])
cy.remove(cy[0])
centroids.remove(centroids[0])

#ordenar as listas com os valores de X e Y (crescente)
cx.sort(reverse=False)
cy.sort(reverse=False)


# inserir grade coluna
limiar_gride = 4;
cor = 200
VCol = []

cv.line(thresh,(cx[0]-limiar_gride, 0), (cx[0]-limiar_gride,thresh.shape[0]),cor)
VCol.append(cx[0]-limiar_gride)
p_aux = 0;
for i in range(len(cx)):
    if(cx[i] >= (p_aux+limiar_gride)): 
        cv.line(thresh,(cx[i]+limiar_gride, 0), (cx[i]+limiar_gride,thresh.shape[0]),cor)
        p_aux = cx[i]
        VCol.append(cx[i]+limiar_gride)

# inserir grade linha
VLine = []
cv.line(thresh,(0, cy[0]-limiar_gride), (thresh.shape[1],cy[0]-limiar_gride),cor)
VLine.append(cy[0]-limiar_gride)
p_aux = 0;
for i in range(len(cy)):
    if(cy[i] >= (p_aux+limiar_gride)): 
        cv.line(thresh,(0, cy[i]+limiar_gride), (thresh.shape[1],cy[i]+limiar_gride),cor)
        p_aux = cy[i]
        VLine.append(cy[i]+limiar_gride)

"""

# VCol = verificao(VLine, VCol, centroids)

# #busca Cela
# flag = 0
# verf = 0
# #num = 0
# for i in range(0,len(VLine)-3,3):  #linha
#     #print(VLine[i:i+4])
#     for j in range(0,len(VCol)-2,2):  #Coluna
#         #print(VCol[j:j+3])
#         vLetras = [0,0,0,0,0,0]
#         cnt = 0;
#         #retira a sub_imagem
#         img = thresh[VLine[i]:VLine[i+3],VCol[j]:VCol[j+2]] #NÃO PRECISA

#         for n in range(2): #Coluna
#             '''print(VCol[j+n])
#             print(VCol[(j+n)+1])'''
#             for m in range(3): #linha
#                 '''print(VLine[i+m])
#                 print(VLine[(i+m)+1])
#                 print("")'''
#                 for k in range(len(centroids)):
#                         if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[j+n] and centroids[k][1] <= VCol[(j+n)+1]):
#                             vLetras[cnt] = 1
#                             #print(VCol[m],VLine[n])
#                             #print("")
#                 cnt = cnt+1
#         [carac, flag] = bdLetra.letra_bd(vLetras, flag)
#         #[carac, flag, num] = bdLetra.bdLetra(vLetras, flag, num)
#         print(carac)
#     print("")
# print("")


""" #busca inversa
#busca Cela
flag = 0
for i in range(0,len(VLine)-3,3):  #linha
    #print(VLine[i:i+4])
            
    for j in range(len(VCol)-1,2,-2):  #Coluna
        #print(VCol[j-2:j+1])

        vLetras = [0,0,0,0,0,0]
        cnt = 0;
        
        #retira a sub_imagem        
        img = thresh[VLine[i]:VLine[i+3],VCol[j-2]:VCol[j]]
        
        for n in range(2,0,-1): #Coluna
            #print(VCol[j-n])
            #print(VCol[j-(n-1)])
      
            for m in range(3): #linha
                #print(VLine[i+m])
                #print(VLine[(i+m)+1])
                #print("")       
   
                for k in range(len(centroids)):
                        if(centroids[k][0] >= VLine[i+m] and centroids[k][0] <= VLine[(i+m)+1] and  centroids[k][1] >= VCol[j-n] and centroids[k][1] <= VCol[j-(n-1)]):                    
                            vLetras[cnt] = 1
                            #print(VCol[m],VLine[n])
                            #print("")
                cnt = cnt+1                

        [carac, flag] = bdLetra.bdLetra(vLetras, flag)
        print(carac)
    print("")
      

"""


"""
        #retira a sub_imagem        
        img = thresh[VLine[i]:VLine[i+3],VCol[j-2]:VCol[j]]
        
        #desenhar um retagulo
        cv.rectangle(thresh,(VCol[j-2],VLine[i]), (VCol[j],VLine[i+3]), 50 )
"""
"""        cv.imshow("original",thresh)
        cv.imshow("subimag",img)
        cv.waitKey();"""


"""  
    #print(cv.boundingRect(contour))

#derp,contours,hierarchy = cv.findContours(imageSeg,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(thresh, contours, -1, (0,255,0), 1)

for contour in contours:
    print(cv.boundingRect(contour))

print(thresh.shape)

cv.imshow("subs",thresh)
cv.waitKey(0);
"""
