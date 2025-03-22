# PopcornHour 🍿

**PopcornHour** es una plataforma web diseñada para amantes del cine y las series. Permite a los usuarios explorar, calificar, comentar y discutir sobre sus películas y series favoritas. Además, ofrece funcionalidades como registro de usuarios, búsqueda de contenido, foros de discusión y más.

---

## **Características principales**

- **Registro y autenticación de usuarios**: Los usuarios pueden crear una cuenta, iniciar sesión y gestionar su perfil.
- **Catálogo de películas y series**: Los usuarios pueden buscar y ver detalles sobre películas y series, incluyendo sinopsis, reparto, duración y más.
- **Calificaciones y comentarios**: Los usuarios pueden calificar y dejar comentarios sobre las películas y series.
- **Foros de discusión**: Los usuarios pueden crear temas de discusión y participar en conversaciones con otros miembros de la comunidad.
- **Favoritos**: Los usuarios pueden guardar sus películas y series favoritas para acceder a ellas fácilmente.

---

## **Tecnologías utilizadas**

- **Frontend**: HTML, CSS, Bootstrap, Jinja2 (plantillas).
- **Backend**: Python, Flask.
- **Base de datos**: SQLite (para desarrollo), SQLAlchemy (ORM).
- **Otras herramientas**: Flask-Login (autenticación), Flask-WTF (formularios), Flask-Migrate (migraciones de la base de datos).

---

## **Instalación y uso**

### **Requisitos previos**

- Python 3.8 o superior.
- Git (opcional, para clonar el repositorio).

### **Pasos para instalar y ejecutar el proyecto**

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Black-hawk22/Popcornhour.git
   cd Popcornhour
Crea y activa un entorno virtual:

Windows:

bash
Copy
python -m venv venv
venv\Scripts\activate
macOS/Linux:

bash
Copy
python3 -m venv venv
source venv/bin/activate
Instala las dependencias:

bash
Copy
pip install -r requirements.txt
Configura la base de datos:

bash
Copy
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Ejecuta la aplicación:

bash
Copy
flask run
Abre tu navegador y visita:

Copy
http://127.0.0.1:5000
Estructura del proyecto
Copy
Popcornhour/
├── app/
│   ├── auth/               # Autenticación de usuarios
│   ├── main/               # Páginas principales
│   ├── movies/             # Gestión de películas y series
│   ├── static/             # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/          # Plantillas HTML
│   └── __init__.py         # Inicialización de la aplicación
├── migrations/             # Migraciones de la base de datos
├── documentation/          # Documentación del proyecto
├── Entregables/            # Capturas de pantalla y videos demostrativos
├── .env                    # Variables de entorno
├── .gitignore              # Archivos y carpetas ignorados por Git
├── README.md               # Este archivo
├── requirements.txt        # Dependencias del proyecto
├── config.py               # Configuración de la aplicación
└── run.py                  # Punto de entrada de la aplicación
Capturas de pantalla
Página de inicio
Página de registro
Página de detalles de película

Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama para tu contribución:

bash
Copy
git checkout -b mi-contribucion
Realiza tus cambios y haz commit:

bash
Copy
git commit -m "Añade nueva funcionalidad"
Envía un pull request.

Licencia
Este proyecto está bajo la licencia MIT.

Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Nombre: [Fernando]

Email: [fm556501@gmail.com]

GitHub: Black-hawk22

Copy

---

## **Explicación de las secciones**

1. **Título y descripción**: Presenta el proyecto de manera clara y atractiva.
2. **Características principales**: Enumera las funcionalidades clave del proyecto.
3. **Tecnologías utilizadas**: Muestra las herramientas y tecnologías que usaste.
4. **Instalación y uso**: Proporciona instrucciones claras para instalar y ejecutar el proyecto.
5. **Estructura del proyecto**: Explica la organización del código.
6. **Capturas de pantalla**: Muestra imágenes del proyecto en funcionamiento.
7. **Contribución**: Indica cómo otros pueden contribuir al proyecto.
8. **Licencia**: Especifica la licencia bajo la cual se distribuye el proyecto.
9. **Contacto**: Proporciona información para que otros puedan contactarte.

---

## **Consejos adicionales**

- **Usa emojis**: Los emojis pueden hacer que tu README sea más visual y atractivo. Por ejemplo, 🎬 para películas o 🍿 para el nombre del proyecto.
- **Mantén el formato limpio**: Usa encabezados (`#`, `##`, `###`) y listas (`-` o `*`) para organizar el contenido.
- **Incluye enlaces**: Si tienes un video demostrativo o un sitio web en vivo, añade enlaces directos.

---
