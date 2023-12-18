from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import *
from .models import Address
from cart_manage.models import Cart, Order


User = get_user_model()

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('home')


    return render(request, 'authentication/signup.html', context={'form': form})

def login(request):
    next_url = request.GET.get('next', None)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Essayez de récupérer l'utilisateur par nom d'utilisateur
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is None:
            # Si la récupération du nom d'utilisateur échoue, essayez de récupérer l'utilisateur par email
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                user = None

        if user is None:
            # Si la récupération par email échoue, essayez de récupérer l'utilisateur par numéro de téléphone
            try:
                user = User.objects.get(phone_number=username)
            except User.DoesNotExist:
                user = None

        if user is not None and user.check_password(password):
            django_login(request, user)
            return redirect('home')
        else:
            if user is not None:
                error_message = 'Mot de passe incorrect.'
            else:
                error_message = 'Aucune correspondance trouvée pour le nom d\'utilisateur, l\'email ou le numéro de téléphone.'
            return render(request, 'authentication/login.html', {'error': error_message})

    return render(request, 'authentication/login.html')

@login_required
def profile(request):
    user = request.user
    cart = Cart.objects.get(user=request.user)
    number_of_items_in_cart = cart.items.count()
    orders = Order.objects.filter(user=request.user).all()
    return render(request, 'authentication/profile.html', {'user': user, 'number_of_items_in_cart': number_of_items_in_cart, 'orders':orders})

@login_required
def settings(request):
    user = request.user

    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = SettingsForm(instance=user)

    cart = Cart.objects.get(user=request.user)
    number_of_items_in_cart = cart.items.count()  # Supposons que vous avez un champ 'items' pour stocker les produits dans le panier

    return render(request, 'authentication/settings.html', {'form': form, 'number_of_items_in_cart': number_of_items_in_cart,})

@login_required
def manage_address(request, address_id=None):
    user = request.user
    instance = None

    if address_id:
        instance = get_object_or_404(Address, id=address_id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            # Gérer la suppression d'une adresse
            if instance:
                instance.delete()
                return redirect('settings')
        else:
            form = AddressForm(request.POST, instance=instance)
            if form.is_valid():
                address = form.save(commit=False)
                address.user = user
                address.save()
                return redirect('settings')
    else:
        form = AddressForm(instance=instance)

    template = 'authentication/manage_address.html'

    cart = Cart.objects.get(user=request.user)
    number_of_items_in_cart = cart.items.count()  # Supposons que vous avez un champ 'items' pour stocker les produits dans le panier

    context = {
        'form': form,
        'address_id': address_id,
        'number_of_items_in_cart': number_of_items_in_cart,
    }

    return render(request, template, context)

@login_required
def delete_account(request):
    cart = Cart.objects.get(user=request.user)
    number_of_items_in_cart = cart.items.count()  # Supposons que vous avez un champ 'items' pour stocker les produits dans le panier

    if request.method == 'POST':
        # Si l'utilisateur confirme la suppression du compte
        if request.POST.get('confirm_delete'):
            user = request.user
            # Supprimez le compte de l'utilisateur
            user.delete()
            return redirect('home')  # Redirige vers la page d'accueil après la suppression du compte
        else:
            return redirect('setiings')  # Redirige vers la page de setiings si la suppression est annulée
    else:
        return render(request, 'authentication/delete_account.html', {'number_of_items_in_cart': number_of_items_in_cart,})

