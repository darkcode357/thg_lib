#brainiac_dosc
from THG_libs.thg_auxiliares.thg_debug.debug import Debug

class Docs:
    def __init__(self):
        pass

    def web_docs():
        import os
        print(os.getcwd())
        os.chdir("docs")
        Debug.AVISO("[+]=> iniciando doc_web")
        try:
            import mkdocs
            del mkdocs
            os.system("mkdocs serve")
        except ImportError:
            os.system("pip3 install mkdocs -v ")
