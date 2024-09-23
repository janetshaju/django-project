from django.contrib import admin
from .models import Category, Book
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Define resources for import/export
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name')  # Specify the fields to be imported/exported

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense')
        # Specify any additional configuration options like export_order if needed

# Update the CategoryAdmin class to enable import/export functionality
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource  # Link the CategoryResource
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('name',)

# Update the BookAdmin class to enable import/export functionality
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BookResource  # Link the BookResource
    list_display = (
        'title', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense'
    )
    search_fields = ('title', 'authors', 'publisher')
    list_filter = ('category', 'published_date')
    ordering = ('-published_date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense')
        }),
        ('Advanced options', {
            'classes': ('collapse',),  # Add collapsible section if needed
            'fields': (),  # Ensure this is not duplicating fields
        }),
    )
