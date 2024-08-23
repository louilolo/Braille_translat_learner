# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:06:46 2020

@author: josiv
"""

import cv2
import numpy as np

# file = ("/Codigo/banco de imagem/binaria/image05.jpg")
"""
imagem = cv2.imread("image05.jpg")
cv2.imshow("Original", imagem)
cv2.waitKey(0)
"""
canvas = (
    np.ones((100, 100, 3)) * 255
)   # imagem 400x300, com fundo branco e 3 canais para as cores


# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)


# desenha a linha vertical
azul = (255, 0, 0)
#                <COL LIN> <COL LIN>
cv2.line(canvas, (25, 0), (25, 100), azul)
cv2.line(canvas, (50, 0), (50, 100), azul)
cv2.line(canvas, (75, 0), (75, 100), azul)


# desenha a linha horizontal
verde = (0, 255, 0)
#               <COL LIN> <COL LIN>
cv2.line(canvas, (0, 25), (100, 25), verde)
cv2.line(canvas, (0, 50), (100, 50), verde)
cv2.line(canvas, (0, 75), (100, 75), verde)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)


def sub_imagem(image, Lin, Lfin, Cin, Cfin):
    imageSub = np.zeros((Lfin - Lin, Cfin - Cin))
    n = 0
    m = 0
    for i in range(Lin, Lfin):
        for j in range(Cin, Cfin):
            imageSub[m][n] = image[i, j]
            n = n + 1
        m = m + 1
        n = 0


for i in range(0, len(index_lin) - 3, 3):   # VLine
    for j in range(0, len(index_col) - 2, 2):   # VCol
        sub_imagem(
            imageSeg,
            index_lin[i],
            index_lin[i + 3],
            index_col[j],
            index_col[j + 2],
        )   # ImgSeg: Após binarização - thresh

    for i in range(0, len(index_lin) - 3, 3):
        for j in range(0, len(index_col) - 2, 2):

            vLinha = index_lin[
                i : i + 4
            ]  # vais ter que adaptar, pois aqui já pego o vetor
            vColuna = index_col[
                j : j + 3
            ]   # vais ter que adaptar, pois aqui já pego o vetor
            vLetras = [0, 0, 0, 0, 0, 0]
            cnt = 0
            flag = 0
            for m in range(len(vColuna) - 1):
                for n in range(len(vLinha) - 1):
                    img = imageSeg[
                        vLinha[n] : vLinha[n + 1], vColuna[m] : vColuna[m + 1]
                    ]

                    for k in range(len(centroids)):
                        if (
                            centroids[k][0] >= vColuna[m]
                            and centroids[k][0] <= vColuna[m + 1]
                            and centroids[k][1] >= vLinha[n]
                            and centroids[k][1] <= vLinha[n + 1]
                        ):
                            vLetras[cnt] = 1
                    cnt = cnt + 1

            # recupera a letra na base de letras (esse passo deixa para depois)
            [carac, flag] = bdLetra.bdLetra(vLetras, flag)
            print('Letra: ', carac)
