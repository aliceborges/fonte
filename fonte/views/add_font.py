from django.shortcuts import render
from fonte.models import Category
from fonte.forms import FontForm
from . import show_category
from django.contrib.auth.decorators import login_required

@login_required
def add_font(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category=None

    form = FontForm()
    if request.method == 'POST':
        form = FontForm(request.POST)
        if form.is_valid():
            if category:
                font = form.save(commit=False)
                font.category = category
                font.views = 0
                font.save()
                return show_category(request, category_name_slug)
            else:
                print(form.errors)

    context_dict = {'form':form, 'category':category}
    return render(request, '../templates/adicionar_fonte.html', context_dict)