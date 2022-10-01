from django.contrib import admin
from todo.models import Contact, Todo


# Register your models here.
admin.site.register(Todo)
admin.site.register(Contact)