from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', context={'news': news})



def author(request, id):
    author = Author.objects.get(pk=id)
    publishers = Author.objects.get(pk=id).publishers.all()
    return render(request, 'author_info.html', context={'author': author, 'publishers': publishers})




def create(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else: 
            return redirect('create')
    else:
        return render(request, 'create.html', context={'form': NewPostForm()})



def edit(request, id):
    thisPost = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = NewPostForm(data=request.POST, instance=thisPost)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'edit.html', context={'form':NewPostForm(instance=thisPost)})




def delete(request, id):
    thisPost = Post.objects.get(pk=id)
    thisPost.delete()
    return redirect('homepage')