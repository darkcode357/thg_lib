from THG_libs.thg_auxiliares.thg_debug.debug import Debug
from THG_libs.thg_auxiliares.thg_cores.cores import *
from base64 import b64encode
from base64 import b32encode
from base64 import b16encode


class Arquivos():
    def __init__(self,arquivo,escrever,tabulacao,encode):
        self.arquivo=arquivo
        self.escrever=escrever
        self.tabulacao=tabulacao
        self.encode=encode
    def ler(arquivo):
        with open(arquivo,"r") as ll:
            print(ll.read())
    def escrever(arquivo,escrever):
        with open(arquivo,"w") as ll:
            ll.write(escrever)
            Debug.CRITICAL("thg_arquivo: "+arquivo)

            Debug.CRITICAL("escreveu: "+escrever)
    def escrever_encode64(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b64encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.INFO("Arquivo: "+arquivo)

            Debug.CRITICAL("escrita "+decode)

    def escrever_encode32(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b32encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("Arquivo: "+arquivo)
            Debug.CRITICAL("escrita "+decode)
    def escrever_encode16(arquivo,escrever):
        with open(arquivo,"w") as ll:
            encode = b16encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("thg_arquivo: "+arquivo)
            Debug.CRITICAL("escrita "+decode)

