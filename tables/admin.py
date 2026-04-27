from django.contrib import admin
from .models import Tables, Author

# admin.site.register(Books)
# admin.site.register(Author)

@admin.register(Tables)
class TablesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')