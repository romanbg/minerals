from django.db import models

# Create your models here.

GROUPS = (
    (1, "trójskośny"),
    (2, "jednoskośny"),
    (3, "rombowy"),
    (4, "tetragonalny"),
    (5, "trygonalny"),
    (6, "heksagonalny"),
    (7, "regularny")
)

class Vials(models.Model):
    id = models.SmallIntegerField(db_index=True, primary_key=True)
    name_pol = models.CharField(max_length=32)
    name_ang = models.CharField(max_length=32)
    formula = models.CharField(max_length=64)
    crystal_system = models.CharField(max_length=16, null=True, choices=GROUPS)
    space_group = models.CharField(max_length=16, null=True)
    a_axis = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    b_axis = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    c_axis = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    alpha = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    beta = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    gamma = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    Z_number = models.SmallIntegerField(null=True)
    code = models.CharField(max_length=16)

