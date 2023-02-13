import cv2

#  Essa desgraça não tá funcionando, mas é assim que se faz
img = cv2.imread('arvores.jpg')  # Lê o endereço da imagem

imgRszed = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)  # Diminui a dimensão da imagem em 50% da largula e altura
'''
img é a imagem a ser passada para redimensionar
Aqui, (0, 0) significa que a dimensão final é calculada pelo opencv.
fx é fator de escala aplicado à largura da imagem e fy é o fator de escala
aplicado à altura. Se os valor para ambos forem 2, a imagem final
terá o dobro da largura e altura, se for 0.5, terão largura e altura
iguais a metade da dimensão da imagem original. 
'''

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Imagem cinza
cv2.imshow('Imagem', img)  # Mostra a imagem com a legenda 'Imagem' na janela
cv2.waitKey(0)  # Com o valor 0, espera por tempo indefinido até que alguma tecla seja pressionada
cv2.destroyAllWindows()  # Fecha todas as janelas
