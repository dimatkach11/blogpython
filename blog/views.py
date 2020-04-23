from django.shortcuts import render

# Create your views here.
from blog.models import Post

def home(request):
    articoli = Post.objects.filter(publish=True)
    return render(request, 'home.html', {'articoli': articoli})