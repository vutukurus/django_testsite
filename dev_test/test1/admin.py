from django.contrib import admin

# Register your models here.
from .models import vendor
from .models import student
from .models import uname_pwd



class vendor_admin(admin.ModelAdmin):
	list_display=("title","amount","status")
	ordering = ['amount']
	search_fields = ('title','amount')
	list_filter = ('status','amount')

class student_admin(admin.ModelAdmin):
	list_display=("name","age")

class uname_admin(admin.ModelAdmin):
	list_display=("username","pwd")

admin.site.register(vendor,vendor_admin)
admin.site.register(student,student_admin)
admin.site.register(uname_pwd,uname_admin)

