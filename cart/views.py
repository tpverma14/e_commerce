from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product ,Upload_images ,Category,Sub_Category
from .cart import Cart
from .forms import CartAddProductFrom
from coupon.forms import CouponApplyForm
from coupon.models import Coupon



@require_POST
def cart_add(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)


    form = CartAddProductFrom(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

    return redirect('cart:cart_detail')






def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    m=len(cart)
    if m == 0:
        return redirect('myshop:home')
    else:
        return redirect('cart:cart_detail')






def cart_detail(request):
    cart = Cart(request)
    data1=[]
    data=[]
    m = len(cart)
    if m == 0:
        return redirect('myshop:home')
    for item in cart:
        item['update_quantity_form'] = CartAddProductFrom(initial={'quantity': item['quantity'], 'update': True})
        coupon_apply_form = CouponApplyForm()

    for item1 in cart:
        objects=item1['product']
        data1.append({'images' :Upload_images.objects.filter(image_id__id=objects.id)})


    category = Category.objects.all().order_by('created')
    for category in category:
        data.append({'category': category, 'sub_categories': Sub_Category.objects.filter(categories__id=category.id)})
    user=request.user




    return render(request, 'cart.html', {'cart': cart,
                                                'coupon_apply_form': coupon_apply_form,'data1':data1,'data':data,'user':user})

def coupon_avaliable(request):
    coupons = []
    coupon = Coupon.objects.filter(active=True)
    for items in coupon:
        coupons.append({'coupons': items})

    return render(request,'coupon.html',{'coupons':coupons})




def checkout(request):
    return render(request,'checkout.html')