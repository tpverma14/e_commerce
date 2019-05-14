from django.shortcuts import render
from myshop.models import Category ,Sub_Category ,Banner,Upload_data,Upload_images ,Product

def home(request):
    data  = []
    data1 = []
    product = []
    category=Category.objects.all().order_by('created')

    for category in category:
        data.append({'category': category , 'sub_categories':Sub_Category.objects.filter(categories__id=category.id)})
        # data[category] = Sub_Categorie.objects.filter(categories__id=category.id


    banner_data=Banner.objects.filter(active=True)
    for banner in banner_data:
        data1.append({'banner_name': banner, 'discount':banner.discount ,'banner_image' : Upload_data.objects.filter(banner__id=banner.id)})

    print(data1)

    sub_categoryes = Sub_Category.objects.all()
    for demo in sub_categoryes:
        data11=Product.objects.filter(product_id__id=demo.id)
        for pro_data in data11:
            product.append({'categories':demo ,'product': pro_data ,'images': Upload_images.objects.filter(image_id__id=pro_data.id)})

    print(product)



    return render(request,"home.html",{'data':data ,'banner_data':data1,'product':product})

def login(request):
    return render(request,"login.html")

