from django.contrib import admin
from .models import Contact
from .models import Images

# Register your models here.
class Comment(admin.ModelAdmin):
    admin.site.site_header = "Kitan Cleaning Service"
    admin.site.site_title = "Cleaning Service"
    admin.site.index_title = "Cleaning Service"
    list_display = ('name','email','phone','message')
    list_editable = ('email','phone',)

class ImageComment(admin.ModelAdmin):
    list_display = ('image',)


admin.site.register(Contact,Comment)
admin.site.register(Images,ImageComment)