
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect
from .forms import CategoryEditForm, PostEditForm
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login page upon logout

def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})



# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    user = request.user
    post = Post.objects.filter(author=user)
    print(post)
    return render(request, 'dashboard.html', {'user': user, 'posts':post})


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    user = request.user  # Access authenticated user
    post = Post.objects.filter(author=user)
    print(post)
    return render(request, 'dashboard.html', {'user': user, 'posts':post})

def blog(request):
    return render(request, 'blog.html')


def edit(request):
    return render(request, 'edit.html')

def edit(request, category_id, post_id):
    category = Category.objects.get(pk=category_id)
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        category_form = CategoryEditForm(request.POST, instance=category)
        post_form = PostEditForm(request.POST, instance=post)
        if category_form.is_valid() and post_form.is_valid():
            category_form.save()
            post_form.save()
            return redirect('home')  # Redirect to home page after saving changes
    else:
        category_form = CategoryEditForm(instance=category)
        post_form = PostEditForm(instance=post)

    return render(request, 'edit.html', {'category_form': category_form, 'post_form': post_form})




def create_blog_post(request):
    user = request.user
    category = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        categor = request.POST.get('category')
        image = request.FILES.get('image')
        subscription = Subscription.objects.get(user_id=user)
        if subscription:
            plans = Plans.objects.get(plan_name=subscription.plan_id)

            if plans.plan_post:

                Post.objects.create(title=title,content=content,cat=Category.objects.get(title=categor), image=image, url='None', author=user)
            else:
                return redirect('home')
        else:
            return redirect('dashboard')

    return render(request, 'create_blog_post.html', {'cat':category})



def subscription_page(request):
    plans = Plans.objects.all()
    return render(request, 'subscription.html',{'plans':plans})


def create_subscription(request, plans):
    subscription = Subscription.objects.filter(user_id=request.user)
    plans = Plans.objects.get(plan_name=plans)
    if subscription:
        subscription = Subscription.objects.get(user_id=request.user)
        subscription.plan_id = plans
        subscription.save()
    else:
        subscription = Subscription.objects.create(user_id=request.user, plan_id=plans)
    return redirect('dashboard')