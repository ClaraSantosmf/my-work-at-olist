from audioop import reverse
from http import HTTPStatus
from django.urls import reverse

from olist.core.models import Autor



def test_endpoint_autor_funcionando(client, db):
    autor = Autor.objects.create(nome='J.K Rowling')

    response = client.get(reverse('lista-autores'))

    assert response.status_code == HTTPStatus.OK
    assert response.json()['data'] == [{'id': autor.id, 'nome': 'J.K Rowling'}]

