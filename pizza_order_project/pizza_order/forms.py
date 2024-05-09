# pizza_order/forms.py
from django import forms

class PizzaOrderForm(forms.Form):
    SIZE_CHOICES = (
        ('5.00', 'Small ($5.00)'),
        ('8.00', 'Medium ($8.00)'),
        ('10.00', 'Large ($10.00)'),
    )

    CRUST_CHOICES = (
        ('1.00', 'Thin Crust (+$1.00)'),
        ('2.00', 'Thick Crust (+$2.00)'),
        ('3.00', 'Stuffed Crust (+$3.00)'),
    )

    TOPPING_CHOICES = (
        ('1.00', 'Pepperoni (+$1.00)'),
        ('0.50', 'Mushrooms (+$0.50)'),
        ('1.50', 'Sausage (+$1.50)'),
        ('0.75', 'Onions (+$0.75)'),
        ('0.50', 'Olives (+$0.50)'),
        ('0.75', 'Peppers (+$0.75)'),
    )

    size = forms.ChoiceField(label='Size', choices=SIZE_CHOICES, widget=forms.RadioSelect)
    crust = forms.ChoiceField(label='Crust', choices=CRUST_CHOICES, widget=forms.RadioSelect)
    toppings = forms.MultipleChoiceField(label='Toppings', choices=TOPPING_CHOICES, widget=forms.CheckboxSelectMultiple)
