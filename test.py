import  argparse

def soma(n1, n2):
    print( f"A soma de {n1} + {n2} = {n1+n2}")

def subtracao(n1, n2):
    print(f"A diferença entre  {n1} e {n2} = {n1 - n2}")

def divisao(n1, n2):
    if n2 == 0:
        print("Sê loco! Tá querendo fazer divisão por zero?")
    else:
        print(f"A divisao de  {n1} por {n2} = {n1 / n2}")

def multiplicacao(n1, n2):
    print(f"O produto de  {n1} e {n2} = {n1 * n2}")

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('option', choices= ['somar', 'subtrair','multiplicar', 'dividir'])

    parser.add_argument("numero1", type=int)
    parser.add_argument("numero2", type=int)

    args = parser.parse_args()
    item_menu = args.option

    if item_menu  == "somar":
        soma(args.numero1, args.numero2)
    elif item_menu == "subtrair":
        subtracao(args.numero1, args.numero2)
    elif item_menu == "multiplicar":
        multiplicacao(args.numero1, args.numero2)
    elif item_menu == "dividir":
        divisao(args.numero1, args.numero2)

if  __name__ == "__main__":
    main()