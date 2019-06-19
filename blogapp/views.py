from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from blogapp.forms import CommentForm , Blog_form
from .models import Blog, Comment

from django.http import HttpResponseRedirect, HttpResponse


def blog_home(request):
    id=''
    if request.user.is_authenticated:
        id=request.user.id
    data=[]
    blogs = Blog.objects.all().order_by('-date')
    for item in blogs:

        data.append({'id':item,'name':item.name,'blog_tittle':item.title,'blog_body':item.half,'blog_day':str(item.date)[8:10],'blog_month':str(item.date)[5:7],
                     'blog_year':str(item.date)[:4],'blog_image':item.image})


    return render(request, 'blog.html', {'blog': data,'id':id})

@login_required(login_url='/login')
def write_blog(request):
    id = ''
    if request.user.is_authenticated:
        id = request.user.id
    email=request.user.email
    if request.method == 'POST':
        blog_form=Blog_form(request.POST, request.FILES)
        if blog_form.is_valid():
            slug1=blog_form.cleaned_data['title']
            slug3=slug1.replace(" ","-")

            Blog.objects.create(name=blog_form.cleaned_data['name'],email=email,slug=slug3,title=blog_form.cleaned_data['title'],body=blog_form.cleaned_data['body'],
                                image=blog_form.cleaned_data['image'])
            return redirect('blogapp:blog_home')
        else:
             print(blog_form.errors)
             return HttpResponse("<h1>form not valid</h1>")
    else:
        blog_show=Blog_form()
        return render(request,'blog-show.html',{'blog':blog_show,'id':id})



def blog_detail(request, post_slug):
    id = ''
    user_email=''
    if request.user.is_authenticated:
        id = request.user.id
        user_email=request.user.email

    data1=[]
    blog = Blog.objects.get(slug=post_slug)
    date=str(blog.date)
    day = date[8:10]
    year = date[:4]
    month=date[5:7]
    email=""
    if request.user.is_authenticated:
        email = request.user.email


    data1.append({'id':blog,'name':blog.name,'blog_tittle':blog.title,'blog_body':blog.body,'blog_date':blog.date,'blog_image':blog.image,'blog_email':blog.email})

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
                               'errors': comment_shows, 'is_liked':is_liked,'day':day,'month':month,'year':year ,'email':email,'blog1':blog,'id':id,'user_email':user_email})
        else:
            return redirect("myshop:login")



    comment_forms = CommentForm()

    return render(request, 'single-blog.html',
                  {'blog': data1 , 'blog_comments': blog_comments, "comment_forms": comment_forms, 'is_liked':is_liked,'day':day,'month':month,'year':year,
                   'blog1':blog,'email':email,'id':id,'user_email':user_email})



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
    comment=Comment.objects.get(id=id)
    post=Blog.objects.get(comment__id=id)
    comment.delete()
    return redirect("/blogapp/"+post.get_absolute_url)


def search_blog(request):
    if request.method == 'POST' :
        search_item= request.POST['search_box']
        if search_item is not None :
            item=Blog.objects.filter(title__icontains=search_item)
            if item :
                for items in item:

                    return redirect("/blogapp/"+items.get_absolute_url)
            else:
                return redirect('blogapp:blog_home')
        else:
            return redirect('blogapp:blog_home')
    return redirect('blogapp:blog_home')


@login_required(login_url="/login")
def blog_edit(request,id):
    user_id= ''
    if request.user.is_authenticated:
        user_id = request.user.id
    object=Blog.objects.get(id=id)

    if(request.method == 'POST'):
        form=Blog_form(request.POST,request.FILES,instance=object)
        if form.is_valid():
            form.save()
            return redirect('blogapp:blog_home')
        else:
            print(form.errors)
    else:
        form = Blog_form(instance=object)
        return render(request,'blog-edit.html',{'blog':object,'form':form,'id':user_id})



def delete_blog(request,id):

    object=Blog.objects.get(id=id)

    object.delete()
    return redirect('blogapp:blog_home')
