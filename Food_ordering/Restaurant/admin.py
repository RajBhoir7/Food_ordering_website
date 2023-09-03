from django.contrib import admin
from Restaurant import models
# Register your models here.

#admin.site.register(models.Rest_details)
admin.site.register(models.Login_details)
#admin.site.register(models.Menu)


@admin.register(models.Rest_details)
class Rest_details(admin.ModelAdmin):
    list_display=('Rest_name','Owner_name','Rest_location')



    
@admin.register(models.Menu)
class Menu(admin.ModelAdmin):
    list_display=('Rest_name',)



