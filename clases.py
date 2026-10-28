class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad<0:
            print("cantidad ha de ser pos")
        else: 

            self.saldo+=cantidad
    def retirar(self, cantidad):
        if(self.saldo<cantidad):
            print("saldo negativo")
        else:
            self.saldo-=cantidad
        
    def mostrar(self):
        print(self.titular)
        print(self.saldo)
cuenta = CuentaBancaria("Juan", 100)
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.retirar(500)   # Saldo insuficiente
cuenta.mostrar()

otra = CuentaBancaria("Ana", 500)
otra.mostrar()
cuenta.mostrar()


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes=0.05):
        super().__init__(titular, saldo)
        self.interes = interes
    def aplicar_interes(self):
        self.saldo+=self.saldo*self.interes+self.saldo
    def retirar(self, cantidad):
        if cantidad>200:
            print("denegada operación")
        else:
            super().retirar(cantidad)
    def mostrar(self):
        super().mostrar()
        print(f"Interés: {self.interes}")


ahorro = CuentaAhorro("Ana", 1000, 0.1)
ahorro.aplicar_interes()
ahorro.mostrar()        # Saldo 1100.0
ahorro.retirar(300)     # Límite de retiro superado
ahorro.retirar(100)
ahorro.mostrar()        # Saldo 1000.0
