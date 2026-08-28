# Urban Routes - Pruebas Automatizadas de UI (E2E)

## 📌 ¿Qué es esto?
Suite de pruebas automatizadas de interfaz de usuario (UI) para la aplicación web de movilidad **Urban Routes**. Simula el flujo completo (End-to-End) de un usuario al solicitar un viaje bajo la tarifa *Comfort*.

## 🎯 Producto bajo prueba y Objetivo
* **Funcionalidad bajo prueba:** Proceso completo de reserva de taxi, validando selección de tarifas, registro telefónico por SMS, métodos de pago, requerimientos adicionales (manta, helados) y confirmación del conductor.
* **Objetivo:** Verificar la estabilidad de la interfaz y la integración asíncrona de la app para asegurar que el usuario complete su pedido sin fallos bloqueantes en el flujo principal (*Happy Path*).

## 💡 Decisiones clave y Mentalidad QA
* **Patrón Page Object Model (POM):** Separación de los localizadores e interacciones UI de los scripts de prueba para facilitar el mantenimiento técnico.
* **Manejo de Asincronía:** Implementación de *waits explícitos* (`WebDriverWait` y `expected_conditions`) para prevenir fallos por renderizado diferido de elementos web.
* **Datos de prueba parametrizados:** Centralización de variables e inputs en `data.py` para evitar datos fijos en el código.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.10+
* **Automatización:** Selenium WebDriver
* **Framework de Pruebas:** Pytest
* **Estructura:** Page Object Model (POM)

## 📂 Estructura del Repositorio
* `data.py`: Datos de prueba parametrizados (URLs, teléfonos, tarjetas, etc.).
* `test_main.py`: Clases del Page Object Model (POM) y suite de pruebas ejecutables con Pytest.
* `README.md`: Documentación y contexto del proyecto.

## 🚀 Instrucciones para Ejecutar las Pruebas

### Prerrequisitos
* Python 3.10+ e instalado Google Chrome.

### Pasos de ejecución
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/jucesar2122/qa-project-Urban-Routes-es.git](https://github.com/jucesar2122/qa-project-Urban-Routes-es.git)
   cd qa-project-Urban-Routes-es
