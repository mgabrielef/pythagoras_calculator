import math
import main
from flask import Flask, render_template, request

app = Flask(__name__)

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