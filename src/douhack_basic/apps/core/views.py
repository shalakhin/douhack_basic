from django.shortcuts import render, redirect

from registrations.forms import ParticipantForm


def home(request):
    """
    Home page with basic registration
    """
    form = ParticipantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # TODO add messages here
            form.save()
            return redirect('home')
    context = {
        'form': form        
    }
    return render(request, 'home.html', context)
