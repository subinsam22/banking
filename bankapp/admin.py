from django.contrib import admin
from.models import application,District,Branch

# # Register your models here.
class applicationAdmin(admin.ModelAdmin):
    list_display = ['district','branch','name','gender','email','phone_number','address','account_type','age','created']

    list_per_page = 30
admin.site.register(application,applicationAdmin)
admin.site.register(District)
admin.site.register(Branch)