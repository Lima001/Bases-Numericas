from flask import Flask, render_template, request, json, jsonify

from funcionalidade import *

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
    dados = request.get_json()
    return jsonify(executar_conversao(dados))

@app.route("/realizar_operacao", methods=["POST"])
def realizar_operacao():
    dados = request.get_json()
    return jsonify(executar_operacao(dados))

@app.after_request
def add_headers(resposta):
    resposta.headers.add('Access-Control-Allow-Origin', '*')
    resposta.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return resposta

app.run(debug=True)