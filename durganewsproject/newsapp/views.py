from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'newsapp/index.html')

def moviesinfo(request):
    return render(request, 'newsapp/news.html')

def sportsinfo(request):
    return render(request, 'newsapp/news.html')

def politicsinfo(request):
    return render(request, 'newsapp/news.html')


