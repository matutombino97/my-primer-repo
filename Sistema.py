class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca = marca  # Marca del vehículo
        self.modelo = modelo  # Modelo del vehículo
        self.año = año  # Año del vehículo

    # Método que devuelve una descripción básica del vehículo
    def descripcion(self):
        return f"El vehiculo es de marca {self.marca}, su modelo es {self.modelo}, y el año es {self.año}"

# Subclase para representar autos


class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, puertas: int):
        # Llama al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.puertas = puertas  # Número de puertas del auto

    # Método que devuelve una descripción completa del auto, sobrescribiendo el método de la clase base
    def descripcion(self):
        # Polimorfismo: Sobrescritura del método descripción para los autos
        return f"{super().descripcion()}, Puertas: {self.puertas}"

# Subclase para representar motos


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, motor: int):
        # Llama al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.motor = motor  # Tipo de motor de la moto

    # Método que devuelve una descripción completa de la moto, sobrescribiendo el método de la clase base
    def descripcion(self):
        # Polimorfismo: Sobrescritura del método descripción para las motos, en este caso añadimos el motor
        return f"{super().descripcion()}, Motor: {self.motor} tiempos"

# Subclase para representar camiones


class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, toneladas: float):
        # Llama al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.toneladas = toneladas  # Capacidad de carga del camión en toneladas

    # Método que devuelve una descripción completa del camión, sobrescribiendo el método de la clase base
    def descripcion(self):
        # Polimorfismo: Sobrescritura del método descripción para el camion, en este caso añadimos las toneladas
        return f"{super().descripcion()}, Toneladas: {self.toneladas}"

# Clase para representar una flota de vehículos


class Flota:
    def __init__(self, nombre: str):
        self.nombre = nombre  # Nombre de la flota
        self.vehiculos = []  # Lista para almacenar los vehículos en la flota

    # Método para añadir un vehículo a la lista de vehículos
    def añadir_vehiculos(self, veh: Vehiculo):
        self.vehiculos.append(veh)

    # Método para mostrar la descripción de todos los vehículos en la flota
    def mostrar_vehiculo(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.descripcion())  # Aquí se usa el polimorfismo


# Creación de instancias de autos
automovil = Auto("Toyota", "Corolla", 2021, 2)
automovil1 = Auto("Renault", "19", 1994, 4)

# Creación de instancias de motos
motocicleta = Moto("Zanella", "X", 2005, 8)
motocicleta1 = Moto("Harley Davinson", "XWED", 2000, 7)

# Creación de instancias de camiones
camionsito = Camion("Mercedez", "Benz", 1960, 30.4)
camionsito1 = Camion("Ofelio", "XTR", 2020, 15.42)

# Creación de una instancia de flota
flota = Flota("Flota numero 4")

# Añadir vehículos a la flota
flota.añadir_vehiculos(automovil)
flota.añadir_vehiculos(automovil1)
flota.añadir_vehiculos(motocicleta)
flota.añadir_vehiculos(motocicleta1)
flota.añadir_vehiculos(camionsito)
flota.añadir_vehiculos(camionsito1)

# Mostrar la descripción de todos los vehículos en la flota
flota.mostrar_vehiculo()  # Aquí se usa el polimorfismo
