from django.contrib import admin
from .models import Sellers, Users, Games, Reviews, Orders, OrderItems

# Простая регистрация без кастомных настроек
admin.site.register(Sellers)
admin.site.register(Users)
admin.site.register(Games)
admin.site.register(Reviews)
admin.site.register(Orders)
admin.site.register(OrderItems)
