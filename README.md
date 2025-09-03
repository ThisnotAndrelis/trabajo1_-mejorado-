# Formalizacion de Mi Proyecto Mini Galería Django

## Descripción
Este proyecto consiste en una mini galería de arte desarrollada con Django y Python.Aqui encontraras el contenido u pasos a seguir para implementar el uso (prueba)del proyecto. 

1. Incluye dos páginas HTML
2. Galería de imágenes escalerita(carpeta static).
3. Explicación de  perosnal de por qué me gustan las obras.
4. De acuerdo con la evalucion, un archivo con el listado de archivos ignorados ".gitignore"
5. Tambien se crearon los modelos a tablas respectivas como cliente, orden, provedores etc, y se realizaron sus migraciones respectivas.
6. Se realizo 3 registros de prueba a la tabla Cliente.

## Estructura del proyecto
proyecto__django
│
├── appdjango/                
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── proyectodjango1/          
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md




## Tecnologías usadas
- Python 3.13
- Django 5.2.5
- Git
-Github

#### Manual de uso
Requisitos previos:
Python 3.10+
Git
Virtualenv
 (opcional pero recomendado)

 # Instalación y configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ThisnotAndrelis/trabajo1_-mejorado-.git
   cd trabajo1_-mejorado-
2. Ingresa al directorio del proyecto:

3. (Opcional pero recomendado) Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

4. Instala las dependencias:
pip install -r requirements.txt

5. Ejecutar migraciones:
python manage.py migrate
6. Iniciar Servidor 
python manage.py runserver
luego habre el navegador 
http://127.0.0.1:8000/ para ver pagina 
http://127.0.0.1:8000/admin como administrador (iniciar sesion con contraseña y usuariode admin)

## Contraseña y Usuario de Admin Django:
usuario:inacap
contrasña:inacap 

## Notas
Este proyecto está pensado como práctica para el curso de Back-End 
