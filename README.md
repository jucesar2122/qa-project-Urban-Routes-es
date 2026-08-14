# Urban Routes - Pruebas Automatizadas de UI

## Descripción del Proyecto
Este proyecto contiene una suite completa de pruebas automatizadas de interfaz de usuario (UI) para la aplicación web **Urban Routes**. Las pruebas simulan el flujo completo de un usuario al solicitar un viaje con tarifa Comfort, abarcando desde la ingreción de la ruta inicial hasta la confirmación de la asignación del conductor.

### Flujo de pruebas cubierto:
1. Configuración de la dirección de origen y destino.
2. Selección de la tarifa **Comfort**.
3. Ingreso de número de teléfono y confirmación del código SMS.
4. Adición de un método de pago (Tarjeta de crédito).
5. Envío de un mensaje para el conductor.
6. Solicitud de manta y pañuelos.
7. Pedido de helados (2 unidades).
8. Confirmación del pedido y espera de la tarjeta de información del conductor.

---

## Tecnologías y Técnicas Utilizadas
- **Python 3.x**: Lenguaje de programación principal.
- **Selenium WebDriver**: Herramienta de automatización de navegador web.
- **PyTest**: Framework de ejecución de pruebas unitarias y de integración.
- **Page Object Model (POM)**: Patrón de diseño utilizado para separar la lógica de la interfaz de usuario de la lógica de los tests, mejorando la mantenibilidad y reutilización del código.
- **Waits explícitos (`WebDriverWait` y `expected_conditions`)**: Para manejar la asincronía del sitio y evitar fallos por elementos no cargados a tiempo.

---

## Estructura del Proyecto
```text
qa-project-Urban-Routes-es/
│
├── data.py          # Datos de prueba (URLs, direcciones, teléfonos, tarjetas, etc.)
├── test_main.py     # Clases del Page Object Model y la suite de pruebas PyTest
├── README.md        # Documentación del proyecto
└── .gitignore       # Archivos omitidos por Git (.venv, __pycache__, etc.)

Instrucciones para Ejecutar las Pruebas
Prerrequisitos
Tener instalado Python 3.10+ en tu sistema.

Tener Google Chrome instalado.

Pasos de ejecución
Clonar el repositorio:
git clone <URL_DE_TU_REPOSOTORIO>
cd qa-project-Urban-Routes-es
Crear y activar el entorno virtual:

En Windows:
python -m venv .venv
.venv\Scripts\activate
En macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate
Instalar dependencias:
pip install selenium pytest
Actualizar la URL del servidor:
Asegúrate de actualizar la variable urban_routes_url en el archivo data.py con un servidor activo de Urban Routes.

Ejecutar las pruebas:
Para ejecutar toda la suite de pruebas desde la terminal, usa:
pytest main.py
Si deseas ver más detalle durante la ejecución:
pytest -v main.py