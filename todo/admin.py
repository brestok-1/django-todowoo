from django.contrib import admin
from .models import Todo


# Register your models here.
class TodooAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo, TodooAdmin)
