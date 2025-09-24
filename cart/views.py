from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product, ProductVariant
from .utils import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    variant_id = request.POST.get('variant_id')
    quantity = int(request.POST.get('quantity', 1))
    message_on_cake = request.POST.get('message_on_cake', "")

    # Make sure variant belongs to product
    variant = get_object_or_404(ProductVariant, id=variant_id, product_id=product_id)

    cart.add(
        variant_id=variant.id,
        quantity=quantity,
        message_on_cake=message_on_cake
    )
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, variant_id):
    cart = Cart(request)
    cart.remove(variant_id)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
