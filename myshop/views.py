from django.shortcuts import render
from myshop.models import Category ,Sub_Category , Product ,Upload_background_image

def home(request):
    data = []
    category=Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories':Sub_Category.objects.filter(categories__id=category.id)})
        # data[category] = Sub_Categorie.objects.filter(categories__id=category.id)




    upload_bg_image=Upload_background_image.objects.all()

    return render(request,"home.html",{'data':data ,'upload_bg_image':upload_bg_image})

def login(request):
    return render(request,"login.html")

