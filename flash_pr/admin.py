from django.contrib import admin
from django import forms
from .models import Users, Sellers, Games, Reviews, Orders, OrderItems

class UsersForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Введите новый пароль'}),
        required=False,
        label='Пароль'
    )
    
    class Meta:
        model = Users
        fields = ['full_name', 'mail', 'password']

class UsersAdmin(admin.ModelAdmin):
    form = UsersForm
    list_display = ['full_name', 'mail', 'registration_date']
    list_filter = ['registration_date']
    search_fields = ['full_name', 'mail']
    readonly_fields = ['registration_date']
    
    fieldsets = [
        ('Основная информация', {
            'fields': ['full_name', 'mail', 'password']
        }),
        ('Дополнительная информация', {
            'fields': ['registration_date'],
            'classes': ['collapse']
        })
    ]

class SellersAdmin(admin.ModelAdmin):
    list_display = ['login', 'user', 'rating', 'registration_date']
    list_filter = ['rating', 'registration_date']
    search_fields = ['login', 'user__full_name']
    readonly_fields = ['registration_date']

class GamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'genre', 'platform', 'price', 'release_date']
    list_filter = ['genre', 'platform', 'release_date']
    search_fields = ['title', 'description']

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'game', 'rating', 'review_date']
    list_filter = ['rating', 'review_date']
    search_fields = ['user__full_name', 'game__title']
    readonly_fields = ['review_date']

class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_date']
    list_filter = ['status', 'created_date']
    search_fields = ['user__full_name']
    readonly_fields = ['created_date', 'updated_date']
    inlines = [OrderItemsInline]

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'game', 'quantity', 'price']

# Регистрация моделей в админке
admin.site.register(Users, UsersAdmin)
admin.site.register(Sellers, SellersAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
