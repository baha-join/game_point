from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flash_pr.urls')),
]

# УБИРАЕМ ВСЕ static вызовы
