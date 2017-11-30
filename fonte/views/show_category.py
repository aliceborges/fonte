from django.shortcuts import render
from fonte.models import Category, Font

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        font = Font.objects.filter(category=category)

        context_dict['font'] = font
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category']= None
        context_dict['font'] = None

    return render(request, '../templates/categoria.html', context_dict)