# Python Remote Objects(Biblioteca python para criação de aplicações que se comuniquem pela rede)
import Pyro4
import os.path
import json
import requests

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

    def Broadcast(self, texto):
        return texto



#-----------------------------------Quarto Exercicio------------

    def Agencia(self, destino, orcamento):
        base_real = 4.43
        link = requests.get('http://data.fixer.io/api/latest?access_key=ad9f98211c08ae5983b119065722bbcd&symbols=' + destino)
        if link.status_code == 200:
            dados = json.loads(link.content)
            taxa = dados['rates'][destino]
            calculo = orcamento/base_real
            resultado = taxa * calculo
            return resultado



# SERVIDOR instancia OBJETO remoto
objeto = Pyro4.Daemon()

# SERVIDOR registra OBJETO e faz um vinculo dele em uma porta.
vinculo = objeto.register(SD)


ns = Pyro4.locateNS()
ns.register('obj',vinculo)

# Vinculo que será usado no programa CLIENTE é apresentado na tela
print('Rodando...')

# OBJETO  espera por clientes que invoquem seus metódos.
objeto.requestLoop()

