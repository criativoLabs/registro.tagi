import os 
import sys
url = raw_input("Digite Dominio: ")
#url = sys.args[0]

def verificaURL(url):
    comando =("python avail_client.py -l PT %s")% url
    x = os.popen(comando)
    x = x.read()
    info = x.split("\n")
    p1 = ( info[1].split(":") )
    p2 = ( info[2].split(":") )
    status = p2[1]
    p2[1] = status[2::]
    p1 = tuple(p1)
    p2 = tuple(p2)
    lista = [p1,p2]
    dic = dict(lista)
    return dic

dic = verificaURL(url)



dicNew = traduz(verificaURL(url))

print "Dominio:%s\nStatus:%s" %(dicNew["Domain name"],dicNew["Response Status"])
