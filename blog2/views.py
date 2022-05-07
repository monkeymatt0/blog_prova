from django.shortcuts import render


# Create your views here.
def index(request):
    print("******************** STO CHIAMANDO INDEX")
    return render(request, 'index.html', {})
