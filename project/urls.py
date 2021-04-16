from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from app.views import DesafioViewSet, Regra_CasaViewSet

api_router = routers.DefaultRouter()
api_router.register(r"desafios", DesafioViewSet)
api_router.register(r"regras", Regra_CasaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_router.urls)),
]