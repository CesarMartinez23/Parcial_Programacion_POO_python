
# Creamos la clase Vehiculo
class Vehiculo:

    # Creamos el constructor de la clase Vehiculo
    def __init__(self):

        print("*"*60)
        print("\tBienvenido al sistema de registro de vehiculos")
        print("*"*60)

        print("\n")

        # Solicitamos los datos del vehiculo
        print("-"*60)
        self.marca = input("Por favor ingrese la marca de su vehiculo: ")
        print("-"*60)
        self.modelo = input("Por favor ingrese el modelo de su vehiculo: ")
        print("-"*60)
        self.anio = int(input("Por favor ingrese el año de su vehiculo: "))
        print("-"*60)

        # Solicitamos el numero de placa del vehiculo, pero si este es mayor a 6 caracteres, entonces lo vuelve a solicitar, hasta que este sea menor a 6 caracteres o igual a 6.
        while True:
            print("-"*80)
            self.placa = input(
                "Por favor ingrese la placa de su vehiculo con un maximo de 6 digitos: ")
            print("-"*80)
            print("\n")
            if(int(len(self.placa) > 6)):
                print("*"*60)
                print("Por favor ingrese solamenten 6 digitos como maximo.")
                print("*"*60)
                print("\n")
                continue
            else:
                break

    # Creamos el metodo para mostrar los datos del vehiculo
    def mostrarInformacion(self):

        mensaje = "Su vehiculo es de la marca: " + self.marca + ", modelo: " + \
            self.modelo + ", año: " + \
            str(self.anio) + ", con numero de placa: " + self.placa

        return mensaje


# Creamos la clase Carro

class Carro(Vehiculo):

    # Creamos el constructor de la clase Carro
    def __init__(self):
        super().__init__()

        print("*"*45)
        print("\tSeleccion de tipo de vehiculos")
        print("*"*45)

        print("\n")

        # Solicitamos el tipo de vehiculo mediante un valor numerico que identfica el tipo de vehiculo, si este es diferente a las opciones, lo vuelve a solicitar hasta que sea valido.
        while True:
            print("-"*65)
            tipoCarro = int(input(
                "Seleccione el numero segun el tipo de vehiculo que posee: \n \n 1-Sedan \n 2-Pick Up \n 3-Camioneta \n 4-Rustico \n >"))
            print("-"*65)

            if(tipoCarro == 1):
                self.tipo = "Sedan"
                break
            elif(tipoCarro == 2):
                self.tipo = "Pick Up"
                break
            elif(tipoCarro == 3):
                self.tipo = "Camioneta"
                break
            elif(tipoCarro == 4):
                self.tipo = "Rustico"
                break
            else:
                print("\n")
                print("-"*65)
                print("La seleccion no esta disponible, por favor vuelva a intentarlo.")
                print("-"*65)
                print("\n")
                continue

    # Creamos el metodo para mostrar los datos del carro.
    def mostrarInformacion(self):

        mensaje = super().mostrarInformacion() + ", de tipo: " + self.tipo
        return mensaje

    # Creamos el metodo para calcular el costo de la gasolina, segun la cantida de galones que el conductor carge a su vehiculo, segun la zona del pais donde carge gasolina y segun en tipo de gasolina que este carge.
    def calcularGasolina(self):

        # Creamos una variable que almacena el costo de la gasolina por galon de gasolina, segun la zona y el tipo de gasolina.
        ZONACENTRAL = [5.95, 6.56, 5.88]
        ZONAOCCIDENTAL = [5.96, 6.57, 5.88]
        ZONAORIENTAL = [6.00, 6.61, 5.92]

        print("\n")

        print("*"*45)
        print("\tDatos de carga de gasolina")
        print("*"*45)

        print("\n")

        # Solicitamos la cantidad de galones que el conductor carge a su vehiculo.
        print("-"*65)
        self.cantidadGalones = float(
            input("Ingrese la cantidad en galones de gasolina que desea cargar: "))
        print("-"*65)

        print("\n")

        # Solicitamos la zona del pais donde el conductor carge gasolina, mediante un valor numerico que identifica la zona y asi asignamos a una variable la zona de carga de gasolina, si esta no es valida la volvemos a solicitar hasta que sea una opcion valida.
        while True:
            print("-"*65)
            zonaGasolinera = int(input(
                "Seleccione la zona donde a cargado el tanque de gasolina \n \n 1-Central \n 2-Occidental \n 3-Oriental \n >"))
            print("-"*65)

            if(zonaGasolinera == 1):
                self.zonaCarga = "Central"
                break
            elif(zonaGasolinera == 2):
                self.zonaCarga = "Occidental"
                break
            elif(zonaGasolinera == 3):
                self.zonaCarga = "Oriental"
                break
            else:
                print("\n")
                print("-"*85)
                print(
                    "La opcion seleccionada no esta disponible, por favor selecciona una opcion valida.")
                print("-"*85)
                print("\n")
                continue

        # Solicitamos el tipo de gasolina que el conductor carge a su vehiculo, mediante un valor numerico que identifica el tipo de gasolina y asi asignamos a una variable el tipo de gasolina, si esta no es valida la volvemos a solicitar hasta que sea una opcion valida.
        while True:
            print("-"*65)
            combustible = int(input(
                "Por favor seleccione el tipo de combustible de su vehiculo: \n \n 1-Regular \n 2-Super \n 3-Diesel \n >"))
            print("-"*65)

            if(combustible == 1):
                self.tipoCombustible = "Regular"
                break
            elif(combustible == 2):
                self.tipoCombustible = "Super"
                break
            elif(combustible == 3):
                self.tipoCombustible = "Diesel"
                break
            else:
                print("\n")
                print("-"*85)
                print(
                    "La opcion seleccionada no esta disponible, por favor, ingrese una opcion valida.")
                print("-"*85)
                print("\n")

                continue

        # Calculamos el costo de la gasolina, segun la zona y el tipo de gasolina y la cantidad de galones que el conductor haya cargado a su vehiculo.
        if(zonaGasolinera == 1):
            if(combustible == 1):
                self.precioPagar = (ZONACENTRAL[0] * self.cantidadGalones)
            elif(combustible == 2):
                self.precioPagar = (ZONACENTRAL[1] * self.cantidadGalones)
            elif(combustible == 3):
                self.precioPagar = (ZONACENTRAL[2] * self.cantidadGalones)
        elif(zonaGasolinera == 2):
            if(combustible == 1):
                self.precioPagar = (ZONAOCCIDENTAL[0] * self.cantidadGalones)
            elif(combustible == 2):
                self.precioPagar = (ZONAOCCIDENTAL[1] * self.cantidadGalones)
            elif(combustible == 3):
                self.precioPagar = (ZONAOCCIDENTAL[2] * self.cantidadGalones)
        elif(zonaGasolinera == 3):
            if(combustible == 1):
                self.precioPagar = (ZONAORIENTAL[0] * self.cantidadGalones)
            elif(combustible == 2):
                self.precioPagar = (ZONAORIENTAL[1] * self.cantidadGalones)
            elif(combustible == 3):
                self.precioPagar = (ZONAORIENTAL[2] * self.cantidadGalones)

        # Mostramos el costo de la gasolina.
        print("\n")
        print("*"*80)
        mensaje = str(self.cantidadGalones) + " galones de " + self.tipoCombustible + \
            " cargados en la zona " + self.zonaCarga + \
            " - $" + str(self.precioPagar)

        return print(mensaje)

# Creamos la clase para el tipo de vehiculo de tipo Camion.


class Camion(Vehiculo):

    # Creamos el metodo constructor para el tipo de vehiculo de tipo Camion.
    def __init__(self):
        super().__init__()

        # Solicitamos la cantidad de toneladas que soporta el camion.
        print("-"*70)
        self.cargaToneladas = float(
            input("Por favor ingrese la cantidad de toneladas que carga su camion: "))
        print("-"*70)

    # Creamos el metodo para mostrar los datos del tipo de vehiculo de tipo Camion.
    def mostrarInformacion(self):

        mensaje = super().mostrarInformacion() + " ,con capatidad de carga de: " + \
            str(self.cargaToneladas) + " toneladas."

        return mensaje

    # Creamos el metodo para clasificar el tipo de camion que es segun su peso en toneladas soportado.
    def clasificarCamion(self):

        if(self.cargaToneladas > 2.5 and self.cargaToneladas <= 3.5):
            self.clasificacion = "Liviano"
        elif(self.cargaToneladas > 3.5 and self.cargaToneladas <= 4.5):
            self.clasificacion = "SemiLiviano"
        elif(self.cargaToneladas > 4.5 and self.cargaToneladas <= 5.5):
            self.clasificacion = "Mediano"
        elif(self.cargaToneladas > 5.5 and self.cargaToneladas <= 7.5):
            self.clasificacion = "SemiPesado"
        elif(self.cargaToneladas > 7.5):
            self.clasificacion = "Pesado"

        print("\tSu camion se clasifica como: " + self.clasificacion)

# --------------------------------------------------------------------------------------


# Clase Vehiculo 👇.

"""
vehuculo1 = Vehiculo()
print("*"*90)
print(vehuculo1.mostrarInformacion())
print("*"*90)
"""

# Usar los ejemplos comentados arrriba.👆Solo necesita Descomentarlos.👆

# --------------------------------------------------------------------------------------

# Clase Carro 👇.

"""
carro1 = Carro()
print("\n")
print("*"*115)
print(carro1.mostrarInformacion())
print("*"*115)
print("\n")
carro1.calcularGasolina()
print("*"*80)
"""

# Usar los ejemplos comentados arrriba.👆Solo necesita Descomentarlos.👆

# --------------------------------------------------------------------------------------

# # Clase Camion 👇.

"""
camion1 = Camion()
print("\n")
print("*"*127)
print(camion1.mostrarInformacion())
print("*"*127)
print("\n")
print("*"*55)
camion1.clasificarCamion()
print("*"*55)
"""

# Usar los ejemplos comentados arrriba.👆Solo necesita Descomentarlos.👆

# --------------------------------------------------------------------------------------