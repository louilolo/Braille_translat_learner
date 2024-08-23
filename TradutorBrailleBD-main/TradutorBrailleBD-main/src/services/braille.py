import cv2 as cv


class ConversorBraille:
    def __init__(self, img):
        self.img = img

    def convert(self):
        # Filtro: Tom de Cinza
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        # Filtro: Binarização
        ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)
        # Filtro: Contorno de cada ponto baille
        im2, contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        return contours
