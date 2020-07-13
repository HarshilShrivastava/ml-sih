from django.shortcuts import render
from .models import Tree
# Create your views here.

def index(request):
    qs=Tree.objects.all().order_by('-Level')
    context={'qs':qs}
    return render(request,"index.html",context)
