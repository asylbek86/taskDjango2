from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello_world_view(request):
    return HttpResponse(
        "<h1> My name is Bektur <h2/>"
    )

# post_views
def post_view(request):
    post = models.Post.objects.all()
    return render(request, template_name= 'index.html', context= {'post': post})