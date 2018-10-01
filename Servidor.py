# Python Remote Objects(Biblioteca python para criação de aplicações que se comuniquem pela rede)
import Pyro4
import os.path

# Decorator  que permite com que as classes/metódos abaixo sejam expostos para um acesso remoto.


@Pyro4.expose
# Criação de uma classe qualquer
class SD:
    # -----------------------------------Primeiro Exercicio------------
    def Soma(self, a, b):
        resultado = a + b
        return resultado

    def Subtracao(self, a, b):
        resultado = a - b
        return resultado

    def Multiplicacao(self, a, b):
        resultado = a * b
        return resultado

    def Divisao(self, a, b):
        resultado = a / b
        return resultado

    def Potenciacao(self, a, b):
        resultado = a ** b
        return resultado

    def Radiciacao(self, a, b):
        resultado = a ** (1 / b)
        return resultado




    #-----------------------------------Segundo Exercicio------------

    def Arquivo(self, arquivolido):
        resultado = os.path.exists(arquivolido)
        return resultado





    #-----------------------------------Terceiro Exercicio------------

    def Arquivo(self, arquivolido):
        resultado = os.path.exists(arquivolido)
        return resultado








# SERVIDOR instancia OBJETO remoto
objeto = Pyro4.Daemon()

# SERVIDOR registra OBJETO e faz um vinculo dele em uma porta.
vinculo = objeto.register(SD)

# Vinculo que será usado no programa CLIENTE é apresentado na tela
print(vinculo)

# OBJETO  espera por clientes que invoquem seus metódos.
objeto.requestLoop()
