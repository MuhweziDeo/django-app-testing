from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User,AnonymousUser
from products.views import product_detail
from mixer.backend.django import mixer
import pytest
from products.models import Product


@pytest.mark.django_db
class TestViews:

    def test_product_view_authenticated(self):
        mixer.blend(Product)
        path = reverse('detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = product_detail(request, pk=1)
        assert response.status_code == 200

    def test_product_view_unathenticated(self):
        mixer.blend(Product)
        path = reverse('detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = product_detail(request, pk=1)
        assert response.status_code == 302
