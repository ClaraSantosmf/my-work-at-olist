from http import HTTPStatus
from django.urls import reverse


def test_endpoint_autor_funcionando(client):
    response = client.get(reverse('autores'))
    assert response.status_code == HTTPStatus.OK
