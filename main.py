from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hipotenusa", methods=["GET"])
def pagHipotenusa():
    return render_template("hipotenusa.html")

@app.route("/resultadoHipotenusa", methods=["POST", "GET"])
def calculaHipotenusa():
  catetoA = int(request.form['catetoA'])
  catetoB = int(request.form['catetoB'])
  hipotenusa = math.sqrt((catetoA**2) + ((catetoB**2)))
  if hipotenusa > 0:
    trueHipotenusa = "É um triângulo pitagórico"
    falseHipotenusa = "Não é um triângulo pitagórico"
    if ((catetoA**2) + ((catetoB**2))) == hipotenusa**2:
      return render_template("resultadoHipotenusa.html", value = hipotenusa, info=trueHipotenusa)
    else:
      return render_template("resultadoHipotenusa.html", value = hipotenusa, info=falseHipotenusa)
  else:
    msg = "Número inválido"
    msg2 = "Insira novos números"
    return render_template("resultadoHipotenusa.html", value=msg, info=msg2)    
     
@app.route("/catetoAdj", methods=["GET"])
def pagCatetoAdj():
  return render_template("catetoAdj.html")

@app.route("/resultadoCatetoAdj", methods=["POST", "GET"])
def calculaCatetoAdj():
  catetoX = int(request.form['catetoX'])
  hipotenusaX = int(request.form['hipotenusaX'])
  catetoY = math.sqrt((hipotenusaX**2) - (catetoX**2))
  if catetoY > 0:
    return render_template("resultadoCatetoAdj.html", value = catetoY)
  else:
    msg = "Número inválido\nInsira novos números"
    return render_template("resultadoHipotenusa.html", value=msg)

@app.route("/catetoOp", methods=["GET"])
def pagCatetoOp():
  return render_template("catetoOp.html")

@app.route("/resultadoCatetoOp", methods=["POST", "GET"])
def calculaCatetoOp():
  catetoX = int(request.form['catetoX'])
  hipotenusaX = int(request.form['hipotenusaX'])
  catetoY = math.sqrt((hipotenusaX**2) - (catetoX**2))
  if catetoY > 0:
    return render_template("resultadoCatetoOp.html", value = catetoY)
  else:
    msg = "Número inválido\nInsira novos números"
    return render_template("resultadoHipotenusa.html", value=msg)


app.run(debug=True)