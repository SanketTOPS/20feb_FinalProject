from django.contrib import admin
from .models import *

# Register your models here.
class notesData(admin.ModelAdmin):
    list_display=['id','created','title','opt','myfile','desc']

class feedbackData(admin.ModelAdmin):
    list_display=['id','name','email','phone','msg']

admin.site.register(usersignup)
admin.site.register(notes,notesData)
admin.site.register(feedback,feedbackData)
