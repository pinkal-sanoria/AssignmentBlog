from django.shortcuts import render
from blog.models import Blog
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def blogs(request):
    blog = Blog.objects.order_by('-id')
    p = Paginator(blog,5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'blogs':page_obj}
   
    return render(request,'blog/blogs.html',context)

# def blog_details(request,id):
#     blog = Blog.objects.get(id=id)
#     context = {'blog': blog}
#     return render(request,'blog/blogdata.html',context)    


def blog_details(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog/blog_details.html',context)