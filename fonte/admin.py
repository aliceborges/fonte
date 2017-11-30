from django.contrib import admin
from .models import Category, Font, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Font)
admin.site.register(UserProfile)