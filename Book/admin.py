from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "price"]
    list_filter = ["title", "author"]
    search_fields = ["title", "author"]

admin.site.register(Book, BookAdmin)
