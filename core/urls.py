from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "core"

router = routers.DefaultRouter()
router.register(r"todos", views.BlogViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    
]
