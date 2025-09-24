# orders/views.py
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.utils import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Save cart items as OrderItems with custom fields
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    size=item.get('size', ''),                # <-- new
                    icing=item.get('icing', ''),              # <-- new
                    eggs=item.get('eggs', ''),                # <-- new
                    message_on_cake=item.get('message_on_cake', '')  # <-- new
                )
            # Clear the cart after order is created
            cart.clear()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/checkout.html', {'cart': cart, 'form': form})
