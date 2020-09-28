from django.db import models


class Consulta(models.Model):

    numero_guia = models.IntegerField()
    cod_medico = models.IntegerField()
    nome_medico = models.CharField("Nome", max_length=100)
    data_consulta = models.DateField()
    valor_consulta = models.DecimalField(max_digits=7, decimal_places=2)


class Exame(models.Model):

    numero_guia_consulta = models.ForeignKey(
        Consulta, related_name="exames", on_delete=models.CASCADE
    )
    exame = models.CharField("Exame", max_length=50)
    valor_exame = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.exame)