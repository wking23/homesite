from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.
def index(request):
    return render(request, 'index_template.html', {'title': 'William King'})