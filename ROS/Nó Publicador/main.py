import rospy  # Importando o ROS do Python

from std_msgs.msg import String  # Importando o tipo String do módulo std_msgs. Será usado apenas para mostrar string.

def talker():  # Início da função do nó publicador 'talker'

    pub = rospy.Publisher('chatter', String, queue_size = 10)  # A variável pub recebe um objeto de rospy.Publisher. 
    '''
    - A variável 'pub' recebe um objeto rospy.Publisher, que representa um publicador de mensagens em um tópico no ROS (Robot Operating System).
    - O primeiro argumento, 'chatter', é o nome do tópico no qual o nó publicador irá publicar mensagens.
    - O segundo argumento, String, é o tipo de mensagem que será publicada no tópico.
    - O terceiro argumento, queue_size = 10, é o tamanho da fila de mensagens. Isso significa que ao menos 10 mensagens podem ser armazenadas na fila, garantindo que as mensagens sejam lidas pelos nós assinantes, mesmo se houver atrasos na entrega. Se o nó publicador enviar mais de 10 mensagens antes que algum nó assinante as leia, as mensagens mais antigas serão descartadas e as mais novas ficarão na fila.
    Em geral, o tamanho da fila ajuda a garantir que as mensagens não sejam perdidas, uma vez que a comunicação no ROS é assíncrona e pode haver atrasos na entrega das mensagens.
    '''
    rospy.init_node('talker', anonymous=True)  # Declara o nó 'talker'
    '''
    - Até que o ROS não tenha o nome do nó, ele não irá estabelecer a comunicação com o ROS Master.
    - O nome que o nó receberá é somente uma string. Não usar barra '\'.
    - anonymous = Ture garante que o nó não terá o mesmo nome que algum outro.
    '''
    rate = rospy.Rate(10)  # Define a frequência de publicação da mensagem. Se não for declarado, o nó publicará na maior velocidade que puder.
    
    while not rospy.is_shutdown():  # Enquando o ROS não for interrompido... (Aqui começa a publicação da mensagem no tópico)
        hello_str = "Hello, World %s" % rospy.get_time()  # Declara uma string para mostrar a string + tempo em milissegundos.
        rospy.loginfo(hello_str)  # Isso é o print do ROS. 
        pub.publish(hello_str)  # Publica a string no tópico
        rate.sleep()  # Espera o tempo necessário para que as mensagens sejam publicadas na frequência definida anteriormente (10Hz)
        
if __name__ == '__main__':
    try:  
        talker()
    except ROSInterruptException:  
        pass
'''
A verificação "if name == 'main'" é uma convenção comum em Python para garantir
que o código só será executado se o arquivo for executado como um script principal,
em vez de ser importado como módulo em outro script. Isso garante que o código 
só seja executado quando o arquivo for executado diretamente, e não quando é importado por outro script.
'''

#  1º - Criar o tópico: rospy.Publisher('nome', tipo, tamanho_fila)
#  2º - Criar o nó publicador: rospy.init_node('nome', anonymous=True)
#  3º - Declarar a frequência de publicação: rospy.Rate(Hz)