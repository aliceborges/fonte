#coding:utf-8
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

def user_login (request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Sua conta está desativada.")
        else:
            print("Seus dados estão inválidos! Login: {0}. Senha: {1}.".format(username, password))
            return HttpResponse("Seus dados de login estão inválidos.")
    else:
        return render(request, '../templates/login.html', {})

    def __unicode__(self):
        return '%s' % self.name