from flask import Flask, render_template, request, redirect, url_for, session
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

@app.route("/converter_numero", methods=["post"])
def converter_numero():
    numero = request.form["numero"]
    base_entrada = int(request.form["base_entrada"])
    base_saida = int(request.form["base_saida"])

    if not (verificar_base_valida(base_entrada) and verificar_base_valida(base_saida)):
        return "Erro -> Bases informadas não suportadas"
    
    if not verificar_numero_valido(float(numero)):
        return "Erro -> Numero informado não suportado"

    numero_decimal = gerar_decimal(numero,base_entrada)
    numero_convertido = converter_decimal(numero_decimal,base_saida)

    return numero_convertido

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