from flask import Flask, render_template,abort
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


app.run(debug=True)