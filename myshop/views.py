from django.shortcuts import render
from myshop.models import Category ,Sub_Category ,Banner,Upload_data,Upload_images

def home(request):
    data  = []
    data1 = []
    category=Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories':Sub_Category.objects.filter(categories__id=category.id)})
        # data[category] = Sub_Categorie.objects.filter(categories__id=category.id

    banner_data=Banner.objects.all()
    for banner in banner_data:
        data1.append({'banner_name': banner, 'banner_image' : Upload_data.objects.filter(banner__id=banner.id)})

    print(category)
    print(banner_data)
    print(data1)
    image=Upload_data.objects.all()
    print(image)
    upload=Upload_images.objects.all()
    print(upload,"hdgcdh")
    return render(request,"home.html",{'data':data ,'banner_data':data1})

def login(request):
    return render(request,"login.html")

