# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator

from blog.models import Post
from users.models import Profile


def register(request):
	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			password2 = request.POST['password2']

			if password == password2:
				if User.objects.filter(username=username).exists():
						messages.error(request , 'User Name Already Taken')
						return redirect('users:register')
				else:
					if User.objects.filter(email=email).exists():
						messages.error(request , 'Email Already Exits ')
						return redirect('users:register')
					else:
						user = User.objects.create_user(username=username,password=password,email=email)
						user.save()
						messages.success(request,'You Are Now Registered')
						return redirect('users:login')
			else:
				messages.error(request , 'Password Doest Not Match')
				return redirect('users:register_view')

		else:
			return render(request,'users/register.html')
	else:
		messages.error(request , 'You Are Already LoggedIn')
		return redirect('users:dashboard')


def login(request):
	if request.user.is_authenticated == False:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = auth.authenticate(username=username , password=password)
			if user is not None:
				auth.login(request,user)
				messages.success(request,'You Are Now LoggedIn')
				return redirect('users:dashboard')
			else:
				messages.error(request,'Invalid Credentials')
				return redirect('users:login')
		else:
			return render(request,'users/login.html')
	else:
		messages.error(request,'You Are Alredy Logged In')
		return redirect('users:dashboard')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request,'You Are Now Logged Out')
		return redirect('blog:home')

@login_required(login_url="/users/login")
def dashboard(request):
	user_posts = Post.objects.order_by('-date_posted').filter(author=request.user.id)
	return render(request,'users/dashboard.html',{'user_posts' : user_posts})

def myposts(request):
	user_posts = Post.objects.order_by('-date_posted').filter(author=request.user.id)
	paginator = Paginator(user_posts, 4)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'blog/home.html',{'posts' : posts})


@login_required(login_url="/users/login")
def profile(request,user_id):
	if request.method == 'POST':
		try:
			image = request.FILES['image']
		except MultiValueDictKeyError:
			image = False
		username = request.POST['username']
		email = request.POST['email']
		user = get_object_or_404(User,pk=user_id)
		profile = Profile.objects.get(user=user_id)
		if image == False:
			user.username = username
			user.email = email
			user.save()
			messages.success(request,'Profile Updated SuccessFully')
			return redirect('users:profile',user_id = user_id)
		else:
			user.username = username
			user.email = email
			profile.image = image
			user.save()
			profile.save()
			messages.success(request,'Profile Updated SuccessFully')
			return redirect('users:profile',user_id = user_id)

	else:
		return render(request,'users/profile.html')

def password_reset(request):
	return render(request,'users/password_reset.html')
