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

mesa_1 = Mesa(1)
mesa_2 = Mesa(2)
mesa_3 = Mesa(3)

mesa_1.agregar("Ensalada", 2500)
mesa_1.agregar("Filete", 2300)
mesa_2.agregar("Hamburguesa", 3200)
mesa_2.agregar("Pasta", 2500)
mesa_3.agregar("Ensalada", 1800)
mesa_3.agregar("Jugo", 1200)

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


class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paredes = []

    def agregar_pared(self, largo, alto):
        pared = Pared(largo, alto)
        self.paredes.append(pared)

    def calcular_superficie_total(self):
        superficie_total = 0
        for pared in self.paredes:
            superficie_total += pared.superficie
        return superficie_total

    def calcular_litros_pintura(self, rendimiento_litros):
        superficie_total = self.calcular_superficie_total()
        litros_pintura = superficie_total / rendimiento_litros
        return litros_pintura

habitacion1 = Habitacion("Sala")

habitacion1.agregar_pared(5, 4)  
habitacion1.agregar_pared(5, 4)  
habitacion1.agregar_pared(5, 4)
habitacion1.agregar_pared(5, 4)  

rendimiento_litros = 10
superficie_total = habitacion1.calcular_superficie_total()
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