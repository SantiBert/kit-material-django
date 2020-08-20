from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
# Create your views here.


def IndexView(request):
    return render(request, 'index.html')


def ResgitrarView(request):
    return render(request, 'register.html')


def HeadersView(request):
    return render(request, 'headers.html')


def AboutUsView(request):
    return render(request, 'about-us.html')


def BlogView(request):
    return render(request, 'blog.html')


def BlogPostView(request):
    return render(request, 'blog-post.html')


def ContacUsview(request):
    return render(request, 'contact-us.html')


def Landingview(request):
    return render(request, 'landing-page.html')


def LoginView(request):
    return render(request, 'login.html')


def PricingView(request):
    return render(request, 'pricing.html')


def ShoppingCartView(request):
    return render(request, 'shopping-cart.html')


def EcommerceView(request):
    return render(request, 'ecommerce.html')


def ProductPageView(request):
    return render(request, 'product-page.html')


def ProfilePageView(request):
    return render(request, 'profile-page.html')


def SignupView(request):
    return render(request, 'signup-page.html')
