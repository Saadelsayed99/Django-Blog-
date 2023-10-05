from django.shortcuts import render

from .models import post


def post_list(request):
    data = post.objects.all()    # orm ---> sql ---> db ---> list[all posts]
    return render(request,'posts.html',{'posts':data})


def post_detail(request,post_id):
    date = post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':date})