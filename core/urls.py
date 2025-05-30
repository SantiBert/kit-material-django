from django.urls import path
from .views import IndexView, ResgitrarView, HeadersView, AboutUsView, BlogView, BlogPostView, ContacUsview, Landingview, LoginView, PricingView, ShoppingCartView, EcommerceView, ProductPageView, ProfilePageView, SignupView

app_name = "core"

urlpatterns = [
    path("", view=IndexView.as_view(), name="home"),
    path("register/", view=ResgitrarView.as_view(), name="register"),
    path("headers/", view=HeadersView.as_view(), name="headers"),
    path("about-us/", view=AboutUsView.as_view(), name="about-us"),
    path("blog/", view=BlogView.as_view(), name="blog"),
    path("blog-post/", view=BlogPostView.as_view(), name="post"),
    path("contact-us/", view=ContacUsview.as_view(), name="contact-us"),
    path("landing-page/", view=Landingview.as_view(), name="landing-page"),
    path("login/", view=LoginView.as_view(), name="login"),
    path("pricing/", view=PricingView.as_view(), name="pricing"),
    path("shopping-cart/", view=ShoppingCartView.as_view(), name="shopping-cart"),
    path("ecommerce/", view=EcommerceView.as_view(), name="ecommerce"),
    path("product-page/", view=ProductPageView.as_view(), name="product-page"),
    path("profile/", view=ProfilePageView.as_view(), name="profile"),
    path("signup/", view=SignupView.as_view(), name="signup"),
]
