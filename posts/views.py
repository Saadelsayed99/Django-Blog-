from django.shortcuts import render

from .models import post


def post_list(request):
    data = post.objects.all()    # orm ---> sql ---> db ---> list[all posts]
    return render(request,'posts.html',{'posts':data})