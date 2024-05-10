from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'registration_form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('polls:list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'login_form': form})

def poll_detail_view(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    vote_form = VoteForm(poll=poll)
    if request.method == 'POST':
        vote_form = VoteForm(poll=poll, data=request.POST)
        if vote_form.is_valid():
            selected_option = vote_form.cleaned_data['selected_option']
            # Process the vote
            return redirect('polls:detail', poll_id=poll_id)
    return render(request, 'poll_detail.html', {'poll': poll, 'vote_form': vote_form})