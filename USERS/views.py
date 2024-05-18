# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group  # Import Group model
from .forms import SignUpForm
from django.http import HttpResponse
from .forms import EventForm
from .forms import Event


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.groups.filter(name='endusers').exists():
                login(request, user)
                return redirect('enduser_dash')  # Redirect to enduserdashboard
    else:
        form = AuthenticationForm()
    return render(request, 'USER_templates/login.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='endusers')  # Replace 'YourGroupName' with the name of your group
            user.groups.add(group)  # Add the user to the group
            return HttpResponse("Hello world!")
    else:
        form = SignUpForm()
    return render(request, 'USER_templates/signup.html', {'form': form})
@login_required
def enduser_dash(request):
    
    if request.user.groups.filter(name='endusers').exists():
        return render(request, 'enduser_dash.html', {'user': request.user})
    else:
        return  ('access_denied') 
    
    #for django form 

def event_booking(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('payment_page', event_id=event.id)
    else:
        form = EventForm()
    return render(request, 'USER_templates/event_booking.html', {'form': form})

def payment_page(request, event_id):
    event = Event.objects.get(id=event_id)
    # Process payment here
    if request.method == 'POST':
        # Process payment and redirect to user dashboard
        return redirect('user_dashboard')
    return render(request, 'payment_page.html', {'event': event})

def user_dashboard(request):
    # Retrieve user's event booking history
    events = Event.objects.all()  # This is just a placeholder, you should filter events by user
    return render(request, 'user_dashboard.html', {'events': events})
