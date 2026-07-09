from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from administrativo import views

router = routers.DefaultRouter()
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrativo.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
