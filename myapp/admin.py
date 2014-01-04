from django.contrib import admin
from .models import Thing

class ThingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title',]}
    list_display = ('title','time')
   
admin.site.register(Thing, ThingAdmin)