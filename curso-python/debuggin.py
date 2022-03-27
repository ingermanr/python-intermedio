# debuyggin y errores
def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors
        
def main():

    
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debe ingresar un número")
    

    try:
        num = int(input("Ingresa un número: "))
        if num<=0:
            raise ValueError
        return print(divisors(num)); print("Terminó mi programa")
    except ValueError:
        print("Debe ingresar un número positivo")

    
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    # assert num>0, "Ingrese un valor positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")

    num = int(input("Ingresa un número: "))
    assert num>0, "Ingrese un valor positivo"
    print(divisors(num))
    print("Terminó mi programa")
        
if __name__ == '__main__':
    main()