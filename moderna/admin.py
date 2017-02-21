from django.contrib import admin
from .models import Category, Paper, Tag, Source
# Register your models here.


admin.site.register(Category)
admin.site.register(Paper)
admin.site.register(Tag)
admin.site.register(Source)
