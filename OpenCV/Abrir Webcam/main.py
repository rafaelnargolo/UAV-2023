import cv2

webcam = cv2.VideoCapture(0)  # Pega a imagem da webcam (valor 0) e coloca dentro da variável webcam
if webcam.isOpened():  # Se webcam estiver aberta
    validacao, frame = webcam.read()  # .read() retorna dois valores: o primeiro é booleano e vai ser atribuído à validação e o segundo é uma lista e será atribuída à frame
    while validacao:   # Enquanto validacao for True
        validacao, frame = webcam.read()  # Lendo webcam, dessa vez em loop infinito
        cv2.imshow("Vídeo da Webcam", frame)  # Mostra uma janela com a legenda 'Vídeo da Webcam' e a imagem mostrada vai ser 'frame'
        key = cv2.waitKey(5)  # Espera 5 milissegundos para a imagem não ser exibida em uma frequência muita alta, assim podemos ver
        if key == 27:  # 27 é a telca Esc
            break
    cv2.imwrite("captura.png", frame)  # Salva imagem, último frame
webcam.release()  # Termina conexão com a webcam
cv2.destroyAllWindows()  # Fecha janelas abertas
