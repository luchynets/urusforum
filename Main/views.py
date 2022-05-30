from django.shortcuts import render, redirect
from .models import Post, Comment
from django.conf import settings 
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth import authenticate, login, logout

import random
from datetime import date

names = {
		'luchynets': ('Ігор', 'Лучинець'), 
		'pasyuk': ('Володимир', 'Пасюк'), 
		'kashanyk': ('Володимир', 'Кашаник'), 
		'masendych': ('Андрій', 'Масендич'), 
		'sarakun': ('Денис', 'Саракун'),
		'tymchischin': ('Остап', 'Тимчишин')
}

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		posts = Post.objects.all()[::-1]
		random_post = random.choice(posts)
		photos = [str(post.photo)[str(post.photo).find('/'):] for post in posts]
		return render(request, 'Main/index.html', {'posts': posts, 'random_post': random_post, 'photos': photos, 'username': request.user.username})
	else: 
		return redirect('login')

def post(request, id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			comment = Comment()
			comment.post_id = int(id)
			comment.first_name = names[request.user.username][0]
			comment.last_name = names[request.user.username][1]
			comment.text = request.POST['text']
			comment.post_date = date.today()
			comment.save()
			return redirect(f'/post/{id}')
		post = Post.objects.get(pk=int(id))
		comments = Comment.objects.filter(post_id=int(id))
		return render(request, 'Main/post.html', {'post': post, 'photo': str(post.photo)[str(post.photo).find('/'):], 'video': str(post.video)[str(post.video).find('/'):], 'username': request.user.username, 'comments': comments})
	else: 
		return redirect('login')

def add_post(request):
	if request.method == 'POST':
		post = Post()
		post.first_name = names[request.user.username][0]
		post.last_name = names[request.user.username][1]
		post.title = request.POST['title']
		post.text = request.POST['text']
		try:
			post.photo = request.FILES['photo']
			post.video = None
		except MultiValueDictKeyError:
			post.photo = None
			post.video = request.FILES['video']
		post.post_date = date.today()
		post.save() 
		return redirect('main') 

	return render(request, 'Main/addpost.html')

def user_login(request):
	if request.user.is_authenticated:
		return redirect('main')	
	else:
		if request.method == 'POST':
			user = authenticate(username=request.POST['login'], password=request.POST['password'])
			if user is not None:
				login(request, user)
				return redirect('main')	
			else:
				return render(request, 'Main/login.html', {'error': 'Неправильний логін або пароль'})
		return render(request, 'Main/login.html')


def user_logout(request):
	logout(request)
	return redirect('login')