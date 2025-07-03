from django.contrib import admin
from django.urls import path
from projects.views import home  # Убедитесь в правильности импорта

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Главная страница
]