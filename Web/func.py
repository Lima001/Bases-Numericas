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

def gerar_decimal(num:int, base:int) -> int:
    decimal = 0
    num = list(str(num))
    for i in range(len(num)):
        decimal += int(simbolos[num[-1-i].upper()])*(base**i)
    
    return decimal

def converter_decimal(num:int, base:int) -> str:
    saida = ""
    exe = True
    while exe:
        if num < base:
            exe = False
        resto = num % base
        num = num // base
        saida += simbolos_invertidos[resto]
    
    return saida[-1::-1]

#Funções Usadas para verificar se as entradas estão de acordo com o suportado pelo programa
def verificar_base_valida(base:int) -> bool:
    '''
        Verifica se um numero informado está contido no intervalo [1,36] no universo dos Naturais.
        Função utilizada para verificar se uma base formada corresponde a uma base suportada pelo
        programa de conversão entre sistemas númericos desenvolvido.
    '''
    if base > 0 and base <= 36:
        return True
    
    return False

#Usar para verificar se as entradas estão de acordo com o suportado pelo programa
def verificar_numero_valido(numero:int) -> bool:
    if numero >= 0 and int(numero) == numero:
        return True
    return False

def executar_conversao(dados:dict) -> dict:
    pass