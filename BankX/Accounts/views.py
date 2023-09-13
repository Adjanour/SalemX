from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm, AccountCreationForm
from django.contrib.auth.decorators import login_required
from .models import Account
import uuid


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('create_account')
        else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




def index(request):
    return render(request, 'index.html')

def create_account(request):
    if request.method == 'POST':
        # Save the form data to the database.
        user = request.user
        account = Account.objects.create(
            user=user,
            account_number = generate_id(),
            account_type=request.POST['account_type'],
            initial_deposit=request.POST['initial_deposit'],
            account_pin=request.POST['account_pin'],
            account_balance=request.POST['initial_deposit'],
        )

        # Redirect the user to the accoun overview page
        return redirect('account_overview')

    else:
        form = AccountCreationForm(request.POST)
        # Render the form with errors.
        return render(request, 'create_account.html', {'form': form})


@login_required
def account_overview(request):
    user = request.user
    account = Account.objects.get(user=user)
    context = {'user': user, 'account': account}
    return render(request, 'account_overview.html', context)

@login_required
def deposit(request):
    if request.method == 'POST':
        # Handle deposit logic here (update account balance)
        return redirect('account_overview')
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    if request.method == 'POST':
        # Handle withdrawal logic here (update account balance)
        return redirect('account_overview')
    return render(request, 'withdraw.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Handle account deletion logic here
        return redirect('logout')  # Redirect to logout page after deleting the account
    return render(request, 'delete_account.html')

def generate_id():
    unique_id = uuid.uuid4()
    id_str = str(unique_id)
    return id_str

def list_accounts(request):
    account = Account.objects.all()
    context = {'accounts': account}
    return render(request, 'accounts.html', context)

