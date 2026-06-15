class ChatbotSoporte:
    """Clase que gestiona la logica de negocio y la maquina de estados

    para el chatbot automatizado de Soporte Tecnico Nivel 1.
    """

    def __init__(self):
        """Inicializa la base de datos simulada, los registros y las sesiones."""
        # Base de datos simulada de empleados (Entidad: Usuario)
        self._usuarios_db = {"LEG-4829": "Juan Perez", "LEG-1234": "Maria Lopez"}

        # Historial de almacenamiento (Entidad: Ticket_Soporte)
        self.tickets_registrados = []

        # Estructura interna para el control de la Maquina de Estados
        self._sesion = {
            "estado": "ESTADO_INICIAL",
            "legajo": None,
            "categoria": None,
        }

    def obtener_estado_actual(self):
        """Retorna el estado logico actual de la sesion.

        Returns:
            str: Nombre del estado actual.
        """
        return self._sesion["estado"]

    def reiniciar_sesion(self):
        """Restablece los parametros de la sesion al estado inicial."""
        self._sesion = {
            "estado": "ESTADO_INICIAL",
            "legajo": None,
            "categoria": None,
        }

    def procesar_entrada(self, mensaje_usuario):
        """Procesa el texto recibido y ejecuta la transicion de estados correspondiente.

        Args:
            mensaje_usuario (str): Texto enviado por el usuario.

        Returns:
            str: Respuesta textual generada por el sistema.
        """
        mensaje = mensaje_usuario.strip()
        estado_actual = self._sesion["estado"]

        if estado_actual == "ESTADO_INICIAL":
            return self._procesar_inicio()

        if estado_actual == "ESPERANDO_LEGAJO":
            return self._validar_legajo(mensaje)

        if estado_actual == "ESPERANDO_OPCION":
            return self._evaluar_opcion_menu(mensaje)

        if estado_actual == "ESPERANDO_CONFIRMACION":
            return self._evaluar_compuerta_resolucion(mensaje)

        if estado_actual == "ESPERANDO_DESCRIPCION":
            return self._registrar_escalado(mensaje)

        return "ERROR: Estado no reconocido."

    def _procesar_inicio(self):
        """Genera el saludo inicial y avanza el estado."""
        self._sesion["estado"] = "ESPERANDO_LEGAJO"
        return (
            "[BOT]: Bienvenido al asistente virtual de Soporte Tecnico Nivel 1.\n"
            "[BOT]: Por favor, ingresa tu numero de LEGAJO para comenzar (Ej: LEG-1234):"
        )

    def _validar_legajo(self, legajo):
        """Verifica la existencia del legajo en la base de datos corporativa."""
        if legajo in self._usuarios_db:
            self._sesion["legajo"] = legajo
            self._sesion["estado"] = "ESPERANDO_OPCION"
            nombre = self._usuarios_db[legajo]
            return (
                f"\n[BOT]: Legajo verificado. Hola {nombre}.\n"
                "[BOT]: Por favor, selecciona el numero de tu inconveniente:\n"
                "       1 - Problemas con el Correo Institucional\n"
                "       2 - Restablecer Contrasena de Red\n"
                "       3 - Fallas en Internet / VPN"
            )

        return (
            "\n[BOT]: ERROR: El legajo ingresado no existe en el sistema.\n"
            "[BOT]: Por favor, verifica los datos e ingresalo nuevamente:"
        )

    def _evaluar_opcion_menu(self, opcion):
        """Asigna el instructivo correspondiente segun la opcion seleccionada."""
        if opcion in ["1", "2", "3"]:
            self._sesion["categoria"] = opcion
            self._sesion["estado"] = "ESPERANDO_CONFIRMACION"

            if opcion == "1":
                instructivo = "Instructivo de Correo: Intenta ingresar desde el navegador en modo incognito o borra la cache."
            elif opcion == "2":
                instructivo = "Instructivo de Contrasena: Ingresa al portal corporativo e introduce tu clave anterior."
            else:
                instructivo = "Instructivo de VPN: Desconecta el enrutador de tu hogar por 10 segundos y vuelve a conectar."

            return (
                f"\n[BOT]: {instructivo}\n"
                "[BOT]: ¿Se soluciono el problema?\n"
                "       1 - SI, esta resuelto.\n"
                "       2 - NO, sigo con problemas."
            )

        return (
            "\n[BOT]: ERROR: Opcion no valida.\n"
            "[BOT]: Por favor, responde unicamente con el numero 1, 2 o 3:"
        )

    def _evaluar_compuerta_resolucion(self, confirmacion):
        """Maneja la bifurcacion logica de la compuerta segun el exito del usuario."""
        if confirmacion == "1":
            self.tickets_registrados.append(
                {
                    "id_ticket": len(self.tickets_registrados) + 1,
                    "legajo": self._sesion["legajo"],
                    "categoria": self._sesion["categoria"],
                    "estado_ticket": "RESUELTO",
                    "comentario": "Resuelto mediante instructivo automatizado.",
                }
            )
            print(
                "\n[BOT]: El problema ha sido marcado como RESUELTO y el ticket se ha cerrado."
            )
            print(
                "[BOT]: Gracias por utilizar el servicio. ¡Que tengas un buen dia!"
            )
            self.reiniciar_sesion()
            return "\n--- REINICIANDO SIMULADOR PARA NUEVO USUARIO ---\n"

        if confirmacion == "2":
            self._sesion["estado"] = "ESPERANDO_DESCRIPCION"
            return "\n[BOT]: Entendido. Por favor, describe brevemente el error para derivarlo al equipo de soporte:"

        return (
            "\n[BOT]: ERROR: Entrada no valida.\n"
            "[BOT]: Por favor, responde 1 si se soluciono o 2 si el problema persiste:"
        )

    def _registrar_escalado(self, descripcion):
        """Almacena el ticket en estado escalado con los comentarios del usuario."""
        self.tickets_registrados.append(
            {
                "id_ticket": len(self.tickets_registrados) + 1,
                "legajo": self._sesion["legajo"],
                "categoria": self._sesion["categoria"],
                "estado_ticket": "ESCALADO",
                "comentario": descripcion,
            }
        )
        print(
            "\n[BOT]: Mensaje recibido. Se ha generado un Ticket bajo el estado ESCALADO."
        )
        print(
            "[BOT]: Un agente humano se comunicara a la brevedad. Fin de la comunicacion."
        )
        print(
            f"\n[SISTEMA - LOG INTERNO]: Ultimo ticket guardado: {self.tickets_registrados[-1]}"
        )
        self.reiniciar_sesion()
        return "\n--- REINICIANDO SIMULADOR PARA NUEVO USUARIO ---\n"


# =====================================================================
# INTERFAZ DE USUARIO (CONSOLA) - SEPARADA DE LA LOGICA DE NEGOCIO
# =====================================================================
if __name__ == "__main__":
    bot = ChatbotSoporte()

    print("=== SIMULADOR DE CHATBOT DE SOPORTE TECNICO (WHATSAPP) ===")
    print("Para salir de la simulacion, escribe 'SALIR'.")
    print("=========================================================\n")

    # Disparador del saludo inicial automático
    respuesta_inicial = bot.procesar_entrada("")
    print(respuesta_inicial)

    while True:
        entrada_usuario = input("[USUARIO]: ")

        if entrada_usuario.upper() == "SALIR":
            print("\nSimulacion finalizada de forma correcta.")
            break

        # Ejecución del motor logico de estados
        respuesta_bot = bot.procesar_entrada(entrada_usuario)

        # Si el proceso se reinicio internamente, el bot devuelve el saludo del nuevo ciclo
        if "REINICIANDO" in respuesta_bot:
            print(respuesta_bot)
            respuesta_bot = bot.procesar_entrada("")

        print(respuesta_bot)
