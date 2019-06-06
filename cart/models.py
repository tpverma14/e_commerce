from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class checkout(models.Model):
    country =models.CharField(max_length=100,db_index=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    company_name = models.CharField(max_length=100)
    address = models.CharField(_('address'), max_length=250)
    email = models.EmailField(_('email'), )
    postal_code = models.CharField(_('postal_code'), max_length=20)
    city = models.CharField(_('city'), max_length=100)
    phone = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)
