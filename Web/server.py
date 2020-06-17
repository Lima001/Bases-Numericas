from flask import Flask, render_template, request, redirect, url_for, session, json, jsonify

from func import *

app = Flask("__name__")

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/exibir_conversor")
def exibir_conversor():
    return render_template("converter.html")

@app.route("/exibir_operador")
def exibir_operador():
    return render_template("operar.html")

@app.route("/converter_numero", methods=["POST"])
def converter_numero():
    resposta = request.get_json()
    print(resposta, type(resposta))
    return "Ok"

@app.after_request
def add_headers(resposta):
    resposta.headers.add('Access-Control-Allow-Origin', '*')
    resposta.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return resposta

@app.route("/realizar_operacao", methods=["post"])
def realizar_operacao():
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    base = int(request.form["base"])
    operacao = request.form["operacao"]

    if not (verificar_base_valida(base)):
        return "Erro -> Base informada não suportada"
    
    if not (verificar_numero_valido(float(num1)) and verificar_numero_valido(float(num2))):
        return "Erro -> Numeros informados não suportados"

    num1_decimal = gerar_decimal(num1,base)
    num2_decimal = gerar_decimal(num2,base)

    comando = f"{num1_decimal}{operacao}{num2_decimal}"

    resultado_decimal = eval(comando)
    resultado = converter_decimal(resultado_decimal,base)

    return resultado

app.run(debug=True)