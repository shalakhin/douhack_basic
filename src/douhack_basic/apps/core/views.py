from django.shortcuts import render


def home(request):
    """
    Home page with basic registration
    """
    context = {}
    return render(request, 'home.html', context)
