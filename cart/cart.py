from decimal import Decimal
from django.conf import settings
from myshop.models import Product, Upload_images
from coupon.models import Coupon


class Cart(object):
    def __init__(self, request):
        """
        cart initialise
        """
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        self.coupon_id = self.session.get('coupon_id')

        if not cart:
            # save empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def add(self, product, quantity=1, update_quantity=False):

        """
        add product to cart or update its quantity
        """

        c = 0
        images = Upload_images.objects.filter(image_id__id=product.id)
        for i in images:
            if (c == 0):
                image = i.image.url
                c = c + 1

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price),
                                     'discount_price': str(product.discount_price),
                                     'image': image}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():

            discount = Decimal(item['discount_price'])

            if (discount == 0):

                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']

                yield item


            else:

                item['discount_price'] = Decimal(item['discount_price'])
                item['total_price'] = item['discount_price'] * item['quantity']

                yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        sum3 = 0
        sum4 = 0
        for item in self.cart.values():
            discount = Decimal(item['discount_price'])
            if (discount == 0):
                price1 = Decimal(item['price'])
                sum1 = price1 * item['quantity']
                sum3 = sum1 + sum3


            else:
                price2 = Decimal(item['discount_price'])
                sum2 = price2 * item['quantity']
                sum4 = sum2 + sum4

        object = sum3 + sum4

        return object

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
