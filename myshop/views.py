from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from myshop.models import Category, Sub_Category, Banner, Upload_data, Upload_images, Product, Category_banner, \
    Size_quantity, Profile
from myshop.forms import Userform, Profileform
from django.contrib.auth import logout


def home(request):
    data = []
    data1 = []
    product = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})
        # data[category] = Sub_Categorie.objects.filter(categories__id=category.id
    feature = []
    feature_product = Product.objects.filter(feature_product=True)
    for object in feature_product:
        feature.append(
            {'product_name': object.brand_name, 'product_price': object.price, 'product_discount': object.discount,
             'product_title': object.title, 'product_slug': object.slug,'image': Upload_images.objects.filter(image_id__id=object.id)})

    banner_data = Banner.objects.filter(active=True)
    for banner in banner_data:
        data1.append({'banner_name': banner, 'discount': banner.discount,
                      'banner_image': Upload_data.objects.filter(banner__id=banner.id)})

    sub_categoryes = Sub_Category.objects.all()
    for demo in sub_categoryes:
        data11 = Product.objects.filter(product_id__id=demo.id)
        for pro_data in data11:
            product.append({'product_slug': pro_data.slug, 'categories': demo, 'slug': demo.slug, 'product': pro_data,
                            'images': Upload_images.objects.filter(image_id__id=pro_data.id)})

    return render(request, "home.html", {'data': data, 'banner_data': data1, 'product': product, 'user': request.user,'feature':feature})


def category(request, post_slug):
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
            data1.append({'product_name': info1.brand_name, 'product_title': info1.title, 'product_price': info1.price,
                          'product_discount': info1.discount,
                          'product_slug': info1.slug, 'image': Upload_images.objects.filter(image_id__id=info1.id)})

    return render(request, "category-1.html",
                  {'data': data, 'object': object, 'data1': data1, 'image_object': image_object, 'product': product,
                   'user': request.user})


def subcategory(request, post_slug):
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1 = []
    object = Sub_Category.objects.get(slug=post_slug)
    object1 = Product.objects.filter(product_id__id=object.id)
    for info in object1:
        data1.append({'product_name': info.brand_name, 'product_price': info.price, 'product_title': info.title,
                      'product_slug': info.slug, 'product_discount': info.discount,
                      'image': Upload_images.objects.filter(image_id__id=info.id)})

    return render(request, "category-2.html", {'data': data, 'data1': data1, 'object1': object1, 'user': request.user})


def product_detail(request, post_slug):
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1 = []
    object = Product.objects.get(slug=post_slug)
    data1.append({'product_name': object.brand_name, 'product_price': object.price, 'product_discount': object.discount,
                  'product_title': object.title, 'additional_description': object.additional_description,
                  'product_size': Size_quantity.objects.filter(product__id=object.id),
                  'product_description': object.description,
                  'image': Upload_images.objects.filter(image_id__id=object.id)})
    is_liked = False
    if object.like.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, "product-detail.html",
                  {'data': data, 'data1': data1, 'user': request.user, 'is_liked': is_liked, 'object': object})


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

            user = Profile.objects.get(phone=username).user

            if user.check_password(password):

                return redirect("/")
            else:

                return HttpResponse("<h1> INVALID </h1>")
        else:

            user = authenticate(username=username, password=password)
            if user is not None:

                auth_login(request, user)
                return redirect("/")
            else:
                return HttpResponse("<h1> INVALID </h1>")
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
