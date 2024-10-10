from django.db import models
from django.utils import timezone

class Dispositivo(models.Model):
    iddispositivo = models.AutoField(primary_key=True)
    nomenclatura = models.CharField(unique=True, max_length=45)
    nrodeserie = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"{self.nomenclatura}"

    class Meta:
        managed = False
        db_table = 'dispositivo'


class Historialubicacion(models.Model):
    idhistorialubicacion = models.AutoField(db_column='idhistorialUbicacion', primary_key=True)
    dispositivo_iddispositivo = models.ForeignKey(Dispositivo, models.DO_NOTHING, db_column='dispositivo_iddispositivo')
    ubic_especifica_idubic_especifica = models.ForeignKey('UbicEspecifica', models.DO_NOTHING, db_column='ubic_especifica_idubic_especifica')
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now, blank=True, null=True)



    def __str__(self):
        return f"Historial Ubicación del {self.dispositivo_iddispositivo} en {self.ubic_especifica_idubic_especifica} el {self.fecha}"

    class Meta:
        managed = False
        db_table = 'historialubicacion'
        unique_together = (('idhistorialubicacion', 'dispositivo_iddispositivo', 'ubic_especifica_idubic_especifica'),)
        verbose_name_plural = "Historial de Ubicaciones del Dispositivo"

class UbicEspecifica(models.Model):
    idubic_especifica = models.AutoField(primary_key=True)
    ubic_especifica = models.CharField(max_length=45)
    ubicacion_idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion_idubicacion')

    def __str__(self):
        return f"{self.ubic_especifica} en {self.ubicacion_idubicacion}"

    class Meta:
        managed = False
        db_table = 'ubic_especifica'
        unique_together = (('idubic_especifica', 'ubicacion_idubicacion'), ('ubic_especifica', 'ubicacion_idubicacion'),)


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    ubicacion = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return f"Ubicación: {self.ubicacion}"

    class Meta:
        managed = False
        db_table = 'ubicacion'

