from django.contrib import admin
from .models import Book

admin.site.register(Book)

admin.site.site_header = "Библиотека"
admin.site.site_title = "Библиотека"
admin.site.index_title = "Управление книгами"
