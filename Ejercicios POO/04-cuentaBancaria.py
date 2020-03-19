# Se quiere crear una clase Cuenta la cual se caracteriza por tener asociado
# un numero de cuenta y un saldo disponible. Ademas, se puede consultar
# el saldo disponible en cualquier momento, recibir abonos y pagar recibos.

# Crear ademas una clase Persona, que se caracteriza por un DNI y un array
# de cuentas bancarias. La Persona puede tener asociada hasta 3 cuentas
# bancarias, y debe tener un metodo que permite añadir cuentas (hasta 3
# que es el maximo). Tambien debe contener un metodo que devuelva si la
# persona es morosa, i.e., si tienen alguna cuenta con saldo negativo.

# Imprimir por pantalla el si la persona es morosa.
# Posteriormente hacer una transferencia de una cuenta a otra y comprobar
# mostrandolo por pantalla que cambia el estado de la persona.

# clase cuenta
class Cuenta:
    num_cuenta = 0
    saldo_disponible = 0

    def __init__(self, num_cuenta, saldo_disponible):
        self.num_cuenta = num_cuenta
        self.saldo_disponible = saldo_disponible

# clase persona
class Persona(Cuenta):
    banco = []
    cuentas = []
    morosos = []

    def __init__(self, dni, cta_bcaria, num_cuenta, saldo_disponible):
        self.dni = dni
        self.cta_bcaria = cta_bcaria
        super().__init__(num_cuenta, saldo_disponible)

    # metodo para agregar las cuentas bancarias
    def agregarCtaBancaria(self, dni_confirm):
        array = []
        if self.dni == dni_confirm:
            array.append(self.dni)
            array.append(self.cta_bcaria)
            self.cuentas.append(array)
        else:
            print("No existe ese dni en nuestra bbdd")
        return print("Agrego '{self.cta_bcaria}'".format(self = self))

    # metodo para agregar nuevas cuentas bancarias
    def agregarNuevaCtaBancaria(self, dni_confirm, nueva_cta):
        for i in self.cuentas:
            if i[0] == self.dni:
                if len(i) < 4:
                    i.append(nueva_cta)
                    return print("Agregado '{nueva_cta}'".format(nueva_cta = nueva_cta))
                else:
                    print("No se pudo agregar '{nueva_cta}' porque no puede agregar mas de 3 cuentas bancarias".format(nueva_cta = nueva_cta))

    # metodo de agregar al banco
    def agregar_Banco(self):
        banco_dic = {}
        guardar = None
        for i in self.cuentas:
            if i[0] == self.dni:
                guardar = i
            if guardar == None:
                guardar = self.cta_bcaria
        banco_dic = dict( dni = self.dni, cta_bcaria = guardar, num_cuenta = self.num_cuenta, saldo = self.saldo_disponible )
        self.banco.append(banco_dic)

    def ver_banco(self):
        print(self.banco)


    # metodo de verificacion de saldo
    def verificacion(self, dni_confirim):
        for i in self.banco:
            if dni_confirim == i["dni"]:
                if i["saldo"] < 0:
                    self.morosos.append(i["dni"])
                    return print("Usted tiene saldo ${saldo}, se agrego a la lista de morosos".format(saldo = i["saldo"]))
                else:
                    try:
                        self.morosos.remove(i["dni"])
                    except:
                        return print("Tiene un saldo de ${saldo}, usted no es moroso".format(saldo = i["saldo"]))

    # metodo de ingresar saldo
    def ingresarSaldo(self, dni_confirm, ingresar):
        for i in self.banco:
            if dni_confirm == i["dni"]:
                if ingresar < 0:
                    return print("Usted no puede ingresar saldo negativo")
                else:
                    i["saldo"] += ingresar
                    return print("Usted ingreso $",ingresar," a su cuenta")

    # metodo de retirar saldo
    def retirarSaldo(self, dni_confirm, retirada):
        for i in self.banco:
            if dni_confirm == i["dni"]:
                if retirada < 0:
                    return print("No puede retirar saldo negativo")
                else:
                    i["saldo"] -= retirada
                    return print("Usted ha retirado $",retirada," de su saldo")

    # metodo de transferencia
    def transferencia(self, dni_confir, transf, dni_transf):
        cta_transf =""
        cta_benef = ""
        for i in self.banco:
            if dni_confir == i["dni"]:
                cta_transf = i["dni"]
                i["saldo"] -= transf
                for j in self.banco:
                    if dni_transf == j["dni"]:
                        cta_benef = j["dni"]
                        j["saldo"] += transf
        return print("la cuenta {cta_transf} transfirio ${transf} a la cuenta de '{cta_transf}' ".format(cta_transf = cta_transf, transf = transf, cta_benef = cta_benef))
    
    # metodo lista de TODOS los morosos
    def imprimir_morosos(self):
        for i in self.banco:
            return print("Los morosos tienen el dni: {self.morosos}".format(self = self))
    
    # metodo que imprime TODAS las cuenatas
    def imprimir_cuentas(self):
        return print(self.cuentas)
        
# instancia

per = Persona(12345, "cuenta ahorro", 12, 500)
per1 = Persona(56789, "cuenta papa", 154, -200)
per2 = Persona(1111, "cuentasss", 22, -2555)

per.agregarCtaBancaria(12345)
per.agregarNuevaCtaBancaria(12345,"Cuenta 2")
per.agregarNuevaCtaBancaria(12345,"Cuenta 5")
per.agregarNuevaCtaBancaria(12345,"Cuenta 6")

per1.agregarCtaBancaria(56789)
per1.agregarNuevaCtaBancaria(56789,"Cuenta 3")
per1.agregarNuevaCtaBancaria(56789,"Cuenta 31")

per.agregar_Banco()
per1.agregar_Banco()
per2.agregar_Banco()

print("-----")

per.ver_banco()

per.verificacion(12345)
per1.verificacion(56789)
per1.imprimir_morosos()
print("-----------")
per.transferencia(12345, 500, 56789)

per2.ingresarSaldo(1111, 250000)

per.ver_banco()
per.verificacion(12345)
per1.verificacion(56789)
per2.verificacion(1111)
per1.imprimir_morosos()

per2.retirarSaldo(1111, 50000)
per.ver_banco()