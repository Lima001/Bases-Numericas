from flask import Flask, render_template, request, redirect, url_for, session
from func import *

app = Flask("__name__")

@app.route("/")
def iniciar():
    return render_template("converter.html")

@app.route("/converter_numero", methods=["post"])
def converter_numero():
    numero = request.form["numero"]
    base_entrada = int(request.form["base_entrada"])
    base_saida = int(request.form["base_saida"])

    numero_decimal = gerar_decimal(numero,base_entrada)
    numero_convertido = converter_decimal(numero_decimal,base_saida)

    return numero_convertido

app.run()