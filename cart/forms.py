# cart/forms.py
from django import forms

CAKE_SIZES = [
    ("1kg", "1kg - Ksh 2000"),
    ("1.5kg", "1.5kg - Ksh 3000"),
    ("2kg", "2kg - Ksh 4000"),
    ("3kg", "3kg - Ksh 4500"),
]

ICING_OPTIONS = [
    ("whipping cream", "Whipping Cream"),
    ("butter icing", "Butter Icing"),
    ("fondant", "Fondant"),
    ("butter cream", "Butter Cream"),
    ("fresh cream", "Fresh Cream"),
]

EGGS_OPTIONS = [
    ("with_eggs", "With Eggs"),
    ("eggless", "Eggless"),
]

class CartAddProductForm(forms.Form):
    size = forms.ChoiceField(choices=CAKE_SIZES, required=True)
    icing = forms.ChoiceField(choices=ICING_OPTIONS, required=True)
    eggs = forms.ChoiceField(choices=EGGS_OPTIONS, required=True)   # <-- new
    message_on_cake = forms.CharField(required=False, max_length=100)
    quantity = forms.IntegerField(min_value=1, initial=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
