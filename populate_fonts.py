import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fontes.settings')

import django
django.setup()
from fonte.models import Category, Font

def populate():
    fontes_desenhadas = [
        {"name":"Brainfish Rush",
         "url": "https://dl.dafont.com/dl/?f=brainfish_rush"},
        {"name":"Keys of Paradise",
         "url":"https://dl.dafont.com/dl/?f=keys_of_paradise"},
        {"name":"Sketch 3D",
         "url":"https://dl.dafont.com/dl/?f=sketch_3d"},
        {"name":"BubbleGum",
         "url":"https://dl.dafont.com/dl/?f=bubblegum"}
    ]

    fontes_serif = [
        {"name":"The Queen",
         "url":"https://dl.dafont.com/dl/?f=the_queen"},
        {"name":"Editors",
         "url":"https://dl.dafont.com/dl/?f=editors"},
        {"name":"Cinzel",
         "url":"https://dl.dafont.com/dl/?f=cinzel"}
    ]

    fontes_celtas = [
        {"name":"Viking",
         "url":"https://dl.dafont.com/dl/?f=viking"},
        {"name":"Stonecross",
         "url":"https://dl.dafont.com/dl/?f=stonecross"},
        {"name":"Stonehenge",
         "url":"https://dl.dafont.com/dl/?f=stonehenge"}
    ]

    cats = {"Desenhadas": {"Font": fontes_desenhadas},
                  "Celtas": {"Font": fontes_celtas},
                  "Serif": {"Font": fontes_serif}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for f in cat_data["Font"]:
            add_fonts(c, f["name"], f["url"])

    for c in Category.objects.all():
        for f in Font.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(f)))

def add_fonts (cat, name, url, views = 0):
    f = Font.objects.get_or_create(category=cat, name=name)[0]
    f.url = url
    f.views = views
    f.save()
    return f

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__== '__main__':
    print("Populando o banco de fontes...")
    populate()
