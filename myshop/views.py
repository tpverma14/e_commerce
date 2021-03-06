from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from myshop.models import Category, Sub_Category, Banner, Upload_data, Upload_images, Product, Category_banner, \
    Size_quantity, Profile
from myshop.forms import Userform, Profileform
from django.contrib.auth import logout
from cart.forms import CartAddProductFrom
from blogapp.models import Blog


def home(request):
    data = []
    data1 = []
    product = []
    id = ""
    if request.user.is_authenticated:
        id = request.user.id

    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})
        # data[category] = Sub_Categorie.objects.filter(categories__id=category.id)

    feature_items = []

    featured_object=Sub_Category.objects.filter(featured_department=True)
    for feature_data in featured_object:

        feature_product = Product.objects.filter(product_id__id=feature_data.id , feature_product=True)

        feature = []
        for object in feature_product:
            feature.append(
                {'product_id': object.id, 'product_name': object.brand_name, 'product_price': object.price,
                 'product_discount': object.discount,
                 'discount_price': object.discount_price, 'product_title': object.title, 'product_slug': object.slug,
                 'image': Upload_images.objects.filter(image_id__id=object.id)})
        feature_items.append({'department':feature_data.product_name,'product_data':feature})




    banner_data = Banner.objects.filter(active=True)
    for banner in banner_data:
        data1.append({'banner_name': banner, 'discount': banner.discount,
                      'banner_image': Upload_data.objects.filter(banner__id=banner.id)})

    sub_categoryes = Sub_Category.objects.all()
    for demo in sub_categoryes:
        data11 = Product.objects.filter(product_id__id=demo.id)
        for pro_data in data11:
            product.append(
                {'product_id': pro_data.id, 'product_slug': pro_data.slug, 'categories': demo, 'slug': demo.slug,
                 'product': pro_data, 'discount_price': pro_data.discount_price,
                 'images': Upload_images.objects.filter(image_id__id=pro_data.id)})

    blog_item=[]
    blog_data=Blog.objects.all().order_by('-date')
    for item in blog_data:

        blog_item.append({'id':item,'name':item.name,'blog_title':item.title,'blog_day':str(item.date)[8:10],'blog_month':str(item.date)[5:7],
                     'blog_year':str(item.date)[:4],'blog_image':item.image})

    return render(request, "home.html",
                  {'data': data, 'banner_data': data1, 'product': product, 'user': request.user, 'feature': feature_items,
                   'id': id,'blog_item':blog_item})


def category(request, post_slug):
    id = ""
    if request.user.is_authenticated:
        id = request.user.id
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1 = []
    object = Category.objects.get(slug=post_slug)
    image_object = Category_banner.objects.filter(category_banner__id=object.id)
    object1 = Sub_Category.objects.filter(categories__id=object.id)
    for info in object1:
        product = Product.objects.filter(product_id__id=info.id)
        for info1 in product:
            data1.append({'product_id': info1.id, 'product_name': info1.brand_name, 'product_title': info1.title,
                          'product_price': info1.price,
                          'product_discount': info1.discount, 'discount_price': info1.discount_price,
                          'product_slug': info1.slug, 'image': Upload_images.objects.filter(image_id__id=info1.id)})

    return render(request, "category-1.html",
                  {'data': data, 'object': object, 'data1': data1, 'image_object': image_object, 'product': product,
                   'user': request.user, 'id': id})


def subcategory(request, post_slug):
    id = ""
    if request.user.is_authenticated:
        id = request.user.id
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1 = []
    object = Sub_Category.objects.get(slug=post_slug)
    object1 = Product.objects.filter(product_id__id=object.id)
    for info in object1:
        data1.append({'product_id': info.id, 'product_name': info.brand_name, 'product_price': info.price,
                      'product_title': info.title,
                      'product_slug': info.slug, 'product_discount': info.discount,
                      'discount_price': info.discount_price,
                      'image': Upload_images.objects.filter(image_id__id=info.id)})

    return render(request, "category-2.html",
                  {'data': data, 'data1': data1, 'object1': object1, 'user': request.user, 'id': id})


def product_detail(request, post_slug):
    id = ""
    if request.user.is_authenticated:
        id = request.user.id
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1 = []
    object = Product.objects.get(slug=post_slug)
    data1.append({'product_id': object.id, 'product_name': object.brand_name, 'product_price': object.price,
                  'product_discount': object.discount,
                  'product_title': object.title, 'additional_description': object.additional_description,
                  'discount_price': object.discount_price,
                  'product_size': Size_quantity.objects.filter(product__id=object.id),
                  'product_description': object.description,
                  'image': Upload_images.objects.filter(image_id__id=object.id)})


    is_liked = False
    if object.like.filter(id=request.user.id).exists():
        is_liked = True

    cart_product_form = CartAddProductFrom()
    return render(request, "product-detail.html",
                  {'data': data, 'cart_product_form': cart_product_form, 'data1': data1, 'user': request.user,
                   'is_liked': is_liked, 'object': object, 'id': id})


def sign_up(request):
    if request.method == "POST":
        userform = Userform(request.POST)
        profileform = Profileform(request.POST)

        if (userform.is_valid()) and (profileform.is_valid()):

            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            first_name = userform.cleaned_data['first_name']
            last_name = userform.cleaned_data['last_name']
            password = userform.cleaned_data['password']
            mobile_number = profileform.cleaned_data['mobile_number']

            user = User.objects.create(username=username, last_name=last_name, first_name=first_name, email=email)
            user.set_password(password)
            user._otherfield = mobile_number
            user.save()

            mobile_number = profileform.cleaned_data['mobile_number']
            Profile.objects.create(user=user, mobile_number=mobile_number)

            auth_login(request, user)
            return redirect("/")
        else:
            return render(request, "signup.html",
                          {"userform": userform, "profileform": profileform, 'error': userform.errors})
            # return HttpResponse("<h1>invalid</h1>")
    else:
        userform = Userform()
        profileform = Profileform()
        return render(request, "signup.html", {"userform": userform, "profileform": profileform})


def log_in(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username.isdigit()):

            user = Profile.objects.get(mobile_number=username).user

            if user.check_password(password):

                return redirect("/")
            else:

                return HttpResponse(
                    "<center><h1> INVALID </h1> <br> <br> <h2><a href='/login'> Try Login Again </a></h2> <br> <br> <h2><a href='/sign_up'> Go For Signup </a></h2></center> ")
        else:

            user = authenticate(username=username, password=password)
            if user is not None:

                auth_login(request, user)
                return redirect("/")
            else:
                return HttpResponse(
                    "<center><h1> INVALID </h1> <br> <br> <h2><a href='/login'> Try Login Again </a></h2> <br> <br> <h2><a href='/sign_up'> Go For Signup </a></h2></center> ")
    else:

        return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect("/")


def like(request):
    if request.user.is_authenticated:

        post = get_object_or_404(Product, id=request.POST.get('post_id'))

        is_liked = False
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            is_liked = False
        else:
            post.like.add(request.user)
            is_liked = True

        return redirect(post.get_absolute_url)
    else:
        return redirect("myshop:login")


def search(request):
    if request.method == 'POST':
        search_item = request.POST['search_box']
        if search_item is not None:
            item = Sub_Category.objects.filter(product_name__icontains=search_item)
            if item is not None:
                for items in item:

                    return redirect(items.get_absolute_url_sub)
            else:
                return HttpResponse(
                    '<center><h1> NOT FOUND </h1> <br> <br> <h2><a href="/"> GO TO HOME PAGE </a></h2> <br> <br> </center>')
        else:
            return redirect('/')
    return redirect('/')


def profile(request, id):
    object = id
    user_object = User.objects.get(id=id)

    if user_object.id == 1:
        return redirect('myshop:home')
    else:
        profile_object = Profile.objects.get(user__id=user_object.id)
        return render(request, "profile.html", {'user': user_object, 'profile': profile_object, 'object': object})


def check_account(request, id):
    object = id
    user_object = User.objects.get(id=id)
    username = user_object.username
    if request.method == "POST":

        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:

            auth_login(request, user)
            return redirect("/profile_edit/" + object)
        else:
            return redirect('/')


    else:
        return render(request, "login.html", {'username': username, 'id': object})


def profile_edit(request, id):
    object = id
    user_object = User.objects.get(id=id)
    profile_object = Profile.objects.get(user__id=user_object.id)
    if request.method == 'POST':
        userform = Userform(request.POST, instance=user_object)
        profileform = Profileform(request.POST, instance=profile_object)
        if (userform.is_valid()) and (profileform.is_valid()):
            user = userform.save(commit=False)
            mobile_number = profileform.cleaned_data['mobile_number']
            user.set_password(userform.cleaned_data['password'])
            user._otherfield = mobile_number
            user.save()
            profileform.save()

            auth_login(request, user_object)

            return redirect('myshop:home')
        else:
            print(userform.errors, profileform.errors)
    else:
        userform = Userform(instance=user_object)
        profileform = Profileform(instance=profile_object)
        return render(request, "profile-edit.html", {'user': userform, 'profile': profileform, 'object': object})


def delete_profile(request, id):
    user_object = User.objects.get(id=id)
    user_object.delete()
    return redirect('myshop:home')













#full text search in django