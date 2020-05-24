from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def search(request):
    return render(request,'my_app/search.html')