from django.contrib import admin
from .models import Post,Document
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Post)
admin.site.register(Document)
@admin.register(Post)
class PersonAdmin(ImportExportModelAdmin):
    pass