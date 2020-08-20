"""creative URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
# Solo para testing, hostear correctamente mas adelante


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name="index"),
    path('register/', views.ResgitrarView, name="Register"),
    path('headers/', views.HeadersView, name="headers"),
    path('about-us/', views.AboutUsView, name="about-us"),
    path('blog/', views.BlogView, name="blog"),
    path('blog-post/', views.BlogPostView, name="post"),
    path('contac-us/', views.ContacUsview, name="contac-us"),
    path('landing-page/', views.Landingview, name="landing-page"),
    path('login/', views.LoginView, name="login"),
    path('pricing/', views.PricingView, name="pricing"),
    path('shopping-cart/', views.ShoppingCartView, name="shopping-cart"),
    path('ecommerce/', views.EcommerceView, name="ecommerce"),
    path('product-page/', views.ProductPageView, name="product-page"),
    path('profile/', views.ProfilePageView, name="profile"),
    path('signup/', views.SignupView, name="signup"),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
