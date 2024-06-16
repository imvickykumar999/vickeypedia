# myapp/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('published_date',)

admin.site.register(Book, BookAdmin)
