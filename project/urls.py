from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from channels.api import ChannelViewSet, ItemViewSet

api_router = routers.DefaultRouter()
api_router.register(r"drink", ChannelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_router.urls)),
]