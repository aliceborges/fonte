from django.shortcuts import render
from fonte.models import Category, Font

def show_all_fonts(request):
    context_dict = {}

    try:
        font = Font.objects.all()
        context_dict['font'] = font

    except Category.DoesNotExist:
        context_dict['font'] = None

    return render(request, '../templates/fontes.html', context_dict)