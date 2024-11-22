def grid_appl(imagem, cy, cx, nova_imagem_centroides):
    limiar_gride = 25
# Inserir grade coluna na imagem original
    imagem_com_grade = imagem.copy()
    VCol = []
    cv2.line(imagem_com_grade, (cx[0] - limiar_gride, 0), (cx[0] - limiar_gride, nova_imagem_centroides.shape[0]), (0, 0, 255), 2)
    VCol.append(cx[0] - limiar_gride)
    p_aux = 0
    for i in range(len(cx)):
        if(cx[i] >= (p_aux + limiar_gride)): 
            cv2.line(imagem_com_grade, (cx[i] + limiar_gride, 0), (cx[i] + limiar_gride, nova_imagem_centroides.shape[0]), (0, 0, 255), 2)
            p_aux = cx[i]
            VCol.append(cx[i] + limiar_gride)

    # Inserir grade linha na imagem original
    VLine = []
    cv2.line(imagem_com_grade, (0, cy[0] - limiar_gride), (nova_imagem_centroides.shape[1], cy[0] - limiar_gride), (0, 0, 255), 2)
    VLine.append(cy[0] - limiar_gride)
    p_aux = 0
    for i in range(len(cy)):
        if(cy[i] >= (p_aux + limiar_gride)): 
            cv2.line(imagem_com_grade, (0, cy[i] + limiar_gride), (nova_imagem_centroides.shape[1], cy[i] + limiar_gride), (0, 0, 255), 2)
            p_aux = cy[i]
            VLine.append(cy[i] + limiar_gride)
    return VLine, VCol