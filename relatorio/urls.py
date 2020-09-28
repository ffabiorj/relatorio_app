from django.urls import path
from relatorio.views import index


urlpatterns = [path("", index, name="index")]
