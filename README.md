 
PopcornHour
Portal web para recomendar, calificar y discutir sobre películas y series.
Descripción
PopcornHour es una plataforma que permite a los usuarios compartir opiniones sobre películas y series. Existen dos tipos de usuarios:

Moderador: Pueden subir películas/series a la plataforma para que otros usuarios las califiquen y comenten.
Estándar: Pueden calificar, comentar y discutir sobre las películas/series disponibles.

Estructura del Proyecto
Copiarpopcornhour/
│
├── app/                        # Aplicación principal
│   ├── __init__.py            # Inicialización de la aplicación
│   ├── auth/                   # Módulo de autenticación
│   │   ├── __init__.py
│   │   ├── routes.py          # Rutas para autenticación
│   │   └── forms.py           # Formularios de autenticación
│   │
│   ├── main/                   # Módulo principal
│   │   ├── __init__.py
│   │   ├── routes.py          # Rutas principales
│   │   └── forms.py           # Formularios principales
│   │
│   ├── movies/                 # Módulo de películas
│   │   ├── __init__.py
│   │   ├── routes.py          # Rutas para películas
│   │   └── forms.py           # Formularios para películas
│   │
│   ├── models.py              # Modelos de la base de datos
│   ├── static/                # Archivos estáticos (CSS, JS, imágenes)
│   └── templates/             # Plantillas HTML
│
├── migrations/                 # Migraciones de la base de datos
├── documentation/             # Documentación del proyecto
│   └── db/                    # Documentación de base de datos
│
├── Entregables/               # Carpeta con los entregables del proyecto
├── run.py                     # Script para ejecutar la aplicación
├── requirements.txt           # Dependencias del proyecto
└── config.py                  # Configuración del proyecto
Requisitos
Para ejecutar este proyecto necesitarás tener instalado Python 3.8 o superior y las siguientes dependencias:
CopiarFlask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
Flask-Login==0.5.0
Flask-WTF==0.15.1
Werkzeug==2.0.1
email-validator==1.1.3
Pillow==8.3.1
python-dotenv==0.19.0
Instalación

Clona este repositorio:

Copiargit clone https://github.com/[usuario]/popcornhour.git
cd popcornhour

Crea un entorno virtual y actívalo:

Copiarpython -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

Instala las dependencias:

Copiarpip install -r requirements.txt

Configura las variables de entorno creando un archivo .env en la raíz del proyecto:

CopiarFLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
DATABASE_URL=sqlite:///popcornhour.db

Inicializa la base de datos:

Copiarflask db init
flask db migrate -m "Initial migration"
flask db upgrade
Ejecución
Para ejecutar la aplicación:
Copiarflask run
La aplicación estará disponible en http://127.0.0.1:5000/.
Características

Registro e inicio de sesión de usuarios
Dos tipos de usuarios: moderador y estándar
Los moderadores pueden subir películas/series
Los usuarios estándar pueden calificar y comentar las películas/series
Foros de discusión para cada película/serie
Sistema de calificación con estrellas (1-5)
Búsqueda y filtrado de películas/series

## Entregables del Proyecto

### Checkpoint 1: Prototipo y estructura inicial
- [Prototipo de vistas](/Entregables/prototipo_vistas.pdf)
- [Repositorio en GitHub](https://github.com/tu-usuario/popcornhour)

### Checkpoint 2: Diseño inicial de la base de datos y flujos de usuario
- [Diagrama Entidad-Relación](/documentation/db/diagrama_entidad_relacion.png)
- [Diagramas de Flujo](/Entregables/diagramas_flujo.png)

### Checkpoint 3: Desarrollo de landing page, login y sign up
- [Capturas de pantalla](/Entregables)
- [Video de navegación](/Entregables/navegacion_cp3.mp4)

### Checkpoint 4: Implementación de autenticación y autorización
- [Video de registro](/Entregables/registro_cp4.mp4)
- [Video de inicio de sesión](/Entregables/login_cp4.mp4)
- [Video de persistencia de sesión](/Entregables/persistencia_sesion_cp4.mp4)

### Checkpoint 5: Implementación de la página inicial
- [Capturas de página inicial](/Entregables/pagina_inicial_cp5.png)
- [Video demostrativo](/Entregables/demo_pagina_inicial_cp5.mp4)