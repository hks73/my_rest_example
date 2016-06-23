###############################################################
from django.shortcuts import render,render_to_response
from restapp.models import user
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
#################################################################

#Using this function we can see the all user name and their user  ids 
def userList(request):
	return render(request,'user_list.html',
											{'user_list':user.objects.all()}	)

#Get the full  user details onclick user name
def userDetails(request,id):
	return render(request,'user.html',
										{'user':user.objects.get(pk=id)}	)

# Delete function for deleting the object using user id
def deleteUserDetails(request, id):
    obj = user.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/User/')

# Post function to  post data from form to database using post request
def postDetails(request):
    if request.method == 'POST':
        name = request.POST.get('user_name', '')
        email = request.POST.get('user_email', '')
        stream = request.POST.get('user_stream', '')
        user_obj = user(user_name=name, user_email=email,user_stream=stream)
        user_obj.save()
        return HttpResponseRedirect('/User/')
