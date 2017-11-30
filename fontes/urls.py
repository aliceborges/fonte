"""fontes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from fonte import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fonte/', include('fonte.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^cadastro/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^categorias/$', views.show_all_categories, name='categories'),
    url(r'^fontes/$', views.show_all_fonts, name='fonts'),
    url(r'^adicionar_categoria/$', views.add_category, name='add_category'),
    url(r'^categoria/(?P<category_name_slug>[\w\-]+)/adicionar_fonte/$',
                      views.add_font, name='add_font'),
    url(r'^categoria/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

