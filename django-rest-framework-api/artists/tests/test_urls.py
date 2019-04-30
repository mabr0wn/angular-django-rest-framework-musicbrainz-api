import pytest
from django.conf import settings
from django.utils.encoding import force_text

@pytest.mark.urls("django-rest-framework-api.urls")
def test_urls():
    try:
        from django.urls import is_valid_path
    except ImportError:
        from django.core.urlresolvers import is_valid_path
    assert settings.ROOT_URLCONF == 'django-rest-framework-api.urls'
    assert is_valid_path('/')

