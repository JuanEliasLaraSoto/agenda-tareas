def sumar(a,b):
    return a+b
def multiplicar(a,b):
    return a*b
def restar(a,b):
    return a-b
def dividir(a,b):
    if b==0:
        print("division entre 0")
    else:
        return a/b
lista=[]
while True :
    a=int(input())
    b=int(input())
    print("1.sumar - 2.restar - 3.multiplicar - 4.dividir - 5.historial - 6.salir")
    operacion=int(input("elige operacion"))
    if operacion==1:
        print(sumar(a,b))
        lista.append(f"{a}+{b}="+str(sumar(a,b)))
    elif operacion==2:
        print(restar(a,b))
        lista.append(f"{a}-{b}="+str(restar(a,b)))

    elif operacion==3:
        print(multiplicar(a,b))
        lista.append(f"{a}*{b}="+str(multiplicar(a,b)))

    elif operacion==4 :
        print(dividir(a,b))
        lista.append(f"{a}/{b}="+str(dividir(a,b)))

    elif operacion==5:
        for elem in lista:
            print(elem)
    elif operacion==6:
        break

