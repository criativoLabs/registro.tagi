from flask import Flask 
import flask.views
import os

app = Flask('__main__')

app.secret_key = 'banana'

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
    def post(self): 
        host = flask.request.form['dominio']
        
        dicNew = traduz(verificaURL(url))        
        
        flask.flash(dicNew)
        return self.get()
    
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])



app.debug = True
app.run()



'''
def executa(url):
    comando =("python avail_client.py -l PT %s")% url
    return os.popen(comando).read()
'''

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

def traduz(dic):
    if (dic["Response Status"]==" (Registered)"):
    dic["Response Status"] = " Dominio Registrado"
    elif (dic["Response Status"] == " (Available)"):
    dic["Response Status"] = " Disponivel p/ Registro"
    else:
    dic["Response Status"] = " Dominio Invalido"
    return dic

dicNew = traduz(verificaURL(url))

print "Dominio:%s\nStatus:%s" %(dicNew["Domain name"],dicNew["Response Status"])
