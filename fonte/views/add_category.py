from django.shortcuts import render
from fonte.forms import CategoryForm
from . import index
from django.contrib.auth.decorators import login_required

@login_required
def add_category(request):
    form  = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, '../templates/adicionar_categoria.html', {'form':form})