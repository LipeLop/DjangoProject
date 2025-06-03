from django.shortcuts import render, redirect
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return redirect('orders:orders_list')
    else:
        form = OrderCreateForm()

    return render(request, 'create.html', {'cart': cart, 'form': form})
def orders_list(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'orders.html', {'orders': orders})