# blogging/views.py

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post


def list_view(request):
	published = Post.objects.exclude(published_date__exact=None)
	posts = published.order_by('-published_date')
	context = {'posts': posts}
	return render(request, 'blogging/list.html', context)
