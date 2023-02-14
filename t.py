import cv2

img = cv2.imread('montanha.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contornos = cv2.Canny(gray, 60, 150)
cv2.imshow('imagem', contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()