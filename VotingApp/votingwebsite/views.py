from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Election, Candidate,Login, Registration, Vote
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

# Use @login_required decorator to ensure that only logged-in users can access the register page
@login_required
def register(request):
    if request.method == 'POST':
        # Use forms instead of manually getting data from the request object
        # This helps in data validation and security
        # For now, I'll keep the manual approach, but consider using forms in the future
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create Registration instance
        registration = Registration.objects.create(
            firstname=firstname, 
            lastname=lastname, 
            email=email, 
            mobile=mobile, 
            username=username, 
            password=password
        )
        
        # Create Login instance
        login = Login.objects.create(
            username=username,
            password=password
        )
        
        # Redirect to login page
        return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # Use forms instead of manually getting data from the request object
        # This helps in data validation and security
        # For now, I'll keep the manual approach, but consider using forms in the future
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Check if the username and password match with the login model
            login = Login.objects.get(username=username, password=password)
            # If match, redirect to next page
            return redirect('home')
        except Login.DoesNotExist:
            # If no match, render login page with error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def home(request):
    # Use get\_list_or_404 to handle the case when there are no elections
    elections = Election.objects.all()
    return render(request, 'home.html', {'elections': elections})

def election_detail(request, election_id):
    # Use get_object_or_404 to handle the case when the election does not exist
    election = Election.objects.get(pk=election_id)
    # Retrieve candidates for the election
    candidates = Candidate.objects.filter(election=election)
    return render(request, 'election_detail.html', {'election': election, 'candidates': candidates})

def vote(request, election_id, candidate_id):
    # Use get_object_or_404 to handle the case when the election or candidate does not exist
    election = Election.objects.get(pk=election_id)
    candidate = Candidate.objects.get(pk=candidate_id)
    
    # Create a vote for the chosen candidate in the election
    vote = Vote.objects.create(election=election, candidate=candidate)
    
    # Increase the vote count for the candidate
    candidate.votes += 1
    candidate.save()
    
    # Redirect back to the election detail page
    return redirect('election_detail', election_id=election_id)