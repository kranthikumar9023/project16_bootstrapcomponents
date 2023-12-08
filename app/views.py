from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'bootstrap.html')
def ballu(request):
    return render(request,'ballu.html')