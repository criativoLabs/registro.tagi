from flask import Flask 
import flask.views
import os

app = Flask('__main__')

app.secret_key = 'banana'

'''
def executa(host):
    comando = "host %s" % host
    return os.popen(comando).read()
'''

def executa(url):
    comando =("python avail_client.py -l PT %s")% url
    return os.popen(comando).read()



class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
    def post(self):
        host = flask.request.form['dominio']
        result = executa(host)
        flask.flash(result)
        return self.get()
    
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])



app.debug = True
app.run('200.238.97.141')
