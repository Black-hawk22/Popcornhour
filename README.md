 
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


