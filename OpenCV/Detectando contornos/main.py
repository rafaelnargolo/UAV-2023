import cv2 

img = cv2.imread('moeda.png')  # Lê o endereço da imagem
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converte a imagem para cinza

blurred = cv2.GaussianBlur(imgGray, (5, 5), 0)
'''
A suavização gaussiana é usada para removero ruído de uma imagem e suavizar as bordas.
imgGray é a imagem cinza que quermos aplicar o filtro,(5, 5) é o tamanho do kernel para suavizar a imagem.
O kernel é uma matriz de pesos que é aplicada à imagem.
O tamanho do kernel é representado por um par de números, como (5, 5), indicando que o kernel é uma matriz 5x5. Quanto maior o tamanho do kernel, mais suave a imagem resultante será, e quanto menor o tamanho do kernel, mais detalhada a imagem resultante será.
O valor 0 após (5, 5) é o parâmetro "sigmaX", que é opcional e especifica o desvio padrão da distribuição Gaussiana aplicada para o eixo X. Se sigmaX for zero (o valor padrão), então o desvio padrão é calculado automaticamente com base na largura e altura do kernel. Geralmente, o valor de sigmaX é mantido em 0 para obter resultados mais precisos.
'''

_, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
'''
A função cv2.threshold() é usada para aplicar um limiar (threshold) a uma imagem.
A imagem limiarizada é uma imagem binária onde os pixels são separados em dois valores distintos, geralmente branco e preto, dependendo se eles atendem ou não a algum critério pré-determinado. Esses critérios são geralmente baseados em valores de intensidade de cor ou de brilho. Em outras palavras, uma imagem limiarizada é uma representação simplificada da imagem original, onde as informações são representadas de forma mais direta e clara. A função cv2.threshold() é usada para transformar uma imagem em uma imagem limiarizada, definindo um valor limite (60 neste caso) que separa pixels na imagem em dois grupos: aqueles com intensidade de cor ou brilho acima do valor limite (que serão transformados em branco) e aqueles abaixo do valor limite (que serão transformados em preto). A imagem resultante é uma imagem binária que pode ser usada para realizar operações de processamento de imagem, como detecção de contornos, segmentação e muito mais.
O primeiro argumento da função é a imagem que será limiarizada (neste caso, a imagem 'blurred' resultante da aplicação do GaussianBlur), e os outros argumentos são:

60: Este é o valor do limiar. Qualquer pixel com um valor de intensidade abaixo de 60 será definido como preto, e qualquer pixel com um valor de intensidade acima de 60 será definido como branco.

255: Este é o valor máximo que pode ser atribuído aos pixels brancos.

cv2.THRESH_BINARY: Este é o tipo de limiarização a ser aplicado. Neste caso, estamos usando a limiarização binária, que converte a imagem em tons de cinza em uma imagem binária de preto e branco.

A função cv2.threshold retorna dois valores: o primeiro é o valor do limiar usado, e o segundo é a imagem resultante da limiarização. Neste caso, estamos usando a sintaxe '_, thresh = cv2.threshold' para descartar o primeiro valor retornado e armazenar apenas a imagem resultante na variável 'thresh'.

A variável "_" é comumente usada como uma variável descartável para receber o resultado de uma operação que não é importante para nós. No caso da linha "_, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)", a primeira informação retornada pelo método cv2.threshold é descartada, e apenas a segunda informação (a imagem limiarizada) é armazenada na variável "thresh".
'''

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
'''
A linha 'contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)' é utilizada para encontrar os contornos de objetos na imagem limiarizada (thresh).

A função cv2.findContours retorna dois valores:

contours: uma lista de todos os contornos encontrados na imagem. Cada contorno é representado como uma lista de pontos.
Um segundo valor, que não é utilizado no exemplo (e é por isso que ele é substituído por _), que representa a hierarquia dos contornos, ou seja, como os contornos estão relacionados uns com os outros.
Os argumentos passados para a função cv2.findContours são:

thresh: a imagem limiarizada.
cv2.RETR_EXTERNAL: especifica que só queremos o contorno externo dos objetos.
cv2.CHAIN_APPROX_SIMPLE: especifica que queremos a aproximação mais simples dos contornos. Isso significa que, em vez de armazenar todos os pontos dos contornos, só armazenamos os pontos mais importantes, o que resulta em contornos com menos pontos e mais fáceis de processar.
'''

for c in contours:
    x, y, w, h, = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
'''
Essa parte do código é usada para desenhar retângulos ao redor de cada contorno encontrado na imagem. A função cv2.boundingRect é usada para encontrar as coordenadas (x, y) da posição do retângulo e as dimensões (w, h) do retângulo. Em seguida, a função cv2.rectangle é usada para desenhar o retângulo na imagem original.

Os argumentos da função cv2.rectangle são:

img: a imagem original na qual queremos desenhar os retângulos.
(x, y): as coordenadas do ponto inicial do retângulo.
(x + w, y + h): as coordenadas do ponto final do retângulo.
(0, 255, 0): a cor do retângulo (verde, nesse caso).
2: a espessura em pixels da linha que desenha o retângulo.

A função é executada em um loop "for" que percorre todos os contornos encontrados na imagem (contours). Para cada contorno, as coordenadas e dimensões do retângulo são encontradas com cv2.boundingRect e o retângulo é desenhado na imagem original com cv2.rectangle.
'''

cv2.imshow('image', img)  # Mostra a imagem numa janela com legenda imagem, com a marcação já
cv2.waitKey(0)  # Espera por um tempo indeterminado até que alguma tecla seja pressionada para fechar a janela
cv2.destroyAllWindows()  # Destrói todas janelas abertas
