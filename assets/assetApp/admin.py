from django.contrib import admin
from assetApp.models import Employee,Company,Category,Assets

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','address','city','email','phone')

class CompAdmin(admin.ModelAdmin):
    list_display=('name','address','city','email','phone')
class CatAdmin(admin.ModelAdmin):
    list_display=('name','desc')
class AssetAdmin(admin.ModelAdmin):
    list_display=('aNumber','tag','desc')

admin.site.register(Employee,EmpAdmin)
admin.site.register(Company,CompAdmin)
admin.site.register(Category,CatAdmin)
admin.site.register(Assets,AssetAdmin)


