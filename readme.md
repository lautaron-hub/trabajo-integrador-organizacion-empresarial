# 🛠️ Bot de Soporte Técnico Nivel 1 - WhatsApp Simulation (Clases OOP)

Trabajo Práctico Integrador para la materia **Organización Empresarial**.  
Esta versión del simulador implementa un chatbot de WhatsApp enfocado en optimizar el proceso administrativo de Soporte Técnico Nivel 1. El desarrollo aplica **Programación Orientada a Objetos (POO)** y cumple con las convenciones de estilo requeridas por la cátedra.

---

## 📋 Arquitectura y Diseño de Software

El proyecto separa la capa de interfaz de usuario de la lógica dura del negocio:
- **Capa de Negocio (`ChatbotSoporte`):** Clase que encapsula la base de datos de usuarios. Gestiona el historial de incidentes y controla las transiciones lógicas de la Máquina de Estados.
- **Capa de Interfaz (`__main__`):** Hilo interactivo por consola integrado en el mismo archivo. Simula las entradas y salidas de texto de WhatsApp de forma asrónica.

---

## 🔧 Recomendaciones Técnicas Aplicadas

Se incorporaron las siguientes mejoras al backend:
1. **Encapsulamiento y Escalabilidad:** Centralización del flujo corporativo dentro de un Gestor de Estados de clase única.
2. **Documentación Formal (Docstrings):** Inclusión de comentarios de triple comilla para explicitar el propósito, argumentos y retornos de cada método lógico.
3. **Adherencia Estricta a PEP 8:** Formateo riguroso sin emojis, espacios limpios alrededor de operadores y nomenclatura autodescriptiva de variables.
4. **Manejo del Camino Infeliz:** Validación activa contra excepciones de tipos de datos o legajos inexistentes en los diccionarios relacionales del sistema.

---

## 🚀 Instrucciones de Despliegue Local

1. **Clonar el proyecto:**
   ```bash
   git clone https://github.com/lautaron-hub/trabajo-integrador-organizacion-empresarial.git
   cd trabajo-integrador-organizacion-empresarial
   ```

2. **Ejecutar la simulación en la terminal:**
   ```bash
   python ChatBot-funcional.py
   ```

3. **Credenciales de prueba disponibles en base de datos:**
   - `LEG-4829` (Empleado registrado: Juan Perez)
   - `LEG-1234` (Empleado registrado: Maria Lopez)
