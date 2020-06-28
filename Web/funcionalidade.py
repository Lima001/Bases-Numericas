#Simbolos para permitir a entrada de numeros até a base 36
#Para ampliar as bases suportadas pelo programa,
#basta adicionar mais elementos ao dicionario de simbolos
simbolos = {
    "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10,
    "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21,
    "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29 ,"U":30, "V":31 ,"W":32,
    "X":33, "Y":34, "Z":35
}

#Dicionario utilizado para converter digitos decimais para outras bases
#Segue o mesmo esquema do dicionário anterior, visto que é é constituido
#Da inversão de chave:valor
simbolos_invertidos = {chave:valor for valor,chave in simbolos.items()}

def gerar_decimal(entrada:str, base:int) -> str:
    saida = 0
    
    sinal, num = retornar_numero_sinal(entrada)
    num = list(num)
    
    for i in range(len(num)):
        saida += int(simbolos[num[-1-i].upper()])*(base**i)

    saida = sinal + str(saida)

    return saida

def converter_decimal(entrada:str, base:int) -> str:
    saida = ""
    
    sinal, num = retornar_numero_sinal(entrada)
    num = int(num)
    
    exe = True
    while exe:
        if num < base:
            exe = False
        resto = num % base
        num = num // base
        saida += simbolos_invertidos[resto]

    saida += sinal
    
    return saida[-1::-1]

#Funções Usadas para verificar se as entradas estão de acordo com o suportado pelo programa
def verificar_base_valida(base:int) -> bool:
    '''
        Verifica se um numero informado está contido no intervalo [1,36] no universo dos Naturais.
        Função utilizada para verificar se uma base formada corresponde a uma base suportada pelo
        programa de conversão entre sistemas númericos desenvolvido.
    '''
    return base > 0 and base <= 36

def retornar_numero_sinal(entrada:str) -> tuple:
    if entrada[0] == "-":
        sinal = "-"
        num = entrada[1:]
    else:
        sinal = ""
        num = entrada

    return (sinal,num)

#Função utilizada para converter o numero de entrada para as diferentes bases informadas
def executar_conversao(dados:dict) -> dict:
    saida = {}
    numero_entrada = dados["numero"]
    base_entrada =  int(dados["base_entrada"])
    numero_decimal = gerar_decimal(numero_entrada, base_entrada)

    for chave, valor in dados["base_saida"].items():
        saida["#resultado-"+chave[11:]] = converter_decimal(numero_decimal, int(valor))

    return saida


def executar_operacao(dados:dict) -> dict:
    saida = {}
    num1 = dados["num1"]
    num2 = dados["num2"]
    operacao = dados["operador"]
    base = int(dados["base"])

    num1_decimal = gerar_decimal(num1, base)
    num2_decimal = gerar_decimal(num2, base)

    expressao = f"{num1_decimal} {operacao} {num2_decimal}"

    resultado_decimal = str(eval(expressao))
    resultado = converter_decimal(resultado_decimal, base)
    
    saida["#resultado"] = resultado
    
    return saida