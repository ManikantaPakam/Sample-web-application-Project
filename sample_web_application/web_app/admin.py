from django.contrib import admin
from web_app.models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['food_name','review']

admin.site.register(Review,ReviewAdmin)