from django import template
from num2words import num2words

register = template.Library()

@register.filter
def amount_to_words(amount):
    return f"{num2words(amount).capitalize()} Naira only"