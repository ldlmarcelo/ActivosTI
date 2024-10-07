# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dispositivo(models.Model):
    iddispositivo = models.AutoField(primary_key=True)
    nomenclatura = models.CharField(unique=True, max_length=45)
    nrodeserie = models.CharField(max_length=45, blank=True, null=True)
    jiracompra = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivo'


class Historialubicacion(models.Model):
    idhistorialubicacion = models.AutoField(db_column='idhistorialUbicacion', primary_key=True)  # Field name made lowercase. The composite primary key (idhistorialUbicacion, dispositivo_iddispositivo, ubic_especifica_idubic_especifica) found, that is not supported. The first column is selected.
    fecha = models.DateTimeField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    dispositivo_iddispositivo = models.ForeignKey(Dispositivo, models.DO_NOTHING, db_column='dispositivo_iddispositivo')
    ubic_especifica_idubic_especifica = models.ForeignKey('UbicEspecifica', models.DO_NOTHING, db_column='ubic_especifica_idubic_especifica')

    class Meta:
        managed = False
        db_table = 'historialubicacion'
        unique_together = (('idhistorialubicacion', 'dispositivo_iddispositivo', 'ubic_especifica_idubic_especifica'),)


class UbicEspecifica(models.Model):
    idubic_especifica = models.AutoField(primary_key=True)  # The composite primary key (idubic_especifica, ubicacion_idubicacion) found, that is not supported. The first column is selected.
    ubic_especifica = models.CharField(max_length=45)
    ubicacion_idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion_idubicacion')

    class Meta:
        managed = False
        db_table = 'ubic_especifica'
        unique_together = (('idubic_especifica', 'ubicacion_idubicacion'), ('ubic_especifica', 'ubicacion_idubicacion'),)


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    ubicacion = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'ubicacion'
