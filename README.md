# entrega_final

Guillermo Galinski

# Escuela de Surf - Proyecto Final Coderhouse

El sitio permite a los alumnos de una escuela de surf registrarse, gestionar su perfil, consultar su membresía activa. También permite la administración de clases de surf desde el panel de administrador.

---

## 🚀 Funcionalidades principales

- Registro, login y logout de usuarios
- Vista de perfil con información personal y membresía activa
- Edición de perfil y cambio de contraseña
- Página de inicio y página "Perfil de Usuario"
- Diseño responsive con Bootstrap 5.3

---

## 🧠 Tecnologías utilizadas

- Python 3.10+
- Django 4.x
- SQLite3 (solo para desarrollo)
- Bootstrap 5.3
- widget_tweaks para personalización de formularios
- Git y GitHub

---

## 📁 Estructura del proyecto

entrega_final/
│
├── escuela_surf/ # App principal (modelos: Clase, Membresía, Alumno)
├── accounts/ # App para autenticación y gestión de usuarios
├── static/ # Archivos CSS/JS/imagenes del sitio
├── templates/ # Templates HTML con herencia
├── .venv/ # Entorno virtual (ignorado por Git)
├── db.sqlite3 # Base de datos local (ignorado por Git)
├── .gitignore
├── requirements.txt
├── manage.py
