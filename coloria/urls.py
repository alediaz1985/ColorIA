from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.analisis.urls')),  # 👈 Esta línea conecta la app 'analisis'
]
