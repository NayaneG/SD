import Pyro4

#CLIENTE acessa remotamente SERVIDOR
acesso = Pyro4.Proxy("PYRO:obj_20efeeaee63f4ee6a4f7957e5eb264a3@localhost:64772")

#CLIENTE referencia remotamente um ou mais métodos do OBJETO que está no SERVIDOR



resultado_soma = acesso.Soma(1, 1)
resultado_subtracao = acesso.Subtracao(10,5)
resultado_multiplicacao = acesso.Multiplicacao(2,2)
resultado_divisao = acesso.Divisao(2,2)
resultado_potenciacao = acesso.Potenciacao(2,2)
resultado_radiciacao = acesso.Radiciacao(2,2)
resultado_arquivo = acesso.Arquivo('testfrhe.txt')




#Retorno do método será apresentado na tela
print('Soma: ',resultado_soma)
print('Subtracao: ',resultado_subtracao)
print('Multiplicacao: ',resultado_multiplicacao)
print('Divisao: ',resultado_divisao)
print('Potenciacao:',resultado_potenciacao)
print('Radiciacao: ',resultado_radiciacao)

print(resultado_arquivo)

