def desenhar_centroides(centroids, shape):
    # Criar uma imagem em branco
    nova_imagem = np.ones(shape, dtype=np.uint8) * 255  # Fundo branco
    
    # Definir o raio do círculo
    raio = 3
    
    # Desenhar um círculo preto em cada centróide
    for centroide in centroids:
        cv2.circle(nova_imagem, tuple(centroide[::-1]), raio, (0, 0, 0), -1)  # Inverte a ordem (y, x) para (x, y)
    cv2.imshow("Nova Imagemp", nova_imagem)
    io.imsave('nova_imagemp.png', nova_imagem)
    print(type(nova_imagem))
    return nova_imagem
