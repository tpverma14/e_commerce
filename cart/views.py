from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product ,Upload_images
from .cart import Cart
from .forms import CartAddProductFrom
from coupon.forms import CouponApplyForm



@require_POST
def cart_add(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    image=Upload_images.objects.filter(image_id__id=product.id)

    form = CartAddProductFrom(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    data=[]
    for item in cart:
        item['update_quantity_form'] = CartAddProductFrom(initial={'quantity': item['quantity'], 'update': True})
        coupon_apply_form = CouponApplyForm()

    for item1 in cart:
        objects=item1['product']
        data.append({'image':Upload_images.objects.filter(image_id__id=objects.id)})


    return render(request, 'cart.html', {'cart': cart,
                                                'coupon_apply_form': coupon_apply_form,'data':data})
