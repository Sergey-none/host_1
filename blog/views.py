from django.shortcuts import render, get_object_or_404 
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
import os
from django.utils import timezone 
from .forms import PostForm
from django.shortcuts import redirect
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .obj import upload_f
# Imaginary function to handle an uploaded file.
'''def file(request,Post):
    newdoc = Document(docfile = request.FILES['file'])
    newdoc.save()
    f_url = iter(request.FILES)'''

def post_list(request):
    posts = Post.published.all() 
    return render(request, 
              'blog/post/list.html', 
              {'posts': posts})
    '''object_list = Post.published.all()  
    paginat = Paginator(object_list, 6)  # 3 поста на каждой странице  
    page_0 = request.GET.getlist('page')[0]
    try:  
        posts = paginat.page(page_0)
    except ProgrammingError:
    	posts = paginat.page(1)
    except PageNotAnInteger:  
        # Если страница не явл	яется целым числом, поставим первую страницу  
        posts = paginat.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginat.page(paginat.num_pages)
    return render(request,  
	          'blog/post/list.html',  
		  {'page': page_0,  
		   'posts': posts})'''
def post_new(request):
    form = PostForm()
    if request.method == "POST":
        print(form)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Post(file_f=request.FILES['file_f'], slug = request.POST['slug'], title = request.POST['title'], body = request.POST['body'])
            instance.save()
            return redirect("../")
            #a = Post(file = request.FILES t)
            #a.save()
            '''post = form.save(commit=False)'''
            '''file_name = 
            post.file = request.FILES[file_name]
            
            '''
            #f = request.POST.get('file')
            #form.save()
            #print(f)
            #form.save()
            '''filename = settings.MEDIA_URL + post.file()
            with open(settings.MEDIA_ROOT + filename, 'wb') as f:
                for chunk in request.FILES['file'].chunks():
                    f.write(chunk)
            return redirect(filename)'''
    else:
        form = PostForm()
    return render(request, 'blog/post-edit.html', {'form': form})

def post_detail(request, year, month, day, post):
        post = get_object_or_404(Post,slug=post, status='published', publish__year=year, publish__month=month, publish__day=day) 
        return render(request,
        'blog/post/detail.html',
        {'post': post})



		#f_url = MEDIA_URL + '/files/' + iter(request.FILES)
		#global newdoc
        #newdoc = Document(docfile = request.FILES['file'])
        #newdoc.save()
