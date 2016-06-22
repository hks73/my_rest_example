from django.shortcuts import render,render_to_response
from django.template import Context
from django.template.loader import get_template
from restapp.models import user
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
# Create your views here.
def user_list(request):
	return render_to_response('user_list.html',
											{'user_list':user.objects.all()}	)
def user_detail(request,user_id=1):
	return render_to_response('user.html',
										{'user':user.objects.get(id=user_id)}	)
def delete(request, id):
    obj = user.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/user_list/')
