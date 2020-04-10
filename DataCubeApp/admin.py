from django.contrib import admin
from .models import Algorithm
from .models import Input

# Register your models here.
admin.site.register(Algorithm)
admin.site.register(Input)