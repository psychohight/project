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
from django.urls import include, path
from store.views import add_to_cart, cart, checkout_success, index, product_detail, delete_cart, create_checkout_session, stripe_webhook
from accounts.views import login_user, logout_user, signup, profile

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
    path('login/', login_user, name='login'),
    path('cart/', cart, name='cart'),
    path('cart/success', checkout_success, name='checkout-success'),
    path('cart/create-checkout-session', create_checkout_session, name='create-checkout-session'),
    path('cart/delete', delete_cart, name='delete-cart'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Permet de servir les fichiers médias en mode DEBUG

