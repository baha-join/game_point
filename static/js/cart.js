// Функции для работы с корзиной
class Cart {
    constructor() {
        this.items = this.getCartFromStorage();
        this.updateCartCount();
    }

    // Получить корзину из localStorage
    getCartFromStorage() {
        const cart = localStorage.getItem('cart');
        return cart ? JSON.parse(cart) : [];
    }

    // Сохранить корзину в localStorage
    saveCartToStorage() {
        localStorage.setItem('cart', JSON.stringify(this.items));
        this.updateCartCount();
    }

    // Обновить счетчик корзины
    updateCartCount() {
        const cartCount = document.getElementById('cartCount');
        if (cartCount) {
            const totalItems = this.items.reduce((sum, item) => sum + item.quantity, 0);
            if (totalItems > 0) {
                cartCount.textContent = totalItems;
                cartCount.style.display = 'block';
            } else {
                cartCount.style.display = 'none';
            }
        }
    }

    // Добавить товар в корзину
    addItem(game) {
        const existingItem = this.items.find(item => item.id === game.id);
        
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.items.push({
                id: game.id || Date.now().toString(),
                title: game.title,
                price: game.price,
                quantity: 1,
                seller: game.seller
            });
        }
        
        this.saveCartToStorage();
        this.showAddToCartMessage(game.title);
    }

    // Показать сообщение о добавлении в корзину
    showAddToCartMessage(title) {
        // Создаем всплывающее сообщение
        const message = document.createElement('div');
        message.className = 'alert alert-success position-fixed top-0 start-50 translate-middle-x mt-3';
        message.style.zIndex = '9999';
        message.innerHTML = `
            <strong>${title}</strong> добавлен в корзину!
            <a href="/cart/" class="alert-link">Перейти в корзину</a>
        `;
        
        document.body.appendChild(message);
        
        // Удаляем сообщение через 3 секунды
        setTimeout(() => {
            message.remove();
        }, 3000);
    }

    // Получить все товары в корзине
    getItems() {
        return this.items;
    }

    // Удалить товар из корзины
    removeItem(itemId) {
        this.items = this.items.filter(item => item.id !== itemId);
        this.saveCartToStorage();
    }

    // Изменить количество товара
    updateQuantity(itemId, quantity) {
        const item = this.items.find(item => item.id === itemId);
        if (item) {
            if (quantity <= 0) {
                this.removeItem(itemId);
            } else {
                item.quantity = quantity;
            }
            this.saveCartToStorage();
        }
    }

    // Очистить корзину
    clearCart() {
        this.items = [];
        this.saveCartToStorage();
    }

    // Получить общую стоимость
    getTotalPrice() {
        return this.items.reduce((total, item) => {
            const price = parseFloat(item.price) || 0;
            return total + (price * item.quantity);
        }, 0);
    }
}

// Создаем глобальный объект корзины
const cart = new Cart();

// Обработчики для кнопок "В корзину"
document.addEventListener('DOMContentLoaded', function() {
    // Добавляем обработчики для всех кнопок "В корзину"
    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.card');
            const game = {
                id: this.dataset.gameId || Date.now().toString(),
                title: card.querySelector('.card-title').textContent,
                price: card.querySelector('.card-price').textContent.replace('Цена: ', '').replace(' RUB', ''),
                seller: {
                    login: 'gamer_shop',
                    rating: '4.75'
                }
            };
            cart.addItem(game);
        });
    });
});
