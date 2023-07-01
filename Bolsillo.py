class Bolsillo:
    idBolsillo=""
    saldoBolsillo=0
    numeroCelular=""
    claveBolsillo=""
    estadoBolsillo= True

    def crearBolsillo(self):
        self.idBolsillo=int(input("Digite el id de su bolsillo, por favor:)"))
        self.numeroCelular=(input("Digite su numero celular, por favor:)"))
        self.claveBolsillo=(input("Digite una clave para su bolsillo, por favor"))
        
    def entrarBolsillo(self):
        numCel=(input("Digite su numero celular"))
        clave=(input("digite su clave"))

        if numCel == self.numeroCelular and clave == self.claveBolsillo:
            print("Acceso exitoso:)")

        else:
            print("lo lamento, ingrese de nuevo sus credenciales:(")

    def ConsultarSaldo(self):
        print(f"su saldo actual es de {self.saldoBolsillo} " )

    def recargarBolsillo(self, valorRecargo):
        valorRecargo=int(input("ingrese el valor que desea recargar"))
        self.saldoBolsillo= valorRecargo + self.saldoBolsillo
        return self.saldoBolsillo
    
    def sacarPlata(self, retirar):
        retirar=int(input("ingrese el valor que desea retirar"))
        if retirar > self.saldoBolsillo:
            
