from django.db import models

int_habilitado = 1
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_www = "WWW"
str_email = "Email"
str_telefono = "Teléfono"
str_fecha_nac = "Fecha Nacimiento"


class Pais(models.Model):
    nombre = models.CharField("País", max_length=60, null=False)
    nacionalidad = models.CharField("Nacionalidad", max_length=50, null=True, blank=True)
    iso_2 = models.CharField("ISO 2", max_length=2, null=False)
    iso_3 = models.CharField("ISO 3", max_length=3, null=False)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)

    class Meta:
        db_table_comment = "Información de países para nacionalidad de propietarios, agentes y clientes."

    def __str__(self):
        return self.nombre


class Region(models.Model):
    codigo = models.CharField(str_codigo, max_length=2, null=False)
    region = models.CharField("Región", max_length=50, null=False)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)

    class Meta:
        db_table_comment = "Regiones de Chile, data de SUBDERE."

    def __str__(self):
        return self.region


class Provincia(models.Model):
    codigo = models.CharField(str_codigo, max_length=3, null=False)
    provincia = models.CharField("Provincia", max_length=50, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=False)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)

    class Meta:
        db_table_comment = "Provincias de Chile, data de SUBDERE. Pertenece a una región específica."

    def __str__(self):
        return self.provincia


class Comuna(models.Model):
    codigo = models.CharField(str_codigo, max_length=5, null=False)
    comuna = models.CharField("Comuna", max_length=60, null=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=False)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)

    class Meta:
        db_table_comment = "Comunas de Chile, data de SUBDERE. Pertenece a una provincia específica."

    def __str__(self):
        return self.comuna


class Direccion(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False)
    calle = models.CharField("Calle", max_length=100, null=False)
    numero = models.CharField("Número", max_length=10, null=True, blank=True)
    departamento = models.CharField("Dpto/Oficina", max_length=10, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Dirección normalizada vinculada a comuna."

    def __str__(self):
        num = f" {self.numero}" if self.numero else ""
        dpto = f" Depto/Of {self.departamento}" if self.departamento else ""
        return f"{self.calle}{num}{dpto}, {self.comuna}"


class Inmobiliaria(models.Model):
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    razon_social = models.CharField("Razón Social", max_length=120, null=True, blank=True)
    rut = models.CharField("RUT", max_length=12, null=True, blank=True)
    web = models.URLField(str_www, null=True, blank=True)
    correo = models.EmailField(str_email, null=True, blank=True)
    telefono = models.CharField(str_telefono, max_length=15, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Datos de la empresa inmobiliaria o sucursal."

    def __str__(self):
        return self.nombre


class TipoInmueble(models.Model):
    tipo = models.CharField("Tipo Inmueble", max_length=50, null=False)
    descripcion = models.CharField(str_descripcion, max_length=255, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Tipos de inmueble (casa, departamento, oficina, local, etc.)."

    def __str__(self):
        return self.tipo


class TipoOperacion(models.Model):
    operacion = models.CharField("Tipo Operación", max_length=30, null=False)
    descripcion = models.CharField(str_descripcion, max_length=255, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Modalidades de negocio (Venta, Arriendo, Arriendo Temporal)."

    def __str__(self):
        return self.operacion


class EstadoInmueble(models.Model):
    estado = models.CharField("Estado", max_length=30, null=False)
    descripcion = models.CharField(str_descripcion, max_length=255, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Estados del inmueble (Disponible, Reservado, Vendido, Arrendado)."

    def __str__(self):
        return self.estado


class Caracteristica(models.Model):
    nombre = models.CharField("Característica", max_length=50, null=False)
    descripcion = models.CharField(str_descripcion, max_length=255, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Amenidades y características de las propiedades."

    def __str__(self):
        return self.nombre


class Propietario(models.Model):
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    rut = models.CharField("RUT", max_length=12, null=True, blank=True)
    correo = models.EmailField(str_email, null=True, blank=True)
    telefono = models.CharField(str_telefono, max_length=15, null=True, blank=True)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    fecha_nacimiento = models.DateField(str_fecha_nac, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Datos de propietarios de los inmuebles."

    def __str__(self):
        return self.nombre


class Agente(models.Model):
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    rut = models.CharField("RUT", max_length=12, null=False)
    codigo_agente = models.CharField(str_codigo, max_length=15, null=False)
    correo = models.EmailField(str_email, null=True, blank=True)
    telefono = models.CharField(str_telefono, max_length=15, null=True, blank=True)
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, null=True, blank=True)
    fecha_contratacion = models.DateField("Fecha Contratación", null=False)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Datos de los agentes inmobiliarios."

    def __str__(self):
        return f"{self.nombre} ({self.codigo_agente})"


class Cliente(models.Model):
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    rut = models.CharField("RUT", max_length=12, null=False)
    correo = models.EmailField(str_email, null=True, blank=True)
    telefono = models.CharField(str_telefono, max_length=15, null=True, blank=True)
    nacionalidad = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    fecha_nacimiento = models.DateField(str_fecha_nac, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Datos de clientes y potenciales interesados."

    def __str__(self):
        return self.nombre


class Inmueble(models.Model):
    codigo = models.CharField(str_codigo, max_length=20, null=False)
    titulo = models.CharField("Título", max_length=150, null=False)
    descripcion = models.TextField(str_descripcion, null=True, blank=True)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, null=False)
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, null=False)
    estado = models.ForeignKey(EstadoInmueble, on_delete=models.CASCADE, null=False)
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, null=True, blank=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=False)
    agente_encargado = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=False)
    precio = models.DecimalField("Precio", max_digits=14, decimal_places=2, null=False)
    gastos_comunes = models.DecimalField("Gastos Comunes", max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    superficie_total = models.DecimalField("Superficie Total (m²)", max_digits=8, decimal_places=2, null=True, blank=True)
    superficie_construida = models.DecimalField("Superficie Construida (m²)", max_digits=8, decimal_places=2, null=True, blank=True)
    habitaciones = models.IntegerField("Habitaciones", default=1)
    banos = models.IntegerField("Baños", default=1)
    estacionamientos = models.IntegerField("Estacionamientos", default=0)
    bodegas = models.IntegerField("Bodegas", default=0)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Data de inmuebles registrados en la inmobiliaria."

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"


class InmuebleCaracteristica(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=False)
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE, null=False)
    detalle = models.CharField("Detalle", max_length=100, null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Características asignadas a cada inmueble."

    def __str__(self):
        return f"{self.inmueble.codigo} - {self.caracteristica.nombre}"


class Visita(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=False)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    fecha_visita = models.DateTimeField("Fecha Visita", null=False)
    comentarios = models.TextField("Comentarios", null=True, blank=True)
    estado_visita = models.CharField("Estado Visita", max_length=20, default='Agendada')
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Registro y seguimiento de visitas a los inmuebles."

    def __str__(self):
        return f"Visita {self.inmueble.codigo} por {self.cliente.nombre} ({self.fecha_visita})"


class HistorialEstadoInmueble(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=False)
    estado_anterior = models.ForeignKey(
        EstadoInmueble, on_delete=models.CASCADE, related_name='historial_estados_previos', null=True, blank=True
    )
    estado_nuevo = models.ForeignKey(
        EstadoInmueble, on_delete=models.CASCADE, related_name='historial_estados_nuevos', null=False
    )
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True, blank=True)
    motivo = models.CharField("Motivo del Cambio", max_length=255, null=True, blank=True)
    fecha_cambio = models.DateTimeField(str_fecha_creacion, auto_now_add=True)

    class Meta:
        db_table_comment = "Registro de auditoría de cambios de estado del inmueble."

    def __str__(self):
        ant = self.estado_anterior.estado if self.estado_anterior else "Inicial"
        return f"{self.inmueble.codigo}: {ant} -> {self.estado_nuevo.estado}"


class OperacionContrato(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=False)
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, null=False)
    fecha_operacion = models.DateTimeField("Fecha Operación", auto_now_add=True)
    monto_final = models.DecimalField("Monto Final", max_digits=14, decimal_places=2, null=False)
    observaciones = models.TextField("Observaciones", null=True, blank=True)
    habilitado = models.BooleanField(int_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Registro histórico de cierre de contratos y operaciones."

    def __str__(self):
        return f"Operación {self.inmueble.codigo} - {self.tipo_operacion.operacion} ({self.cliente.nombre})"
