from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('activosit.urls')),  # Incluimos las URLs de la app 'activosit'
]

