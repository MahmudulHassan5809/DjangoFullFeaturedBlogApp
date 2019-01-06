		username = request.POST['username']
		email = request.POST['email']
		user = get_object_or_404(User,pk=user_id)
		profile = Profile.objects.get(user=user_id)

		if username == '' and email == '':
			messages.error(request,'Field Must Be Filled')
		if bool(request.FILES.get('filepath', False)) == True:
			user.username = username
			user.email = email
			profile.image = request.FILES['myfile']
			return HttpResponse(request.FILES['image'])
			user.save()
			profile.save()
			messages.success(request,'Profile Updated SuccessFully')
			return redirect('users:profile',user_id = user_id)
		else:
			user.username = username
			user.email = email
			user.save()
			messages.success(request,'Profile Updated SuccessFully')
			return redirect('users:profile',user_id = user_id)


	if request.method == 'POST' and request.FILES['image']:
		username = request.POST['username']
		email = request.POST['email']
		image = request.FILES['image']
		user = get_object_or_404(User,pk=user_id)
		profile = Profile.objects.get(user=user_id)
		user.username = username
		user.email = email
		profile.image = image
		user.save()
		profile.save()
		messages.success(request,'Profile Updated SuccessFully')
		return redirect('users:profile',user_id = user_id)
	elif request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		user = get_object_or_404(User,pk=user_id)
		user.username = username
		user.email = email
		user.save()
		messages.success(request,'Profile Updated SuccessFully')
		return redirect('users:profile',user_id = user_id)
