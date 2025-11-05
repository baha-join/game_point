from django.contrib import admin
from .models import Users, Sellers, Games, Reviews, Orders, OrderItems

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'mail', 'registration_date']
    search_fields = ['full_name', 'mail']

@admin.register(Sellers)
class SellersAdmin(admin.ModelAdmin):
    list_display = ['login', 'email', 'rating', 'registration_date']
    search_fields = ['login', 'email']

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'genre', 'platform', 'price']
    list_filter = ['genre', 'platform']
    search_fields = ['title', 'description']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'game', 'rating', 'review_date']
    list_filter = ['rating', 'review_date']
    search_fields = ['user__full_name', 'game__title']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_date']
    list_filter = ['status', 'created_date']
    search_fields = ['user__full_name']

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'game', 'quantity', 'price']
    search_fields = ['order__id', 'game__title']
