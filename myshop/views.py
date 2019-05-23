from django.shortcuts import render , HttpResponse
from myshop.models import Category ,Sub_Category ,Banner,Upload_data,Upload_images ,Product , Category_banner

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



    sub_categoryes = Sub_Category.objects.all()
    for demo in sub_categoryes:
        data11=Product.objects.filter(product_id__id=demo.id)
        for pro_data in data11:
            product.append({'categories':demo ,'product': pro_data ,'images': Upload_images.objects.filter(image_id__id=pro_data.id)})


    return render(request,"home.html",{'data':data ,'banner_data':data1,'product':product})

def category(request,post_slug):
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})


    data1=[]
    object=Category.objects.get(slug=post_slug)
    image_object=Category_banner.objects.filter(category_banner__id=object.id)
    object1=Sub_Category.objects.filter(categories__id=object.id)
    for info in object1:
        product=Product.objects.filter(product_id__id=info.id)
        for info1 in product:
            data1.append({'product_name':info1.brand_name,'product_price':info1.price,'product_discount':info1.discount,
                          'product_slug':info1.slug,'image':Upload_images.objects.filter(image_id__id=info1.id)})

    print(data1)
    return render(request,"category-1.html",{'data':data,'object':object,'data1':data1,'image_object':image_object,'product':product})


def subcategory(request,post_slug):
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1=[]
    object=Sub_Category.objects.get(slug=post_slug)
    object1=Product.objects.filter(product_id__id=object.id)
    for info in object1:
        data1.append({'product_name':info.brand_name,'product_price':info.price,
                      'product_slug':info.slug,'product_discount':info.discount,'image':Upload_images.objects.filter(image_id__id=info.id)})

    print(data1)
    return render(request,"category-2.html",{'data':data,'data1':data1,'object1':object1})



def product_detail(request,post_slug):
    data = []
    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})

    data1=[]
    object=Product.objects.get(slug=post_slug)
    data1.append({'product_name':object.brand_name,'product_price':object.price,'product_discount':object.discount,
                  'product_description':object.description,'image':Upload_images.objects.filter(image_id__id=object.id)})


    return render(request,"product-detail.html",{'data':data,'data1':data1})

def login(request):
    return render(request,"login.html")

