
from django.shortcuts import render, redirect, get_object_or_404

from blogapp.forms import CommentForm
from .models import Blog, Comment

from django.http import  HttpResponseRedirect



def blog_home(request):
    data=[]

    blogs = Blog.objects.all().order_by('date')
    for item in blogs:

        data.append({'id':item,'blog_tittle':item.title,'blog_body':item.half,'blog_day':str(item.date)[8:10],'blog_month':str(item.date)[5:7],
                     'blog_year':str(item.date)[:4],'blog_image':item.image})




    return render(request, 'blog.html', {'blog': data})


def blog_detail(request, post_slug):

    data1=[]
    blog = Blog.objects.get(slug=post_slug)
    date=str(blog.date)
    day = date[8:10]
    year = date[:4]
    month=date[5:7]

    data1.append({'id':blog,'blog_tittle':blog.title,'blog_body':blog.body,'blog_date':blog.date,'blog_image':blog.image})

    is_liked = False
    if blog.like.filter(id=request.user.id).exists():
        is_liked=True



    blog_comments = Comment.objects.filter(blog__id=blog.id)

    if request.method == "POST":
        comment_show = CommentForm(request.POST)
        if request.user.is_authenticated:
            if comment_show.is_valid():
                Comment.objects.create(blog=blog, comment=comment_show.cleaned_data['comment'],
                                       email=comment_show.cleaned_data['email'],name=comment_show.cleaned_data['name'])
                return redirect("/blogapp/details-/" + post_slug)
            else:

                for field in comment_show.errors :
                    comment_shows=field


                return render(request, "single-blog.html",
                              {'blog': data1, 'blog_comments': blog_comments, "comment_forms": comment_show,
                               'errors': comment_shows, 'is_liked':is_liked,'day':day,'month':month,'year':year})
        else:
            return redirect("myshop:login")



    comment_forms = CommentForm()
    return render(request, 'single-blog.html',
                  {'blog': data1 , 'blog_comments': blog_comments, "comment_forms": comment_forms, 'is_liked':is_liked,'day':day,'month':month,'year':year,'blog1':blog,})



def like_post(request):
    if request.user.is_authenticated:

        post=get_object_or_404(Blog, id=request.POST.get('post_id'))


        is_liked = False
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            is_liked=False
        else:
            post.like.add(request.user)
            is_liked=True


        return HttpResponseRedirect(post.get_absolute_url)
    else:
        return redirect("myshop:login")




def delete_comment(request,id):
    print("helllloooo",id)
    comment=Comment.objects.get(id=id)
    print(comment)
    post=Blog.objects.get(comment__id=id)
    print(post)
    comment.delete()
    return redirect("/blogapp/"+post.get_absolute_url)



