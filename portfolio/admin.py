from django.contrib import admin
from portfolio.models import Aboutme,Workingstyle,Myexperience,Offering,Myprojects,Myskils,Uploadcv

# Register your models here.
admin.site.register(Aboutme)
admin.site.register(Myexperience)
admin.site.register(Offering)
admin.site.register(Myprojects)
admin.site.register(Myskils)
admin.site.register(Workingstyle)
admin.site.register(Uploadcv)