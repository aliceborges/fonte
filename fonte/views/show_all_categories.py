from django.shortcuts import render
from fonte.models import Category, Font

def show_all_categories(request):
    context_dict = {}

    try:
        category = Category.objects.all()
        font = Font.objects.filter(category=category)

        context_dict['font'] = font
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category']= None
        context_dict['font'] = None

    return render(request, '../templates/categorias.html', context_dict)