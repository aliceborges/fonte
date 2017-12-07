from django.shortcuts import render
from fonte.models import Category, Font
from . import visitor_cookie_handler

def index(request):
    #request.session.set_test_cookie()
    category_list = Category.objects.order_by('name')[:6]
    font_list = Font.objects.order_by('views')[:32]

    context_dict = {'categories':category_list,
                    'fonts':font_list,
                    }

    #visitor_cookie_handler(request)
    #context_dict['visits'] = request.session['visits']

    return render(request, '../templates/index.html', context=context_dict)