from flask import Flask, render_template, request
import math


#Iniciando app
app = Flask(__name__)


#Definindo rota inicial
@app.route("/")
def index():
    return render_template("index.html")


#Definindo rota para página "CALCULAR HIPOTENUSA"    
@app.route("/hipotenusa", methods=["GET"])
def pagHipotenusa():
    return render_template("hipotenusa.html")


#Criando função para calcular o valor da hipotenusa
@app.route("/resultadoHipotenusa", methods=["POST", "GET"])
def calculaHipotenusa():
  #Requisitando valores inseridos no form pela name tag
  catetoA = int(request.form['catetoA'])
  catetoB = int(request.form['catetoB'])
  #Realizando cálculo para obter valor da hipotenusa
  hipotenusa = math.sqrt((catetoA**2) + ((catetoB**2)))
  #Inserindo condição, se o valor da hipotenusa for maior que 0 irá redirecionar a página e retornar o valor com informação
  if hipotenusa > 0:
    trueHipotenusa = "É um triângulo pitagórico"
    falseHipotenusa = "Não é um triângulo pitagórico"
    if ((catetoA**2) + ((catetoB**2))) == hipotenusa**2:
      return render_template("resultadoHipotenusa.html", value = hipotenusa, info=trueHipotenusa)
    else:
      return render_template("resultadoHipotenusa.html", value = hipotenusa, info=falseHipotenusa)
  #Se o valor da hipotenusa não condizer com a condição anterior irá redirecionar a página e exibir mensagem 
  else:
    msg = "Número inválido"
    msg2 = "Insira novos números"
    return render_template("resultadoHipotenusa.html", value=msg, info=msg2)    


#Definindo rota para página "CALCULAR CATETO OPOSTO" 
@app.route("/catetoOp", methods=["GET"])
def pagCatetoOp():
  return render_template("catetoOp.html")


#Criando função para calcular o valor do Cateto Oposto
@app.route("/resultadoCatetoOp", methods=["POST", "GET"])
def calculaCatetoOp():
  #Requisitando valores inseridos no form pela name tag
  catetoX = int(request.form['catetoX'])
  hipotenusaX = int(request.form['hipotenusaX'])
  #Realizando cálculo para obter valor do cateto oposto
  catetoY = math.sqrt((hipotenusaX**2) - (catetoX**2))
  #Inserindo condição, se o valor do cateto for maior que 0 irá redirecionar a página e retornar o valor
  if catetoY > 0:
    return render_template("resultadoCatetoOp.html", value = catetoY)
  #Se o valor do cateto não condizir com a condição anterior irá redirecionar a página e exibir mensagem  
  else:
    msg = "Número inválido\nInsira novos números"
    return render_template("resultadoCatetoOp.html", value=msg)


#Definindo rota para página "CALCULAR CATETO ADJACENTE"     
@app.route("/catetoAdj", methods=["GET"])
def pagCatetoAdj():
  return render_template("catetoAdj.html")


#Criando função para calcular o valor do Cateto Adjacente
@app.route("/resultadoCatetoAdj", methods=["POST", "GET"])
def calculaCatetoAdj():
  #Requisitando valores inseridos no form pela name tag
  catetoX = int(request.form['catetoX'])
  hipotenusaX = int(request.form['hipotenusaX'])
  #Realizando cálculo para obter valor do cateto adjacente
  catetoY = math.sqrt((hipotenusaX**2) - (catetoX**2))
  #Inserindo condição, se o valor do cateto for maior que 0 irá redirecionar a página e retornar o valor
  if catetoY > 0:
    return render_template("resultadoCatetoAdj.html", value = catetoY)
  #Se o valor do cateto não condizir com a condição anterior irá redirecionar a página e exibir mensagem
  else:
    msg = "Número inválido\nInsira novos números"
    return render_template("resultadoCatetoAdj.html", value=msg)

#Certificando se o app já está aberto, se não, irá abrir
if __name__ == '__main__':
    app.run(debug=True)