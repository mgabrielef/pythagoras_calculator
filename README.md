# PYTHAGORAS_CALCULATOR

Projeto para descobrir os valores dos catetos e hipotenusa de acordo com o teorema de pitágoras utilizando Flask.

Tecnologias utilizadas:
- Python
- Flask

## ÍNDICE
* [Utilizando o projeto](#Utilizando-o-projeto)
* [Inicialização](#Inicialização)
* [Métodos do projeto](#Métodos-do-projeto)
* [Utilizando](#Utilizando)

## Utilizando o projeto

Para utilizar o projeto execute:

```
git clone https://github.com/mgabrielef/pythagoras_calculator
```

## Inicialização

Para iniciar o projeto será necessário ter o Flask instalado em sua máquina:

```
$ pip install -U Flask
```

# Métodos do projeto

Calcular hipotenusa

```python
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
  
```  

Calcular cateto oposto

```python
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
  
```
Calcular cateto adjacente

```python
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
```

# Utilizando

Para rodar o app, insira o código no terminal:
```
python app.py
```


Você pode acessar também o [HEROKU APP](https://mysterious-mesa-79161.herokuapp.com)
