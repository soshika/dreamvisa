from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog


def allblog(request):
    last_three = Blog.objects.order_by('-id')[:3][::-1]
    last_three = reversed(last_three)

    blog_list = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 3)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog/allblog.html', {'rblogs': last_three,
                                                 'blogs': blogs})


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    last_three = Blog.objects.order_by('-id')[:3][::-1]
    last_three = reversed(last_three)

    return render(request, 'blog/detail.html', {'rblogs': last_three,
                                                'blog': detail_blog})
