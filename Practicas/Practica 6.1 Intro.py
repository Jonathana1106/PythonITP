#####################################################################

class Carro:
    def __init__(self, marcaCarro, modeloCarro, añoCarro):
        self.marcaCarro= marcaCarro
        self.modeloCarro = modeloCarro
        self.añoCarro = añoCarro
        self.km = 0

    def mostrar(self):
        print(self.marcaCarro)
        print(self.modeloCarro)
        print(self.añoCarro)
        print(self.km)
        
    def marca(self):
        print(self.marcaCarro)
    
    def modelo(self):
        print(self.modeloCarro)

    def año(self):
        print(self.añoCarro)

    def viaje(self, kms):
        self.km += kms

    def estado(self):
        if self.km > 100000:
            print ("Fuera de Garantía")
        elif (self.km % 5000 == 0):
            print ("Revisión")
        else:
            print ("Normal")

###################################################################

class Empleado:
    def __init__(self, Numerodeempleado, Nombre, Salariohora):
        self.Nombre = Nombre
        self.Numerodeempleado = Numerodeempleado
        self.Salariohora = Salariohora

    def mostrar(self):
        print(self.Numerodeempleado)
        print(self.Nombre)
        print(self.Salariohora)

    def calculoSalario(self, horas):
        self.horas = horas
        if self.horas >= 0:
            pago = self.horas * self.Salariohora
            return pago
        else:
            return "Ingrese una cantidad de horas significativa."

#################################################################

class Cliente:
    def __init__(self, Numerodecliente, Nombre):
        self.Numerodecliente = Numerodecliente
        self.Nombre = Nombre
        self.Saldo = 0

    def mostrar(self):
        print(self.Numerodecliente)
        print(self.Nombre)
        print(self.Saldo)

    def registraDoc(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto
        if self.tipo == "fa":
            self.Saldo = self.Saldo + self.monto
            self.monto = 0
        elif self.tipo == "re":
            self.Saldo = self.Saldo - self.monto
            self.monto = 0
            if self.Saldo < 0:
                return "Su saldo es menor que 0, por favor recargue su cuenta."
        else:
            return "Ingrese un tipo valido: 'fa' o 're'."

    def saldo(self):
        print(self.Saldo)
        
#################################################################

class TerraMedia:
    def __init__(self, Nombrepelicula, Sala, Fecha, Hora, Categoria):
        self.Nombrepelicula = Nombrepelicula
        self.Sala = Sala
        self.Fecha = Fecha
        self.Hora = Hora
        self.Categoria = Categoria

    def mostrar(self):
        print(self.Nombrepelicula)
        print(self.Sala)
        print(self.Fecha)
        print(self.Hora)
        print(self.Categoria)

    def retornaFecha(self):
        print(self.Fecha)

    def actualizahora(self, hora):
        self.hora = hora
        self.Hora = self.hora

    def actualizafecha(self, fecha):
        self.fecha = fecha
        self.Fecha = self.fecha

#####################################################################
class Persona:
    def __init__(self, Nombre, Apellido, Edad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad

    def mostrar(self):
        print("Nombre: ", self.Nombre)
        print("Apellidp: ", self.Apellido)
        print("Edad: ", self.Edad)

###################################################################

class Curso:
    def __init__(self, Listaestudiantes):
        self.Listaestudiantes = Listaestudiantes

    def mostrar(self):
        return self.Listaestudiantes

    def agregaEstudiantes(self, Nuevosestudiantes):
        self.Nuevosestudiantes = Nuevosestudiantes
        self.Listaestudiantes = self.Listaestudiantes + self.Nuevosestudiantes

    def Elimina(self, Nombreestudiante):
        if not isinstance(Nombreestudiante, str):
            return "Error"
        i = 0
        while i < len(self.Listaestudiantes):
            if self.Listaestudiantes[i] == Nombreestudiante:
                del self.Listaestudiantes[i]
            i = i+1
        

######################################################################





        
