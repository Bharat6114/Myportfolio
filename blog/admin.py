from django.contrib import admin
from blog.models import Category,Blogs,Comment,Reply
# Register your models here.
admin.site.register(Category)
admin.site.register(Blogs)
admin.site.register(Comment)
admin.site.register(Reply)