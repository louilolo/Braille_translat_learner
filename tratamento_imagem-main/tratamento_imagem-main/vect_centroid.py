
def centroid_vect(escala_de_cinza_processada3):
        # Encontrar contornos na imagem limiarizada
    contornos, _ = cv2.findContours(escala_de_cinza_processada3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    

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
    return centroids