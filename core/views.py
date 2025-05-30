from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ResgitrarView(TemplateView):
    template_name = "register.html"

class HeadersView(TemplateView):
    template_name = "headers.html"

class AboutUsView(TemplateView):
    template_name = "about-us.html"

class BlogView(TemplateView):
    template_name = "blog.html"

class BlogPostView(TemplateView):
    template_name = "blog-post.html"

class ContacUsview(TemplateView):
    template_name = "contact-us.html"

class Landingview(TemplateView):
    template_name = "landing-page.html"

class LoginView(TemplateView):
    template_name = "login.html"

class PricingView(TemplateView):
    template_name = "pricing.html"

class ShoppingCartView(TemplateView):
    template_name = "hopping-cart.html"

class EcommerceView(TemplateView):
    template_name = "ecommerce.html"

class ProductPageView(TemplateView):
    template_name = "product-page.html"

class ProfilePageView(TemplateView):
    template_name = "profile-page.html"

class SignupView(TemplateView):
    template_name = "signup-page.html"
