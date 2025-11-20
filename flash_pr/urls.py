from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_authenticated, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('new-games/', views.new_games, name='new_games'),
    path('sale/', views.sale_games, name='sale'),
    path('profile/', views.profile, name='profile'),
    path('all-games/', views.all_games, name='all_games'),
    path('games/', views.games_list, name='games_list'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('sellers/', views.sellers_list, name='sellers_list'),
    path('seller/<int:seller_id>/', views.seller_detail, name='seller_detail'),
    path('search/', views.search, name='search'),
]
