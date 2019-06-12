from decimal import Decimal

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product, Upload_images, Category, Sub_Category, Size_quantity
from .cart import Cart
from .forms import CartAddProductFrom ,Checkout_form
from coupon.forms import CouponApplyForm
from coupon.models import Coupon
from .models import Checkout ,Oder_item



@require_POST
def cart_add(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)


    form = CartAddProductFrom(request.POST)

    if ( form.is_valid()  ):
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
        data1.append({'images' :Upload_images.objects.filter(image_id__id=objects.id),'product_size': Size_quantity.objects.filter(product__id=objects.id)})


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
    cart = Cart(request)


    if (request.method == 'POST'):

        checkout = Checkout_form(request.POST)
        if checkout.is_valid():

            country =checkout.cleaned_data['country']
            first_name =checkout.cleaned_data['first_name']
            last_name =checkout.cleaned_data['last_name']

            address =checkout.cleaned_data['address']
            email =checkout.cleaned_data['email']
            postal_code =checkout.cleaned_data['postal_code']
            city =checkout.cleaned_data['city']
            phone =checkout.cleaned_data['phone']
            other_notes =checkout.cleaned_data['other_notes']
            if cart.coupon:
                coupon=cart.coupon
                discount=cart.coupon.discount
                object = Checkout.objects.create(country=country, first_name=first_name, last_name=last_name,
                                                 address=address, email=email, postal_code=postal_code, city=city
                                                 , phone=phone, other_notes=other_notes,coupon=coupon,discount=discount)
            else:
                object = Checkout.objects.create(country=country, first_name=first_name, last_name=last_name,
                                                 address=address, email=email, postal_code=postal_code, city=city
                                                 , phone=phone, other_notes=other_notes)

            object.save()


            for item in cart:

                discount = Decimal(item['discount_price'])

                if (discount == 0):


                    object1=Oder_item.objects.create(order=object,product=item['product'],price=item['price'],quantity=item['quantity'])

                    object1.save()
                else:

                    object2=Oder_item.objects.create(order=object, product=item['product'], price=item['discount_price'],
                                             quantity=item['quantity'])
                    object2.save()
            cart.clear()
            return redirect("{% url 'paytm:home' %}")
    else:
        checkout1 = Checkout_form()
        return render(request, 'checkout.html',{'checkout':checkout1 , 'cart':cart})

@staff_member_required
def admin_order_detail(request, product_id):
    order = get_object_or_404(Checkout,id=product_id)
    print(order)
    return render(request, 'detail.html', {'order': order})
