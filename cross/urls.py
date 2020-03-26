from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'memes', views.MemeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
