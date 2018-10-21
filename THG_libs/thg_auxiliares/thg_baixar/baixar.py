import wget
from THG_libs.thg_auxiliares.thg_debug.debug import Debug


class Baixar():
    def __init__(self, url, arquivo, saida=""):
        self.url = url
        self.saida = saida
        self.arquivo = arquivo

    def baixar(url, saida=""):
        if url == None:
            print("[+]erro nao pode ser um argumento vazio")
            pass
        elif saida == None:
            print("local padrao [/tmp]")
            try:
                _local = "/tmp"
                arquivo = wget.download(url=url, out=_local)
                Debug.AVISO("Diretorio => [" + _local + "]")
                Debug.AVISO("Arquivo => [" + arquivo + "]")
            except Exception:
                pass
        else:
            local = saida
            arquivo = wget.download(url=url, out=local)
            Debug.AVISO("Diretorio => ["+local+"]")
            Debug.AVISO("Arquivo => ["+arquivo+"]")
