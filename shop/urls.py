"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from shop import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from store.views import detail, index, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('product/<slug:slug>/', product_detail, name='product'),
    path('store/', include('store.urls', namespace='store')),  # Inclure les URLs de l'application 'store'
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Permet de servir les fichiers médias en mode DEBUG

