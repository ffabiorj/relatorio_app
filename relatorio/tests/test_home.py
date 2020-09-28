import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains


@pytest.mark.django_db
def test_home_status_code_ok(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_template_used(client):
    url = reverse("index")
    response = client.get(url)
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_h1_content(client):
    url = reverse("index")
    response = client.get(url)
    assertContains(response, "Relatório")