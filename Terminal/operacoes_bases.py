import decimal

def verificar_base(base=0):
    if base > 1 and base < 37:
        return True
    return False

while True:
    print("\n"*100)
    print("-"*10)
    print("Digite '0' para sair ou '1' para continuar \n")
    
    op = input("Deseja utilizar o programa? ")
    if op == "0":
        break

    base = 0
    while not(verificar_base(base)):
        base = int(input("\nDigite a base em que deseja realizar as operações(2-36): ")) 
    
    num1 = (input("Digite o primeiro numero: "))
    num2 = (input("Digite o segundo numero: "))
    
    print("\n-- Operações suportadas--")
    print("'+' Soma | '-' Subtração | '*' multiplicação | '/' divisão")
    print("'**' Potenciação inteira | '//' Divisão inteira | '%' resto de divisão")
    operacao = input("Digite a operação a ser realizada: ")
    
    num1_decimal = decimal.gerar_decimal(num1,base)
    num2_decimal = decimal.gerar_decimal(num2,base)
    comando = "resultado_decimal = " + str(num1_decimal) + operacao + str(num2_decimal)
    exec(comando)
    print(decimal.converter_decimal(resultado_decimal,base))
    trava = input("Pressione enter para continuar")