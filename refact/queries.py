from core.models import Consulta, Exame
from django.db.models import Sum, Count


def select_medicos():
    return Consulta.objects.raw(
        "SELECT 1 id, nome_medico FROM core_consulta GROUP BY nome_medico ORDER BY nome_medico ASC"
    )


def select_datas():
    return Consulta.objects.raw(
        "SELECT 1 id, data_consulta FROM core_consulta GROUP BY data_consulta ORDER BY data_consulta ASC"
    )


def returna_consultas():
    return (
        Consulta.objects.values(
            "numero_guia",
            "nome_medico",
            "data_consulta",
            "valor_consulta",
        )
        .annotate(
            gasto_consulta=Sum("exames__valor_exame"),
            qtde_exames=Count("exames__valor_exame"),
        )
        .order_by("-gasto_consulta")
    )


def lista_medicos(nome_medico):
    return (
        Consulta.objects.values(
            "numero_guia",
            "nome_medico",
            "data_consulta",
            "valor_consulta",
        )
        .annotate(
            gasto_consulta=Sum("exames__valor_exame"),
            qtde_exames=Count("exames__valor_exame"),
        )
        .filter(nome_medico=nome_medico)
        .order_by("-gasto_consulta")
    )


def lista_datas(data_consulta):
    return (
        Consulta.objects.values(
            "numero_guia",
            "nome_medico",
            "data_consulta",
            "valor_consulta",
        )
        .annotate(
            gasto_consulta=Sum("exames__valor_exame"),
            qtde_exames=Count("exames__valor_exame"),
        )
        .filter(data_consulta=data_consulta)
        .order_by("-gasto_consulta")
    )


def lista_medicos_consultas(nome_medico, data_consulta):
    return (
        Consulta.objects.values(
            "numero_guia",
            "nome_medico",
            "data_consulta",
            "valor_consulta",
        )
        .annotate(
            gasto_consulta=Sum("exames__valor_exame"),
            qtde_exames=Count("exames__valor_exame"),
        )
        .filter(nome_medico=nome_medico, data_consulta=data_consulta)
        .order_by("-gasto_consulta")
    )
