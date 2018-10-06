import Pyro4

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#CLIENTE acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

#CLIENTE referencia remotamente um ou mais métodos do OBJETO que está no SERVIDOR


print('CLIENTE 0')

print('-----------------Exercicio 1--------------------')
#Chamadas dos metodos
resultado_soma = acesso.Soma(1, 1)
resultado_subtracao = acesso.Subtracao(10,5)
resultado_multiplicacao = acesso.Multiplicacao(2,2)
resultado_divisao = acesso.Divisao(2,2)
resultado_potenciacao = acesso.Potenciacao(2,2)
resultado_radiciacao = acesso.Radiciacao(2,2)

#Apresentando resultados
print('Soma: ',resultado_soma)
print('Subtracao: ',resultado_subtracao)
print('Multiplicacao: ',resultado_multiplicacao)
print('Divisao: ',resultado_divisao)
print('Potenciacao:',resultado_potenciacao)
print('Radiciacao: ',resultado_radiciacao)


print('\n-----------------Exercicio 2--------------------')
#Chamada do metodo
resultado_arquivo = acesso.Arquivo('arquivo.txt')

#Apresentando resultados
if (resultado_arquivo == False):
    print('Arquivo nao encontrado')
else:
    print('Arquivo encontrado')



print('\n-----------------Exercicio 3--------------------')
#Chamada do metodo
resultado_broadcast = acesso.Broadcast('Quero enviar esta mensagem para todos os clientes - Cliente 0')
print(resultado_broadcast)



print('\n-----------------Exercicio 4--------------------')
destino = 'USD'
orcamento = 200
resultado_agencia = acesso.Agencia(destino,orcamento)
print(destino,resultado_agencia)
