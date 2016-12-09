from django.contrib import admin

from .models import Cinema


class InlineImage(admin.TabularInline):
    model = Cinema


class MovieAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

# Register your models here.

admin.site.register(Cinema)
