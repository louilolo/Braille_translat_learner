def letras(snap, flags):
    flag = int(flags)

    a = [1, 0, 0, 0, 0, 0]
    b = [1, 1, 0, 0, 0, 0]
    c = [1, 0, 0, 1, 0, 0]
    d = [1, 0, 0, 1, 1, 0]
    e = [1, 0, 0, 0, 1, 0]
    f = [1, 1, 0, 1, 0, 0]
    g = [1, 1, 0, 1, 1, 0]
    h = [1, 1, 0, 0, 1, 0]
    i = [0, 1, 0, 1, 0, 0]
    j = [0, 1, 0, 1, 1, 0]
    k = [1, 0, 1, 0, 0, 0]
    l = [1, 1, 1, 0, 0, 0]
    m = [1, 0, 1, 1, 0, 0]
    n = [1, 0, 1, 1, 1, 0]
    o = [1, 0, 1, 0, 1, 0]
    p = [1, 1, 1, 1, 0, 0]
    q = [1, 1, 1, 1, 1, 0]
    r = [1, 1, 1, 0, 1, 0]
    s = [0, 1, 1, 1, 0, 0]
    t = [0, 1, 1, 1, 1, 0]
    u = [1, 0, 1, 0, 0, 1]
    v = [1, 1, 1, 0, 0, 1]
    w = [0, 1, 0, 1, 1, 1]
    x = [1, 0, 1, 1, 0, 1]
    y = [1, 0, 1, 1, 1, 1]
    z = [1, 0, 1, 0, 1, 1]
    cedilha = [1, 1, 1, 1, 0, 1]
    espaco = [0, 0, 0, 0, 0, 0]
    ag = [1, 1, 1, 0, 1, 1]
    eg = [1, 1, 1, 1, 1, 1]
    ig = [0, 0, 1, 1, 0, 0]
    og = [0, 0, 1, 1, 0, 1]
    ug = [0, 1, 1, 1, 1, 1]
    acr = [1, 1, 0, 1, 0, 1]
    ecr = [0, 1, 1, 1, 0, 1]
    icr = [1, 0, 0, 1, 0, 1]
    ocr = [0, 1, 0, 1, 1, 1]
    ucr = [1, 0, 0, 0, 1, 1]
    ac = [1, 0, 0, 0, 0, 1]
    ec = [1, 1, 0, 0, 0, 1]
    oc = [1, 0, 0, 1, 1, 1]
    at = [0, 0, 1, 1, 1, 0]
    ot = [0, 1, 0, 1, 0, 1]
    virg = [0, 1, 0, 0, 0, 0]
    doisp = [0, 1, 0, 0, 1, 0]
    ponto = [0, 0, 1, 0, 0, 0]
    excla = [0, 1, 0, 1, 0, 1]
    inte = [0, 1, 0, 0, 0, 1]
    pontvirg = [0, 1, 1, 0, 0, 0]
    maiuscula = [0, 0, 0, 1, 0, 1]

    abP = [1, 1, 0, 0, 0, 1]
    feP = [0, 0, 1, 1, 1, 0]
    mais = [0, 1, 1, 0, 1, 0]
    hif = [0, 0, 1, 0, 0, 1]
    aster = [0, 1, 1, 0, 0, 1]
    divisao = [0, 1, 0, 0, 1, 1]
    igual = [0, 1, 1, 0, 1, 1]

    letter = ['', str(flag)]

    if a == snap:
        if flag == 1:
            letter[0] = 'A'
            flag = 0
        else:
            letter[0] = 'a'
    elif b == snap:
        if flag == 1:
            letter[0] = 'B'
            flag = 0
        else:
            letter[0] = 'b'
    elif c == snap:
        if flag == 1:
            letter[0] = 'C'
            flag = 0
        else:
            letter[0] = 'c'
    elif d == snap:
        if flag == 1:
            letter[0] = 'D'
            flag = 0
        else:
            letter[0] = 'd'
    elif e == snap:
        if flag == 1:
            letter[0] = 'E'
            flag = 0
        else:
            letter[0] = 'e'
    elif f == snap:
        if flag == 1:
            letter[0] = 'F'
            flag = 0
        else:
            letter[0] = 'f'
    elif g == snap:
        if flag == 1:
            letter[0] = 'G'
            flag = 0
        else:
            letter[0] = 'g'
    elif h == snap:
        if flag == 1:
            letter[0] = 'H'
            flag = 0
        else:
            letter[0] = 'h'
    elif i == snap:
        if flag == 1:
            letter[0] = 'I'
            flag = 0
        else:
            letter[0] = 'i'
    elif j == snap:
        if flag == 1:
            letter[0] = 'J'
            flag = 0
        else:
            letter[0] = 'j'
    elif k == snap:
        if flag == 1:
            letter[0] = 'K'
            flag = 0
        else:
            letter[0] = 'k'
    elif l == snap:
        if flag == 1:
            letter[0] = 'L'
            flag = 0
        else:
            letter[0] = 'l'
    elif m == snap:
        if flag == 1:
            letter[0] = 'M'
            flag = 0
        else:
            letter[0] = 'm'
    elif n == snap:
        if flag == 1:
            letter[0] = 'N'
            flag = 0
        else:
            letter[0] = 'n'
    elif o == snap:
        if flag == 1:
            letter[0] = 'O'
            flag = 0
        else:
            letter[0] = 'o'
    elif p == snap:
        if flag == 1:
            letter[0] = 'P'
            flag = 0
        else:
            letter[0] = 'p'
    elif q == snap:
        if flag == 1:
            letter[0] = 'Q'
            flag = 0
        else:
            letter[0] = 'q'
    elif r == snap:
        if flag == 1:
            letter[0] = 'R'
            flag = 0
        else:
            letter[0] = 'r'
    elif s == snap:
        if flag == 1:
            letter[0] = 'S'
            flag = 0
        else:
            letter[0] = 's'
    elif t == snap:
        if flag == 1:
            letter[0] = 'T'
            flag = 0
        else:
            letter[0] = 't'
    elif u == snap:
        if flag == 1:
            letter[0] = 'U'
            flag = 0
        else:
            letter[0] = 'u'
    elif v == snap:
        if flag == 1:
            letter[0] = 'V'
            flag = 0
        else:
            letter[0] = 'v'
    elif w == snap:
        if flag == 1:
            letter[0] = 'W'
            flag = 0
        else:
            letter[0] = 'w'
    elif x == snap:
        if flag == 1:
            letter[0] = 'X'
            flag = 0
        else:
            letter[0] = 'x'
    elif y == snap:
        if flag == 1:
            letter[0] = 'Y'
        else:
            letter[0] = 'y'
    elif z == snap:
        if flag == 1:
            letter[0] = 'Z'
            flag = 0
        else:
            letter[0] = 'z'
    elif cedilha == snap:
        letter[0] = 'ç'
    elif (espaco) == snap:
        letter[0] = ' '
    elif ag == snap:
        letter[0] = 'á'
    elif eg == snap:
        letter[0] = 'é'
    elif ig == snap:
        letter[0] = 'í'
    elif og == snap:
        letter[0] = 'ó'
    elif ug == snap:
        letter[0] = 'ú'
    elif acr == snap:
        letter[0] = 'à'
    elif ecr == snap:
        letter[0] = 'è'
    elif icr == snap:
        letter[0] = 'ì'
    elif ocr == snap:
        letter[0] = 'ò'
    elif ucr == snap:
        letter[0] = 'ù'
    elif ac == snap:
        letter[0] = 'â'
    elif ec == snap:
        letter[0] = 'ê'
    elif oc == snap:
        letter[0] = 'ô'
    elif at == snap:
        letter[0] = 'ã'
    elif ot == snap:
        letter[0] = ''  # verificar
    elif virg == snap:
        letter[0] = ' == '
    elif doisp == snap:
        letter[0] = ':'
    elif ponto == snap:
        letter[0] = '.'
    elif inte == snap:
        letter[0] = '?'
    elif excla == snap:
        letter[0] = '!'
    elif pontvirg == snap:
        letter[0] = ';'
    elif hif == snap:
        letter[0] = '-'
    elif abP == snap:
        letter[0] = '('
    elif feP == snap:
        letter[0] = '){'
    elif mais == snap:
        letter[0] = '+'
    elif aster == snap:
        letter[0] = '*'
    elif divisao == snap:
        letter[0] = '/'
    elif igual == snap:
        letter[0] = '='
    elif maiuscula == snap:
        flag = 1
        letter[0] = ''
    else:
        letter[0] = '#'
        
    letter[1] = str(flag)
    return letter
