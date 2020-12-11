from __future__ import unicode_literals

from django.contrib import admin
from .models import Categories,Product
# Register your models here.

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Categories)
admin.site.register(Product)
