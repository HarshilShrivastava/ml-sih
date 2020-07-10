from django.shortcuts import render
from .models import Tree
# Create your views here.

def index(request):
    qs=Tree.objects.all()
    context={'qs':qs}
    return render(request,"index.html",context)
