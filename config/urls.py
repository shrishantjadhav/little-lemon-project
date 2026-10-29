from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
