# Archivo: ejercicio1_suma_colas.py

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def tamanio(self):
        return len(self.items)

    def obtener_elementos(self):
        return list(self.items)


def sumar_colas(cola_a, cola_b):
    """
    Recibe dos colas con números enteros y devuelve una nueva cola
    con sus elementos sumados uno a uno.
    """
    cola_resultado = Cola()

    # Mientras ambas colas tengan elementos, se desencolan y se suman
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        valor_a = cola_a.desencolar()
        valor_b = cola_b.desencolar()
        cola_resultado.encolar(valor_a + valor_b)

    # Si alguna de las colas tenía más elementos que la otra, se agregan al final
    while not cola_a.esta_vacia():
        cola_resultado.encolar(cola_a.desencolar())

    while not cola_b.esta_vacia():
        cola_resultado.encolar(cola_b.desencolar())

    return cola_resultado


# --- Bloque principal de prueba ---
if __name__ == "__main__":
    cola_a = Cola()
    cola_b = Cola()

    datos_a = [3, 4, 2, 8, 12]
    datos_b = [6, 2, 9, 11, 3]

    for num in datos_a:
        cola_a.encolar(num)

    for num in datos_b:
        cola_b.encolar(num)

    # Guardamos copias de las listas para mostrar la tabla comparativa en consola
    vista_a = cola_a.obtener_elementos()
    vista_b = cola_b.obtener_elementos()

    # Ejecutamos la función
    cola_res = sumar_colas(cola_a, cola_b)
    vista_res = cola_res.obtener_elementos()

    # Impresión con el formato del ejercicio
    print(f"{'Cola A':^10} {'Cola B':^10} {'Cola Resultado':^16}")
    print("-" * 38)
    for a, b, r in zip(vista_a, vista_b, vista_res):
        print(f"{a:^10} {b:^10} {r:^16}")