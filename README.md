# Gestión de Inmuebles

Aplicación web para centralizar la gestión de propiedades, propietarios, agentes, visitas y operaciones inmobiliarias.

## Estructura del proyecto

```text
Gestión_De_Inmuebles/
├── manage.py
├── core/                 # Núcleo y configuración de Django
├── inmuebles_app/        # Aplicación del dominio inmobiliario
├── index.html            # Template de bienvenida
├── 404.html              # Template de error personalizado
├── styles.css            # Estilos de la interfaz
└── app.js                # Interacciones del frontend
```

## Crear el ambiente virtual

Desde la carpeta raíz del proyecto:

```powershell
python -m venv nombre_ambiente
```

En este equipo, si el comando `python` no es reconocido, utiliza directamente la instalación detectada:

```powershell
& 'C:\Users\user\AppData\Local\Programs\Python\Python313\python.exe' -m venv nombre_ambiente
```

Actívalo en Windows:

```powershell
.\nombre_ambiente\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, ejecuta una vez:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Para salir del ambiente:

```powershell
deactivate
```

## Instalar Django

```powershell
pip install -r requirements.txt
```

## Iniciar el servidor

```powershell
python manage.py runserver
```

También puedes ejecutar Django sin activar el ambiente, usando su intérprete directamente:

```powershell
& '.\nombre_ambiente\Scripts\python.exe' manage.py runserver
```

La aplicación quedará disponible en `http://127.0.0.1:8000/`.

- Inicio: `/`
- Página 404 de prueba: `/404/`
- Administración Django: `/admin/`

Para comprobar el error personalizado, visita cualquier URL inexistente, por ejemplo `http://127.0.0.1:8000/ruta-inexistente/`.

## Dependencias

El proyecto utiliza Django 6.1 para administrar la configuración del núcleo, el enrutamiento URL, las vistas HTML, el servidor de desarrollo y el panel de administración. Las dependencias transitorias son instaladas automáticamente por Django y quedan aisladas dentro del ambiente virtual.
