from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import RawPostForm
from django.http import HttpResponse
from tablib import Dataset
# Create your views here.
def file_view(request):
    my_post  = Post.objects.all()
    context = {
        'my_post': my_post
        }
    return render(request, 'file_view.html',context)
def upload_view(request):
    return render(request, 'simple_upload.html')
def post_create_view(request):
    print(request.GET)
    print(request.POST)
    my_form = RawPostForm()
    if request.method == "POST":
        my_form= RawPostForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data.get('title'))
            Post.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context=  {
        'my_form': my_form,
        'post' :Post
    }
    return render(request,'create_post.html',context)
    # return render(request,'home.html')
def first_view(request):
    obj = Post.objects.get(id = 1)
    context=  {
        "post_title": obj.title,
        "post_slug ": obj.slug,
        "post_description": obj.description,
        "post_published": obj.published,
        "post_created": obj.created,
        "post_content": obj.content
    }
    all_post = Post.objects.all()
    new_context = {"all_post":all_post}
    return render(request,'home.html',new_context)
def detail_view(request,post_id):
    detail = Post.objects.get(id = post_id)
    return render(request,'detail.html',{"detail": detail})