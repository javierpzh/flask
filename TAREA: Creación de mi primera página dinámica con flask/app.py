from flask import Flask, render_template,abort
from lxml import etree
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/potencia/<int:base>/<exponente>',methods=["GET","POST"])
def potencia(base,exponente):
	exponente=int(exponente)
	if exponente>0:
		resultado = base**exponente
	elif exponente==0:
		resultado = 1
	elif exponente<0:
		resultado = base**exponente
	else:
		abort(404)
	return render_template("potencia.html",base=base,exponente=exponente,res=resultado)

@app.route('/cuenta/<palabra>/<letra>',methods=["GET","POST"])
def cuentaletras(palabra,letra):
	if len(letra)!=1:
		abort(404)
	else:
		resultado=palabra.count(letra)
	return render_template("cuentaletras.html",palabra=palabra,letra=letra,res=resultado)

@app.route('/libro/<int:cod>',methods=["GET","POST"])
def codigolibro(cod):
	cod=str(cod)
	doc=etree.parse("libros.xml")
	libros=doc.xpath('//libro/codigo/text()')
	if cod in libros:
		titulo=doc.xpath('/biblioteca/libro[codigo="%s"]/titulo/text()' %(cod))[0]
		autor=doc.xpath('/biblioteca/libro[codigo="%s"]/autor/text()' %(cod))[0]
	else:
		abort(404)
	return render_template("libros.html",libro=titulo,autor=autor)

app.run(debug=True)