from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)