from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from restaurant.models import Menu
from restaurant.forms import f

from .forms import UserRegistrationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = UserRegistrationForm()
    return render(request, 'signup1.html', {'form': form})



