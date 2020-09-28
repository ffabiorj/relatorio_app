import pytest
from relatorio.models import Consulta, Exame


@pytest.fixture
def criar_consulta():
    return Consulta.objects.create(
        numero_guia=1111,
        cod_medico=1000,
        nome_medico="Fabio",
        data_consulta="2019-08-22",
        valor_consulta=100,
    )


@pytest.fixture
def criar_exame(criar_consulta):
    return Exame.objects.create(
        numero_guia_consulta=criar_consulta, exame="HEMOGRAMA", valor_exame=20
    )


@pytest.mark.django_db
def test_criar_acao(criar_consulta):
    assert Consulta.objects.count() == 1


@pytest.mark.django_db
def test_str_consulta(criar_consulta):
    assert criar_consulta.__str__() == 1111


@pytest.mark.django_db
def test_criar_exame(criar_exame):
    assert Exame.objects.count() == 1


@pytest.mark.django_db
def test_str_exame(criar_exame):
    assert criar_exame.__str__() == "HEMOGRAMA"