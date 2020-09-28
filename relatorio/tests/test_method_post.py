import pytest
from django.contrib.messages import get_messages
from django.urls import reverse
from relatorio.models import Consulta


@pytest.fixture
def criar_consulta():
    Consulta.objects.create(
        numero_guia=1111,
        cod_medico=1000,
        nome_medico="Fabio",
        data_consulta="2019-08-22",
        valor_consulta=100,
    )


@pytest.mark.django_db
def test_post_none_redirect(client):
    data = {"nome_medico": "", "data_consulta": ""}
    url = reverse("index")
    response = client.post(url, data=data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_post_nome_medico(client):
    data = {"nome_medico": "TALISON", "data_consulta": ""}
    url = reverse("index")
    response = client.post(url, data=data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_data_consulta(client):
    data = {"nome_medico": "", "data_consulta": "2018-06-10"}
    url = reverse("index")
    response = client.post(url, data=data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_nome_medico_e_data_consulta(client):
    data = {"nome_medico": "TALISON", "data_consulta": "2018-06-10"}
    url = reverse("index")
    response = client.post(url, data=data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_nome_medico_e_data_consulta_diferentes_message(client):
    data = {"nome_medico": "TALISON", "data_consulta": "2017-08-10"}
    url = reverse("index")
    response = client.post(url, data=data)
    messages = list(get_messages(response.wsgi_request))
    assert str(messages[0]) == "Não há registro para o filtro."


@pytest.mark.django_db
def test_page_errada_redirect(client):
    data = {"page": 10}
    url = reverse("index")
    response = client.get(url, data=data)
    assert response.status_code == 200
