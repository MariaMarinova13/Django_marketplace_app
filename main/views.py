from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from main.models import Item, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.forms import NewItemForm, EditItemForm
from django.db.models import Q


def homepage(request):
    return render(request, template_name='main/home.html')

def itemspage(request):

    if request.method == 'GET':
        items = Item.objects.filter(owner=None)
        categories = Category.objects.all()
        return render(request, template_name='main/items.html', context={'items': items, 'categories': categories})


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items= items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'main/browse.html', context={
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(request, id):
    item = Item.objects.get(id=id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=id)[0:3]

    return render(request, 'main/detail.html', context={"item": item,
                                                        "related_items": related_items})

@login_required
def new(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()

            messages.success(request, f'Your item was added successfully!')
            return redirect('items')
    else:
        form = NewItemForm()

    return render(request, 'main/new_item.html', context={'form':form})

@login_required
def edit(request, id):
    item = get_object_or_404(Item, id=id, added_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST or None, request.FILES or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your item was edited successfully!')
            return redirect('items')
    else:
        form = EditItemForm(instance=item)
    return render(request, 'main/edit_form.html', context={'form':form})

@login_required
def dashboard(request):
    items = Item.objects.filter(added_by=request.user)

    return render(request, 'main/my_items.html', context={'items':items})

@login_required
def delete(request, id):
    item = get_object_or_404(Item, id=id, added_by=request.user)
    item.delete()
    messages.success(request, 'Item was deleted!')

    return redirect('items')

def loginpage(request):

    if request.method == 'GET':
        return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are logged in as {user.username}')
            return redirect('items')
        else:
            messages.error(request, 'Username and Password are not a match!')
            return redirect('login')


def registerpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'You have registered your account successfully! Logged in as {user.username}')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('register')

def logoutpage(request):
    logout(request)
    messages.success(request,'You are logged out!')
    return redirect('home')
