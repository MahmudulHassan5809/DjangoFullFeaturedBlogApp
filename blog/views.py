from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .models import Post

# Create your views here.

def createBlog(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		if title and content:
			author = request.user;
			post = Post(title=title,content=content,author=author)
			post.save()
			messages.success(request,'Post Created SuccessFully')
			return redirect('users:myposts')
		else:
			messages.warning(request,'Filed Must Be Filled')
			return redirect('blog:createBlog')
	else:
		return render(request,'blog/create.html')


def home(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 4)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'blog/home.html',{'posts' : posts})

def show(request,post_id):
	postById = get_object_or_404(Post,pk=post_id)
	return render(request,'blog/show.html',{'post' : postById})


def deleteBlog(request,post_id):
	if request.method == 'POST':
		author_id = get_object_or_404(Post,pk=post_id).author_id
		current_user = request.user.id
		if author_id == current_user:
			post = Post.objects.filter(pk = post_id)
			post.delete()
			messages.success(request,'Post Deleted SuccessFully')
			return redirect('users:dashboard')
	else:
		messages.warning(request,'You Dont Have Permission')
		return redirect('blog:show',post_id = post_id)

def editBlog(request,post_id):
	author_id = get_object_or_404(Post,pk=post_id).author_id
	if request.user.id == author_id:
		post = get_object_or_404(Post,pk=post_id)
		#return HttpResponse(post)
		return render(request , 'blog/edit.html',{'post' : post})
	else:
		messages.warning(request,'You Dont Have Permission')
		return redirect('blog:show',post_id = post_id)


def updateBlog(request,post_id):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		if title and content:
			post = get_object_or_404(Post,pk=post_id)
			post.title = title
			post.content = content
			post.save()
			messages.success(request,'Post Updated SuccessFully')
			return redirect('blog:show',post_id = post_id)
		else:
			messages.warning(request,'Filed Must Be Filled')
			return redirect('blog:editBlog',post_id = post_id)
	else:
		messages.warning(request,'You Dont Have Permission')
		return redirect('blog:editBlog',post_id = post_id)




def about(request):
	return render(request,'blog/about.html')
