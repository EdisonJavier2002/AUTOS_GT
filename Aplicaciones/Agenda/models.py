from django.db import models

# Create your models here.
class Ciudad(models.Model):
    id_ciu = models.AutoField(primary_key=True)
    nombre_ciu = models.TextField()

    class Meta:
        db_table = 'ciudad'

    def __str__(self):
        return self.nombre_ciu
    
class Modelo(models.Model):
    id_mod = models.AutoField(primary_key=True)
    nombre_mod = models.TextField()

    class Meta:
        db_table = 'modelo'

    def __str__(self):
        return self.nombre_mod

class Propietario(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nombre_pro = models.TextField()
    apellido_pro = models.TextField()
    email_pro = models.CharField(max_length=50)
    telefono_pro = models.CharField(max_length=15)
    fk_id_ciu = models.ForeignKey(Ciudad, on_delete=models.CASCADE, db_column='fk_id_ciu')

    class Meta:
        db_table = 'propietario'
    
    def __str__(self):
        return f"{self.nombre_pro} {self.apellido_pro}"

class Vehiculo(models.Model):
    id_veh = models.AutoField(primary_key=True)
    fabricacion_veh = models.CharField(max_length=30)
    precio_veh = models.FloatField()
    color_veh = models.CharField(max_length=30)
    placa_veh = models.CharField(max_length=30)
    fk_id_mod = models.ForeignKey(Modelo, on_delete=models.CASCADE, db_column='fk_id_mod')
    fk_id_pro = models.ForeignKey(Propietario, on_delete=models.CASCADE, db_column='fk_id_pro')

    class Meta:
        db_table = 'vehiculo'

    def __str__(self):
        return f"Vehículo {self.placa_veh} - {self.color_veh}"