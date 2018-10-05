import codecs
from THG_libs.thg_auxiliares.thg_decode.conf_decode import *
class Decode:
    def decode(texto,ddencode):
        for k in arry_decode.values():
            if k == ddencode:
                enc = codecs.encode(texto,k)
                print(str(enc)[2:-1])


