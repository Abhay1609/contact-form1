from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your accounte has been created! You able to login now')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request,'user/register.html',{'form': form})
@login_required
def profile(request):
    return render(request,'user/profile.html')

