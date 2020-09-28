# from core.models import Consulta, Exame
import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "relatorio_app.settings")
django.setup()

from relatorio.models import Consulta, Exame

Consulta.objects.all().delete()
Exame.objects.all().delete()

consultas = []
with open("contrib/consulta.csv") as file_csv:
    consulta_csv = csv.DictReader(file_csv, delimiter=";")
    for row in consulta_csv:
        consulta = Consulta(
            numero_guia=row["numero_guia"],
            cod_medico=row["cod_medico"],
            nome_medico=row["nome_medico"],
            data_consulta=row["data_consulta"],
            valor_consulta=row["valor_consulta"],
        )
        consultas.append(consulta)

Consulta.objects.bulk_create(consultas)


exames = []
with open("contrib/exames.csv") as file_csv:
    exame_csv = csv.DictReader(file_csv, delimiter=";")
    for row in exame_csv:
        numero_consulta = Consulta.objects.get(numero_guia=row["numero_guia_consulta"])
        exame = Exame(
            numero_guia_consulta=numero_consulta,
            exame=row["exame"],
            valor_exame=row["valor_exame"],
        )
        exames.append(exame)

Exame.objects.bulk_create(exames)
