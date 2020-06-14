#O seguinte conversor de bases suporta bases do intervalo [2,36]
#E utiliza a base decimal como meio de conversão entre as bases informadas
#Sendo assim é necessário importar o modulo decimal, que já foi implementado
#E disponibilizado no mesmo local deste arquivo
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
    
    base_entrada = 0
    base_saida = 0
    while not(verificar_base(base_entrada)):
        base_entrada = int(input("Digite a base de entrada(2-36): ")) 
    
    numero_entrada = (input("Digite o numero a ser convertido: "))
    
    while not(verificar_base(base_saida)):
        base_saida = int(input("Digite a base de saída(2-36): "))

    saida_decimal = decimal.gerar_decimal(numero_entrada,base_entrada)
    numero_saida = decimal.converter_decimal(saida_decimal,base_saida)
    
    print(numero_saida)
    trava = input("Pressione Enter para prosseguir")