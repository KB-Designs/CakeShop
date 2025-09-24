from decimal import Decimal
from django.conf import settings
from products.models import Product, ProductVariant

CART_SESSION_ID = 'cart'   # key to store cart in session


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            # If cart doesn't exist, create empty dict
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, variant_id, quantity=1, replace=False, message_on_cake=""):
        """Add a product variant to the cart or update its quantity."""
        variant = ProductVariant.objects.get(id=variant_id)
        key = str(variant_id)

        if key not in self.cart:
            self.cart[key] = {
                'quantity': 0,
                'price': str(variant.price),
                'message_on_cake': message_on_cake,
            }

        if replace:
            self.cart[key]['quantity'] = quantity
        else:
            self.cart[key]['quantity'] += quantity

        self.save()

    def remove(self, variant_id):
        """Remove a variant from the cart."""
        key = str(variant_id)
        if key in self.cart:
            del self.cart[key]
            self.save()

    def __iter__(self):
        """Iterate over cart items and fetch variant + product objects."""
        variant_ids = self.cart.keys()
        variants = ProductVariant.objects.filter(id__in=variant_ids)
        cart = self.cart.copy()

        for variant in variants:
            item = cart[str(variant.id)]
            item['variant'] = variant
            item['product'] = variant.product
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count total items in cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Calculate total cost of items."""
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        """Remove cart from session."""
        if CART_SESSION_ID in self.session:
            del self.session[CART_SESSION_ID]
            self.save()

    def save(self):
        self.session.modified = True
