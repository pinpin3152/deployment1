from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import Email


def index(request):
	if request.method == "POST":
		results = Email.objects.addEmail(email=request.POST['email'])
		if results == False:
			messages.add_message(request, messages.INFO, 'The email is not valid')
			return redirect ('/')
		else:
			messages.add_message(request, messages.INFO, 'Great! The email ({}) is fine! created on {}'.format(results.email, results.created_at))
			
			results = Email.objects.getAll()
			context = {
				'all_emails' : results
			}
			print context
			return render(request, 'success.html', context)
	else:
		return render(request, 'index.html')