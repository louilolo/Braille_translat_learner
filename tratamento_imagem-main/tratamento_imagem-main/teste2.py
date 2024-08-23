import cv2
import numpy as np
import matplotlib.pyplot as plt
#IMAGEM EQUALIZADA NORMAL
# imagem = cv2.imread('imagesTratadas/im 8.jpg', cv2.IMREAD_GRAYSCALE)

# equalizador = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# imagem_equalizada = equalizador.apply(imagem)

# imagem_limiarizada = cv2.threshold(imagem_equalizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# # Exibir as imagens original e equalizada
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(imagem_limiarizada, cmap='gray')
# plt.title('Imagem Limiar')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(imagem_equalizada, cmap='gray')
# plt.title('Imagem Equalizada')
# plt.axis('off')

# plt.show()


# # Carregar a imagem em tons de cinza
# imagem = cv2.imread('imagesTratadas/im 8.jpg', cv2.IMREAD_GRAYSCALE)

# # Calcular o histograma da imagem
# hist, bins = np.histogram(imagem.flatten(), 256, [0, 256])

# # Calcular a função de distribuição acumulada (CDF)
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max() / cdf.max()

# # Equalizar o histograma
# imagem_equalizada = np.interp(imagem.flatten(), bins[:-1], cdf_normalized)

# # Remodelar a imagem equalizada
# imagem_equalizada = imagem_equalizada.reshape(imagem.shape)

# # Exibir as imagens original e equalizada
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(imagem, cmap='gray')
# plt.title('Imagem Original')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(imagem_equalizada, cmap='gray')
# plt.title('Imagem Equalizada')
# plt.axis('off')

# plt.show()




import cv2
import numpy as np

# Função para calcular a inclinação média dos pontos
def calcular_inclinacao_media(centroids):
    # Calcular a média das diferenças entre as coordenadas y dos pontos
    deltas_y = np.diff([p[0] for p in centroids])
    inclinacao_media_rad = np.arctan(np.mean(deltas_y))
    inclinacao_media_graus = np.degrees(inclinacao_media_rad)
    return inclinacao_media_graus

# Função para desenhar os centroides alinhados
def desenhar_centroides_alinhados(centroids, shape):
    # Calcular a inclinação média dos centroides
    inclinacao_media = calcular_inclinacao_media(centroids)
    
    # Criar uma imagem em branco
    nova_imagem = np.ones(shape, dtype=np.uint8) * 255  # Fundo branco
    
    # Definir o raio do círculo
    raio = 4
    
    # Desenhar um círculo preto em cada centróide alinhado
    for centroide in centroids:
        # Calcular as coordenadas do centróide alinhado
        x, y = centroide
        x_alinhado = int(x * np.cos(np.radians(-inclinacao_media)) - y * np.sin(np.radians(-inclinacao_media)))
        y_alinhado = int(x * np.sin(np.radians(-inclinacao_media)) + y * np.cos(np.radians(-inclinacao_media)))
        
        # Desenhar o círculo preto na posição alinhada
        cv2.circle(nova_imagem, (y_alinhado, x_alinhado), raio, (0, 0, 0), -1)
    
    return nova_imagem

# Exemplo de uso
centroids = [[10, 20], [30, 40], [50, 60]]  # Lista de centroides de exemplo
shape = (100, 100)  # Formato da imagem de exemplo

# Desenhar os centroides alinhados
imagem_com_centroides_alinhados = desenhar_centroides_alinhados(centroids, shape)

# Exibir a imagem resultante
cv2.imshow("Imagem com Centroides Alinhados", imagem_com_centroides_alinhados)
cv2.waitKey(0)
cv2.destroyAllWindows()
