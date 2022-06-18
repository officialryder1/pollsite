from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Company
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

def Index(request):
    company = Company.objects.all()
    one = Company.objects.filter(pk__in=[4, 7])
    two = Company.objects.filter(pk__in=[12, 9])
    three = Company.objects.filter(pk__in=[2, 6])
    four = Company.objects.filter(pk__in=[10, 3])
    five = Company.objects.filter(pk__in=[1, 8])
    six = Company.objects.filter(pk__in=[5, 11])
    content = {
        'company':company,
        'one':one,
        'two':two,
        'three':three,
        'four':four,
        'five':five,
        'six':six,
    }
    return render(request, 'company/index.html', content)

def post_vote(request, pk):
    user = request.user
    post = get_object_or_404(Company, id=request.POST.get('vote'))
    liked = False
    if post.vote.filter(id=user.id).exists():
        post.vote.remove(request.user)
        liked = False
    else:
        post.vote.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('home'))

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'company/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out, Try Logging Again..."))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'company/register.html', {'form':form})

