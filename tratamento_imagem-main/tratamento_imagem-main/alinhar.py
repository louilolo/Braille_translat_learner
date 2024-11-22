def alinhar_pontos_braille(centroids, imagem):
    # Aplicar Canny para detectar bordas (opcional, melhora detecção de linhas)
   # bordas = cv2.Canny(imagem, 50, 150, apertureSize=3)

    # Ordenar os pontos por coordenadas (y, x)
    centroids = sorted(centroids, key=lambda p: (p[1], p[0]))  # Ordena por y (vertical), depois por x (horizontal)

    # Critério de proximidade para considerar pontos alinhados
    threshold = 10 
    
    # Desenhar linhas verticais entre pontos alinhados
    for i in range(len(centroids) - 1):
        for j in range(i + 1, len(centroids)):
            # Se a diferença na coordenada x for pequena, os pontos estão verticalmente alinhados
            if abs(centroids[i][0] - centroids[j][0]) < threshold:
                # Desenhar linha entre esses dois pontos
                cv2.line(imagem, tuple(centroids[i]), tuple(centroids[j]), (0, 0, 255), 2)
    
    # Desenhar linhas horizontais entre pontos alinhados
    for i in range(len(centroids) - 1):
        for j in range(i + 1, len(centroids)):
            # Se a diferença na coordenada y for pequena, os pontos estão horizontalmente alinhados
            if abs(centroids[i][1] - centroids[j][1]) < threshold:
                # Desenhar linha entre esses dois pontos
                cv2.line(imagem, tuple(centroids[i]), tuple(centroids[j]), (0, 0, 255), 2)


    # Detectar linhas com a Transformada de Hough
    linhas = cv2.HoughLines(imagem, 1, np.pi/180, 200)
    
    angulos = []
    
    # Desenhar as linhas detectadas na imagem
    if linhas is not None:
        for rho, theta in linhas[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)
            
            # Adiciona a linha na imagem
            cv2.line(imagem, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
            # Calcular o ângulo em graus (conversão de radianos para graus)
            angulo = np.degrees(theta)
            angulos.append(angulo)
    
    # Calcular o ângulo de rotação para alinhar a imagem
    if angulos:
        # Considerar apenas ângulos que correspondem a linhas horizontais ou verticais
        angulos_filtrados = [angulo for angulo in angulos if 70 < angulo < 100 or -10 < angulo < 10]
        if angulos_filtrados:
            angulo_medio = np.mean(angulos_filtrados)
            
            # Rotacionar a imagem para alinhar
            altura, largura = imagem.shape[:2]
            matriz_rotacao = cv2.getRotationMatrix2D((largura // 2, altura // 2), angulo_medio, 1.0)
            imagem_alinhada = cv2.warpAffine(imagem, matriz_rotacao, (largura, altura))
            
            # Mostrar a imagem alinhada
            cv2.imshow('Imagem Alinhada', imagem_alinhada)
            
        else:
            print("Nenhuma linha horizontal ou vertical detectada.")
            imagem_alinhada = imagem
    else:
        print("Nenhuma linha detectada.")
        imagem_alinhada = imagem

    return imagem_alinhada