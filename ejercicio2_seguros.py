# Archivo: ejercicio2_seguros.py

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


class SistemaSeguros:
    def __init__(self):
        # Diccionario para almacenar la Cola de cada servicio: {num_servicio: Cola()}
        self.colas_servicios = {}
        # Diccionario para llevar el conteo histórico de turnos asignados por servicio
        self.contadores_turnos = {}

    def registrar_llegada(self, servicio):
        # Si el servicio no existe aún, inicializamos su cola y su contador
        if servicio not in self.colas_servicios:
            self.colas_servicios[servicio] = Cola()
            self.contadores_turnos[servicio] = 0

        # Incrementamos el turno para ese servicio y lo encolamos
        self.contadores_turnos[servicio] += 1
        numero_atencion = self.contadores_turnos[servicio]
        self.colas_servicios[servicio].encolar(numero_atencion)

        print(f"-> Cliente registrado en Servicio {servicio}. "
              f"Su número de atención es: {numero_atencion} "
              f"(Personas en espera: {self.colas_servicios[servicio].tamanio()})")

    def atender_cliente(self, servicio):
        # Verificamos si existen clientes esperando en ese servicio
        if servicio not in self.colas_servicios or self.colas_servicios[servicio].esta_vacia():
            print(f"-> [Aviso] No hay clientes en espera para el Servicio {servicio}.")
            return

        numero_llamado = self.colas_servicios[servicio].desencolar()
        print(f"-> Llamando al cliente número {numero_llamado} del Servicio {servicio}.")


def iniciar_aplicacion():
    sistema = SistemaSeguros()
    print("=== SISTEMA DE ATENCIÓN - COMPAÑÍA DE SEGUROS ===")
    print("Comandos disponibles:")
    print("  C + número de servicio (Ej. C1 o C 1) : Llegada de cliente")
    print("  A + número de servicio (Ej. A1 o A 1) : Atender cliente")
    print("  S                                     : Salir del sistema\n")

    while True:
        entrada = input("Ingrese comando: ").strip().upper()

        if not entrada:
            continue

        if entrada == "S":
            print("Cerrando el sistema de atención...")
            break

        accion = entrada[0]
        resto = entrada[1:].strip()

        # Validamos que la acción sea C o A y que el número de servicio sea un entero válido
        if accion in ("C", "A") and resto.isdigit():
            numero_servicio = int(resto)
            if accion == "C":
                sistema.registrar_llegada(numero_servicio)
            elif accion == "A":
                sistema.atender_cliente(numero_servicio)
        else:
            print("-> [Error] Formato inválido. Use 'C' o 'A' seguido del número de servicio (Ej: C1, A2) o 'S' para salir.")


if __name__ == "__main__":
    iniciar_aplicacion()