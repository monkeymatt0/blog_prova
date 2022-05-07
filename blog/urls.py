"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# In questa parte vado a comunicare quali sono gli URLS per il sito ed in particolare vado a comunicare che quando si accede al sito
# ovvero quando spawnano vanno a visualizzare la blog2.urls(che sarà un file che si deve creare all'interno della cartella).
urlpatterns = [
    path('', include('blog2.urls')),
    path('admin/', admin.site.urls),
]
