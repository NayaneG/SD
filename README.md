# Sistemas Distribuidos 

1. Construa uma calculadora onde as seguintes operações básicas devem ser realizadas no
servidor: soma, subtração, multiplicação, divisão, potencialização e radiciação. O cliente
deve, portanto, definir a operação e as constantes desejadas. O servidor irá receber estas
informações como parâmetro, realizará o cálculo solicitado e retornará o resultado para o
cliente, que irá, por sua vez, imprimi-lo na tela.

2. Construa uma aplicação para localizar um arquivo no servidor. O nome do arquivo deve ser
informado pelo cliente. O servidor deve informar ao cliente se o arquivo existe ou não.

3. Construa uma aplicação de Chat Broadcast onde os clientes enviam mensagens para o
servidor e o mesmo propaga as mensagens para todos os clientes conectados a ele.

4. Uma agência de viagens possui um sistema online para que seus clientes brasileiros façam
cotações para saber a viabilidade de viajar para Europa ou Estados Unidos. Esses clientes
informam o orçamento em reais e a empresa converte esse valor para Dólar ou Euro
considerando a cotação do dia e o destino do cliente.

    A sequência de passos da interação seria:
    I. O Cliente informa o destino (Europa ou EUA) e o orçamento em reais.
    II. O Servidor recebe esses parâmetros.
    III. O Servidor consulta a cotação atual do Dólar ou Euro (dependendo do destino)
    por meio de um serviço web JSON (fixer.io).
    IV. Baseado na cotação, o Servidor realiza a conversão e retorna o resultado para o
    cliente.
    V. O Cliente recebe a informação na tela.
