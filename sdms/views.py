from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render
from sdms.forms import MyRegistrationForm, LoginForm

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def loggedin(request):
    return render(request, 'loggedin.html', {'username': request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('index.html', context_instance=RequestContext(request))

def register_user(request):
    form = MyRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounts/register_success')
    return render_to_response('register.html', {'form': form}, context_instance = RequestContext(request))

def register_success(request):
    return render_to_response('register_success.html')