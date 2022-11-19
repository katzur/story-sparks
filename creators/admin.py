from django.contrib import admin
from .models import Creator


class CreatorAdmin(admin.ModelAdmin):
    list_display = ("name", "job")
    ordering = ("name",)


admin.site.register(Creator, CreatorAdmin)
