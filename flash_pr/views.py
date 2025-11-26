from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Games, Sellers, Users, Reviews, Orders, OrderItems

def home_authenticated(request):
    games = Games.objects.all()[:10]
    recommended_games = Games.objects.order_by('?')[:6]
    recent_games = Games.objects.order_by('-id')[:4]
    
    context = {
        'games': games,
        'recommended_games': recommended_games,
        'recent_games': recent_games,
        'games_count': Games.objects.count(),
        'sellers_count': Sellers.objects.count(),
        'users_count': Users.objects.count(),
        'top_sellers': Sellers.objects.order_by('-rating')[:5]
    }
    
    return render(request, 'home.html', context)

@csrf_exempt
def login_view(request):
    print("=== LOGIN VIEW CALLED ===")
    print(f"Method: {request.method}")
    
    if request.method == 'POST':
        username = request.POST.get('username', 'NO_USERNAME')
        password = request.POST.get('password', 'NO_PASSWORD')
        print(f"LOGIN ATTEMPT: '{username}' / '{password}'")
        
        user = authenticate(request, username=username, password=password)
        print(f"AUTH RESULT: {user}")
        
        if user is not None:
            login(request, user)
            print(f"LOGIN SUCCESS: {user.username}")
            return redirect('home')
        else:
            print("LOGIN FAILED")
            return render(request, 'login.html', {'error': 'Wrong username or password'})
    
    print("RENDERING LOGIN FORM")
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def cart_view(request):
    return render(request, 'cart.html')

def add_to_cart(request, game_id):
    game = get_object_or_404(Games, id=game_id)
    return redirect('cart')

def new_games(request):
    new_games_list = Games.objects.order_by('-id')[:6]
    context = {'games': new_games_list}
    return render(request, 'new_games.html', context)

def sale_games(request):
    sale_games_list = Games.objects.all()[:6]
    context = {'games': sale_games_list}
    return render(request, 'sale.html', context)

def profile(request):
    return render(request, 'profile.html')

def all_games(request):
    all_games_list = Games.objects.all()
    context = {'games': all_games_list}
    return render(request, 'all_games.html', context)

def games_list(request):
    genre = request.GET.get('genre')
    platform = request.GET.get('platform')
    games = Games.objects.all()
    if genre:
        games = games.filter(genre=genre)
    if platform:
        games = games.filter(platform=platform)
    context = {'games': games}
    return render(request, 'games_list.html', context)

def game_detail(request, game_id):
    game = get_object_or_404(Games, id=game_id)
    reviews = Reviews.objects.filter(game=game)
    context = {
        'game': game,
        'reviews': reviews
    }
    return render(request, 'game_detail.html', context)

def sellers_list(request):
    sellers = Sellers.objects.all()
    context = {'sellers': sellers}
    return render(request, 'sellers_list.html', context)

def seller_detail(request, seller_id):
    seller = get_object_or_404(Sellers, id=seller_id)
    seller_games = Games.objects.filter(seller=seller)
    context = {
        'seller': seller,
        'seller_games': seller_games
    }
    return render(request, 'seller_detail.html', context)

def search(request):
    query = request.GET.get('q', '')
    games = Games.objects.filter(title__icontains=query) if query else []
    context = {
        'games': games,
        'query': query
    }
    return render(request, 'search.html', context)
