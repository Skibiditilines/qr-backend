# Backend - Avon QR

Aqui se encuentra la api de Avon-QR. Este backend está construido con Python (FastAPI) y utiliza Neon (PostgreSQL) para la base de datos y Cloudinary para el almacenamiento de imágenes.

## Estructura del Proyecto

```
api/
├── app/
│   ├── main.py                 # Punto de entrada de la aplicación FastAPI.
│   ├── core/
│   │   ├── config.py           # Configuración de variables de entorno (Pydantic Settings).
│   │   └── database.py         # Configuración y conexión a la base de datos (SQLAlchemy).
│   ├── models/
│   │   └── user.py             # Modelos de base de datos SQLAlchemy (ej. Tablas de Usuarios).
│   │   └── concept.py
│   ├── routes/
│   │   ├── concept_routes.py               # Endpoints para la generación y redirección de QR.
│   │   └── user_routes.py             # Endpoints para la gestión de usuarios.
│   ├── schemas/
│   │   └── concept.py               # Esquemas Pydantic para validación de datos de entrada/salida.
│   │   └── user.py
│   └── services/
│       └── qr_service.py       # Lógica de negocio (Interacción con Cloudinary, generación de QR).
├── requirements.txt            # Lista de dependencias del proyecto.
├── vercel.json                 # Configuración para despliegue en Vercel.
└── .env                        # Variables de entorno (no subir al repositorio).
└── /env                        # Variables de entorno (no subir al repositorio).
```

## Dependencias Necesarias

Las siguientes librerías son requeridas para el funcionamiento del proyecto:

*   **fastapi**: Framework web moderno y rápido para construir APIs con Python.
*   **uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
*   **sqlalchemy**: ORM para interactuar con la base de datos SQL.
*   **psycopg2-binary**: Adaptador de base de datos PostgreSQL para Python.
*   **pydantic**: Validación de datos y gestión de configuraciones.
*   **pydantic-settings**: Gestión de configuraciones basada en Pydantic.
*   **python-dotenv**: Carga variables de entorno desde un archivo `.env`.
*   **cloudinary**: SDK para integración con el servicio de almacenamiento de imágenes Cloudinary.
*   **qrcode**: Librería para generar códigos QR.
*   **pillow**: Librería de procesamiento de imágenes (necesaria para `qrcode` y manipulación de imágenes).

## Instalación (Manual)

Aunque no se ha creado el entorno virtual, para instalar las dependencias se usaría:

```bash
python -m venv venv
```

```bash
env\Scripts\activate
```

```bash
pip install -r requirements.txt
```