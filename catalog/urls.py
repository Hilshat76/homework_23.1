from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('',home, name='home'),
    path('products/<int:pk>/',products_detail, name='products_detail'),
    path('contacts/',contacts,name='contacts')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)