# EJERCICIO 1
class Pedido:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.pedidos = []

    def agregar(self, nombre, precio):
        pedido = Pedido(nombre, precio)
        self.pedidos.append(pedido)

    def total(self):
        total = 0
        for pedido in self.pedidos:
            total += pedido.precio
        return total
    
    def borrar(self):
        self.pedidos = []

mesa_1 = Mesa(1)
mesa_2 = Mesa(2)
mesa_3 = Mesa(3)

mesa_1.agregar("Ensalada", 2500)
mesa_1.agregar("Filete", 2300)
mesa_2.agregar("Hamburguesa", 3200)
mesa_2.agregar("Pasta", 2500)
mesa_3.agregar("Ensalada", 1800)
mesa_3.agregar("Jugo", 1200)

mesa_1.borrar()

total_a_pagar_mesa1 = mesa_1.total()
total_a_pagar_mesa2 = mesa_2.total()
total_a_pagar_mesa3 = mesa_3.total()

print("El total a pagar en la mesa 1 es de:", total_a_pagar_mesa1)
print("El total a pagar en la mesa 2 es de:", total_a_pagar_mesa2)
print("El total a pagar en la mesa 3 es de:", total_a_pagar_mesa3)


# EJERCICIO 2
class Pared:
    def __init__(self, largo, alto):
        self.largo = largo
        self.alto = alto
        self.superficie = self.calcular_superficie()

    def calcular_superficie(self):
        return self.largo * self.alto
    
class Abertura:
        def __init__(self, largo_abertura, alto_abertura):
            self.largo_abertura = largo_abertura
            self.alto_abertura = alto_abertura
            self.superficie = self.calcular_superficie()

        def calcular_superficie(self):
            return self.largo_abertura * self.alto_abertura

class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paredes = []
        self.aberturas = []

    def agregar_pared(self, largo, alto):
        pared = Pared(largo, alto)
        self.paredes.append(pared)
        
    def agregar_abertura(self, largo_abertura, alto_abertura):
        abertura = Abertura(largo_abertura, alto_abertura)
        self.aberturas.append(abertura)

    def superficie_aberturas(self):
        superficie_total_de_aberturas = 0
        for abertura in self.aberturas:
            superficie_total_de_aberturas += abertura.superficie
        return superficie_total_de_aberturas
    
    def superficie_total_de_pared(self):
        superficie_total_de_pared = 0
        for pared in self.paredes:
            superficie_total_de_pared += pared.superficie
        return superficie_total_de_pared
    
    def superficie_total_a_pintar(self):
        superficie_pared = self.superficie_total_de_pared()
        superficie_abertura = self.superficie_aberturas()
        superfie_total_a_pintar = superficie_pared - superficie_abertura
        return superfie_total_a_pintar
        
    def calcular_litros_pintura(self, rendimiento_litros):
        superficie_total = self.superficie_total_a_pintar()
        litros_pintura = superficie_total / rendimiento_litros
        return litros_pintura

habitacion1 = Habitacion("Sala")

habitacion1.agregar_pared(5, 4) 
habitacion1.agregar_pared(5, 4)  
habitacion1.agregar_pared(5, 4)
habitacion1.agregar_pared(5, 4)  

habitacion1.agregar_abertura(2, 5)

rendimiento_litros = 10
superficie_total = habitacion1.superficie_total_a_pintar()
litros_pintura = habitacion1.calcular_litros_pintura(rendimiento_litros)

print("La superficie total a pintar en la habitación es de:", superficie_total, "metros cuadrados")
print("Los litros de pintura necesarios son:", litros_pintura)


# EJERCICIO 3
class Pais:
    def __init__(self, nombre, capital, poblacion):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = []

    def agregar_limitrofe(self, pais):
        if pais not in self.limitrofes:
            self.limitrofes.append(pais)
            pais.agregar_limitrofe(self)

    def obtener_limitrofes(self):
        nombres_limitrofes = [pais.nombre for pais in self.limitrofes]
        return nombres_limitrofes

argentina = Pais("Argentina", "Buenos Aires", 45000000)
uruguay = Pais("Uruguay", "Montevideo", 3500000)
brasil = Pais("Brasil", "Brasilia", 210000000)
paraguay = Pais("Paraguay", "Asunción", 7000000)

argentina.agregar_limitrofe(uruguay)
argentina.agregar_limitrofe(brasil)
argentina.agregar_limitrofe(paraguay)

pais_seleccionado = argentina

limitrofes = pais_seleccionado.obtener_limitrofes()
print("Países limítrofes de", pais_seleccionado.nombre + ":")
for pais in limitrofes:
    print(pais)