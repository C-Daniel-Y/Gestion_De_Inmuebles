# Gestión de Inmuebles - Backend Django & REST API

Aplicación web y API REST para centralizar la gestión de propiedades inmobiliarias, actores involucrados (propietarios, agentes, clientes), control de visitas, auditoría de cambios de estado y registro histórico de operaciones.

---

## Estructura del Proyecto

```text
Gestión_De_Inmuebles/
├── manage.py
├── .env                          # Variables de entorno (SECRET_KEY, DB)
├── .env.example                  # Plantilla de referencia del .env
├── requirements.txt              # Dependencias del proyecto
├── README.md
├── core/                         # Configuración principal de Django
│   ├── settings.py               # Lee configuración desde .env
│   ├── urls.py                   # Enrutador principal (vistas, admin y API)
│   ├── asgi.py
│   └── wsgi.py
├── inmuebles_app/                # Aplicación de dominio inmobiliario
│   ├── models.py                 # Modelo de datos completo
│   ├── serializer.py             # Serializadores DRF
│   ├── views.py                  # FBV (inicio, 404) y CBV (ModelViewSets)
│   ├── urls.py                   # Rutas REST con DefaultRouter
│   ├── admin.py                  # Registro completo en Django Admin
│   ├── fixtures/                 # Datos iniciales (países, regiones, comunas)
│   └── migrations/               # Migraciones del modelo de datos
├── scripts_sql/                  # Scripts SQL obligatorios
│   └── crear_bd_usuario.sql      # Crear BD, usuario y permisos en MySQL
├── index.html                    # Plantilla de bienvenida
├── 404.html                      # Plantilla de error 404
├── styles.css
└── app.js
```

---

## Modelo de Datos

El modelo incluye 18 entidades con campos de auditoría (`habilitado`, `created_at`, `updated_at`):

**División Geográfica:** `Pais`, `Region`, `Provincia`, `Comuna`, `Direccion`

**Organización:** `Inmobiliaria`, `TipoInmueble`, `TipoOperacion`, `EstadoInmueble`, `Caracteristica`

**Actores:** `Propietario`, `Agente`, `Cliente`

**Inmuebles y Operaciones:** `Inmueble`, `InmuebleCaracteristica`, `Visita`, `HistorialEstadoInmueble`, `OperacionContrato`

---

## Instalación y Puesta en Marcha

### 1. Crear y Activar Ambiente Virtual

```powershell
python -m venv nombre_ambiente
.\nombre_ambiente\Scripts\Activate.ps1
```

### 2. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### 3. Configurar la Base de Datos

La configuración de entrega usa SQLite para que el proyecto pueda ejecutarse sin instalar un servidor de base de datos. Django crea `db.sqlite3` al aplicar las migraciones.

Si se utilizará MySQL, ejecutar `scripts_sql/crear_bd_usuario.sql` en MySQL (vía phpMyAdmin o terminal):

```sql
-- Contenido de scripts_sql/crear_bd_usuario.sql
CREATE DATABASE IF NOT EXISTS gestion_inmuebles
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_general_ci;

CREATE USER IF NOT EXISTS 'usr_inmuebles'@'%' IDENTIFIED BY 'Inmuebles2026!';
GRANT ALL PRIVILEGES ON gestion_inmuebles.* TO 'usr_inmuebles'@'%';
FLUSH PRIVILEGES;
```

### 4. Configurar Variables de Entorno

El archivo `.env` está en la raíz del proyecto y contiene la clave de Django y los parámetros de conexión. La versión de entrega usa `DB_ENGINE=sqlite3`. Para cambiar a MySQL, establecer `DB_ENGINE=mysql` y usar en `.env` el nombre de base de datos, host, puerto, usuario y contraseña creados por el script SQL. Las credenciales incluidas son temporales para evaluación; no reutilizarlas fuera de este proyecto.

### 5. Aplicar Migraciones

```powershell
python manage.py migrate
```

### 6. Cargar Datos Iniciales (Fixtures)

```powershell
python manage.py loaddata data_paises.json data_regiones.json data_provincias.json data_comunas.json data_catalogos_inmuebles.json
```

### 7. Crear Superusuario

```powershell
python manage.py createsuperuser
```

### 8. Ejecutar Servidor

```powershell
python manage.py runserver
```

---

## Endpoints REST

- **Raíz de la API:** `http://127.0.0.1:8000/inmuebles_app/`
- **Panel Admin Django:** `http://127.0.0.1:8000/admin/`

### Recursos disponibles (CRUD completo con GET, POST, PUT, PATCH, DELETE):

| Recurso | URL |
|---|---|
| Países | `/inmuebles_app/paises/` |
| Regiones | `/inmuebles_app/regiones/` |
| Provincias | `/inmuebles_app/provincias/` |
| Comunas | `/inmuebles_app/comunas/` |
| Direcciones | `/inmuebles_app/direcciones/` |
| Inmobiliarias | `/inmuebles_app/inmobiliarias/` |
| Tipos de Inmueble | `/inmuebles_app/tipos-inmueble/` |
| Tipos de Operación | `/inmuebles_app/tipos-operacion/` |
| Estados de Inmueble | `/inmuebles_app/estados-inmueble/` |
| Características | `/inmuebles_app/caracteristicas/` |
| Propietarios | `/inmuebles_app/propietarios/` |
| Agentes | `/inmuebles_app/agentes/` |
| Clientes | `/inmuebles_app/clientes/` |
| Inmuebles | `/inmuebles_app/inmuebles/` |
| Inmueble-Características | `/inmuebles_app/inmuebles-caracteristicas/` |
| Visitas | `/inmuebles_app/visitas/` |
| Historial Estados | `/inmuebles_app/historial-estados/` |
| Operaciones/Contratos | `/inmuebles_app/operaciones/` |

Cada endpoint soporta las operaciones **GET** (listar/detalle), **POST** (crear), **PUT** (actualizar completo), **PATCH** (actualizar parcial) y **DELETE** (eliminar).

---

## Tecnologías

- Python 3.13
- Django 6.1
- Django REST Framework 3.18
- MySQL (mysqlclient)
- python-decouple (variables de entorno)
