from .models import  Bid, Item, ItemComment
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# admin.site.register(User, UserAdmin)
admin.site.register(Item)
admin.site.register(Bid)
admin.site.register(ItemComment)
